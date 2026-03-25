from rest_framework import serializers
from .models import Order, OrderItem, Cart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'subtotal']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price', 'created_at', 'updated_at']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    is_cancelled = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'customer', 'status', 'total_amount',
            'shipping_address', 'notes', 'payment_method', 'items', 
            'is_cancelled', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'order_number', 'customer', 'created_at', 'updated_at']

class CreateOrderSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(max_length=500)
    
    def validate(self, attrs):
        user = self.context['request'].user
        cart = getattr(user, 'cart', None)
        
        if not cart or not cart.items.exists():
            raise serializers.ValidationError("Cart is empty")
        
        return attrs
