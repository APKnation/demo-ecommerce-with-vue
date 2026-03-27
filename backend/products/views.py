from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductCreateSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def category_create(request):
    if not request.user.is_staff and not request.user.is_admin_user:
        return Response({'error': 'Only staff and admins can create categories'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product_list(request):
    products = Product.objects.filter(is_active=True)
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def product_create(request):
    if not request.user.is_staff and not request.user.is_admin_user:
        return Response({'error': 'Only staff and admins can create products'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Debug: Print what we're receiving
    print(f"DEBUG: Content-Type: {request.content_type}")
    print(f"DEBUG: Request data: {request.data}")
    print(f"DEBUG: Request FILES: {request.FILES}")
    
    # Handle both JSON and FormData
    if request.content_type and 'multipart/form-data' in request.content_type:
        # FormData handling - add author to data
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = ProductCreateSerializer(data=data)
    else:
        # JSON handling - add author to data
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = ProductCreateSerializer(data=data)
    
    print(f"DEBUG: Serializer valid: {serializer.is_valid()}")
    if not serializer.is_valid():
        print(f"DEBUG: Serializer errors: {serializer.errors}")
    
    if serializer.is_valid():
        serializer.save()
        return Response(ProductSerializer(serializer.instance).data, 
                       status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def product_manage(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'DELETE':
        if product.author != request.user and not request.user.is_staff and not request.user.is_admin_user:
            return Response({'error': 'Permission denied'}, 
                           status=status.HTTP_403_FORBIDDEN)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        if product.author != request.user and not request.user.is_staff and not request.user.is_admin_user:
            return Response({'error': 'Permission denied'}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProductCreateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def my_products(request):
    products = Product.objects.filter(author=request.user)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
