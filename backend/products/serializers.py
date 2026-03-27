from rest_framework import serializers
from django.conf import settings
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    image = serializers.SerializerMethodField()
    is_in_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price', 'condition', 'category', 'category_id',
            'author', 'image', 'stock', 'is_active', 'is_in_stock', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return f"{settings.MEDIA_URL}{obj.image.name}"
        return None

class ProductCreateSerializer(serializers.ModelSerializer):
    # Simplified - no image processing for now
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price', 'condition', 'category', 'image',
            'stock', 'is_active', 'author'
        ]
    
    def create(self, validated_data):
        # author will be passed from view, so remove it from validated_data
        # but ensure it's set before creating the product
        author = validated_data.pop('author', None)
        product = Product.objects.create(author=author, **validated_data)
        return product
