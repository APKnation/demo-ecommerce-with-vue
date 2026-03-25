from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Order, OrderItem, Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer, CreateOrderSerializer
from products.models import Product
import uuid

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        product_id=product_id,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def cart_item_manage(request, pk):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = get_object_or_404(CartItem, pk=pk, cart=cart)
    
    if request.method == 'DELETE':
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        quantity = request.data.get('quantity')
        if quantity and quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)
        return Response({'error': 'Invalid quantity'}, 
                       status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def create_order(request):
    """Create order from cart or directly from items"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Handle order creation from cart items or direct items
    items_data = request.data.get('items', [])
    shipping_address = request.data.get('shipping_address', '')
    notes = request.data.get('notes', '')
    payment_method = request.data.get('payment_method', 'cash')
    
    # If no items provided, use cart items
    if not items_data and cart.items.exists():
        items_data = [
            {
                'product': cart_item.product.id,
                'quantity': cart_item.quantity,
                'price': str(cart_item.product.price)
            }
            for cart_item in cart.items.all()
        ]
    
    if not items_data:
        return Response({'error': 'No items to order'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    # Calculate total amount
    total_amount = sum(
        float(item['price']) * int(item['quantity']) 
        for item in items_data
    )
    
    order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
    
    order = Order.objects.create(
        customer=request.user,
        order_number=order_number,
        total_amount=total_amount,
        shipping_address=shipping_address,
        notes=notes,
        payment_method=payment_method
    )
    
    # Create order items
    for item_data in items_data:
        OrderItem.objects.create(
            order=order,
            product_id=item_data['product'],
            quantity=item_data['quantity'],
            price=item_data['price']
        )
        
        # Update product stock
        product = Product.objects.get(id=item_data['product'])
        product.stock -= int(item_data['quantity'])
        product.save()
    
    # Clear cart if it was used
    if cart.items.exists():
        cart.items.all().delete()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, customer=request.user)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_order_status(request, pk):
    """Update order status (admin only)"""
    order = get_object_or_404(Order, pk=pk)
    new_status = request.data.get('status')
    
    if new_status not in dict(Order.STATUS_CHOICES):
        return Response({'error': 'Invalid status'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    order.status = new_status
    order.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def update_order_status_user(request, pk):
    """Update order status (user can mark as paid, cancel pending)"""
    order = get_object_or_404(Order, pk=pk, customer=request.user)
    new_status = request.data.get('status')
    
    if new_status not in dict(Order.STATUS_CHOICES):
        return Response({'error': 'Invalid status'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    # Users can only cancel pending orders or mark as paid
    if new_status == 'cancelled' and order.status != 'pending':
        return Response({'error': 'Only pending orders can be cancelled'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    if new_status == 'paid' and order.status != 'pending':
        return Response({'error': 'Only pending orders can be marked as paid'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    order.status = new_status
    order.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def cancel_order(request, pk):
    """Cancel a pending order"""
    order = get_object_or_404(Order, pk=pk, customer=request.user)
    
    if order.status != 'pending':
        return Response({'error': 'Only pending orders can be cancelled'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    order.status = 'cancelled'
    order.save()
    
    # Restore product stock
    for item in order.items.all():
        item.product.stock += item.quantity
        item.product.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_order_paid(request, pk):
    """Mark order as paid"""
    return update_order_status_user(request, pk)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_order_shipped(request, pk):
    """Mark order as shipped (admin only)"""
    if not request.user.is_staff:
        return Response({'error': 'Permission denied'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    order = get_object_or_404(Order, pk=pk)
    
    if order.status != 'paid':
        return Response({'error': 'Only paid orders can be shipped'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    order.status = 'shipped'
    order.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_order_delivered(request, pk):
    """Mark order as delivered (admin only)"""
    if not request.user.is_staff:
        return Response({'error': 'Permission denied'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    order = get_object_or_404(Order, pk=pk)
    
    if order.status != 'shipped':
        return Response({'error': 'Only shipped orders can be delivered'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    order.status = 'delivered'
    order.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)
