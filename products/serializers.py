from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    images = ProductImageSerializer(many=True, read_only=True)
    is_in_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price', 'condition', 'category', 'category_id',
            'author', 'image', 'images', 'stock', 'is_active', 'is_in_stock', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class ProductCreateSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price', 'condition', 'category', 'image',
            'stock', 'is_active', 'images'
        ]
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        
        return product
