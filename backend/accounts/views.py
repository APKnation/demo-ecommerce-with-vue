from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from .models import User
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserSerializer, 
    UserThemeSerializer, UserProfileSerializer
)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully. Please login to get token.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except:
        pass
    logout(request)
    return Response({'message': 'Logged out successfully'})

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAdminUser])
def admin_user_detail(request, pk):
    """Get user details or delete user (admin only)"""
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        # Prevent admin from deleting themselves
        if user == request.user:
            return Response({'error': 'Cannot delete your own account'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        user.delete()
        return Response({'message': 'User deleted successfully'}, 
                       status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def admin_update_user(request, pk):
    """Update user role or details (admin only)"""
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Prevent admin from demoting themselves
    if user == request.user:
        return Response({'error': 'Cannot modify your own account through admin panel'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    # Only allow updating certain fields
    allowed_fields = ['first_name', 'last_name', 'email', 'role', 'is_active', 'phone', 'address']
    update_data = {k: v for k, v in request.data.items() if k in allowed_fields}
    
    serializer = UserSerializer(user, data=update_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def admin_dashboard_stats(request):
    """Get admin dashboard statistics"""
    from orders.models import Order
    from products.models import Product
    
    # Calculate order statistics
    all_orders = Order.objects.all()
    completed_orders = all_orders.filter(status='delivered')
    pending_orders = all_orders.filter(status='pending')
    
    # Calculate revenue
    total_revenue = sum(float(order.total_amount) for order in completed_orders)
    total_revenue = round(total_revenue)  # Ensure integer value
    
    # Calculate average order value
    avg_order_value = 0
    if completed_orders.exists():
        avg_order_value = total_revenue / completed_orders.count()
    
    # Calculate low stock products (less than 10 units)
    low_stock_products = Product.objects.filter(stock__lt=10).count()
    
    stats = {
        'total_users': User.objects.count(),
        'total_customers': User.objects.filter(role='customer').count(),
        'total_authors': User.objects.filter(role='author').count(),
        'total_admins': User.objects.filter(role='admin').count(),
        'total_orders': all_orders.count(),
        'pending_orders': pending_orders.count(),
        'confirmed_orders': all_orders.filter(status='paid').count(),
        'completed_orders': completed_orders.count(),
        'total_products': Product.objects.count(),
        'total_revenue': total_revenue,
        'avg_order_value': round(avg_order_value, 2),
        'low_stock_products': low_stock_products,
    }
    
    return Response(stats)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAdminUser])
def admin_order_detail(request, pk):
    """Get order details or update order status (admin only)"""
    from orders.models import Order
    from orders.serializers import OrderSerializer
    
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Admin can update order status
        new_status = request.data.get('status')
        if new_status and new_status in ['Pending', 'Confirmed', 'Completed', 'Cancelled']:
            order.status = new_status
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_theme(request):
    """Update user theme preference"""
    serializer = UserThemeSerializer(request.user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Theme updated successfully',
            'theme': request.user.theme
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_theme(request):
    """Get user theme preference"""
    return Response({
        'theme': request.user.theme,
        'available_themes': [
            {'value': 'light', 'label': 'Light Theme'},
            {'value': 'dark', 'label': 'Dark Theme'},
            {'value': 'system', 'label': 'System Theme'}
        ]
    })

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def vendor_list(request):
    """Get list of vendors for admin management"""
    vendors = User.objects.filter(role='vendor')
    serializer = UserProfileSerializer(vendors, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def approve_vendor(request, pk):
    """Approve or reject vendor registration"""
    try:
        vendor = User.objects.get(pk=pk, role='vendor')
    except User.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    is_approved = request.data.get('is_approved', True)
    vendor.is_vendor_approved = is_approved
    vendor.is_active = is_approved
    vendor.save()
    
    return Response({
        'message': f'Vendor {"approved" if is_approved else "rejected"} successfully',
        'vendor': UserProfileSerializer(vendor).data
    })

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def toggle_vendor_status(request, pk):
    """Activate or deactivate vendor"""
    try:
        vendor = User.objects.get(pk=pk, role='vendor')
    except User.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    vendor.is_active = not vendor.is_active
    vendor.save()
    
    return Response({
        'message': f'Vendor {"activated" if vendor.is_active else "deactivated"} successfully',
        'vendor': UserProfileSerializer(vendor).data
    })

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def vendor_products(request, pk):
    """Get products for a specific vendor"""
    try:
        vendor = User.objects.get(pk=pk, role='vendor')
    except User.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    from products.models import Product
    from products.serializers import ProductSerializer
    
    products = Product.objects.filter(vendor=vendor)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def approve_product(request, pk):
    """Approve or reject vendor product"""
    from products.models import Product
    from products.serializers import ProductSerializer
    
    try:
        product = Product.objects.get(pk=pk)
        if not product.vendor:
            return Response({'error': 'Product is not from a vendor'}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    is_approved = request.data.get('is_approved', True)
    product.is_approved = is_approved
    product.save()
    
    return Response({
        'message': f'Product {"approved" if is_approved else "rejected"} successfully',
        'product': ProductSerializer(product).data
    })

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def admin_dashboard_stats(request):
    """Get admin dashboard statistics with vendor data"""
    from orders.models import Order
    from products.models import Product
    
    # Calculate order statistics
    all_orders = Order.objects.all()
    completed_orders = all_orders.filter(status='delivered')
    pending_orders = all_orders.filter(status='pending')
    
    # Calculate revenue
    total_revenue = sum(float(order.total_amount) for order in completed_orders)
    total_revenue = round(total_revenue)  # Ensure integer value
    
    # Calculate average order value
    avg_order_value = 0
    if completed_orders.exists():
        avg_order_value = total_revenue / completed_orders.count()
    
    # Calculate low stock products (less than 10 units)
    low_stock_products = Product.objects.filter(stock__lt=10).count()
    
    # Vendor statistics
    total_vendors = User.objects.filter(role='vendor').count()
    active_vendors = User.objects.filter(role='vendor', is_active=True).count()
    pending_vendors = User.objects.filter(role='vendor', is_vendor_approved=False).count()
    vendor_products = Product.objects.filter(vendor__isnull=False).count()
    pending_products = Product.objects.filter(vendor__isnull=False, is_approved=False).count()
    
    stats = {
        'total_users': User.objects.count(),
        'total_customers': User.objects.filter(role='customer').count(),
        'total_vendors': total_vendors,
        'total_admins': User.objects.filter(role='admin').count(),
        'active_vendors': active_vendors,
        'pending_vendors': pending_vendors,
        'vendor_products': vendor_products,
        'pending_products': pending_products,
        'total_orders': all_orders.count(),
        'pending_orders': pending_orders.count(),
        'confirmed_orders': all_orders.filter(status='paid').count(),
        'completed_orders': completed_orders.count(),
        'total_products': Product.objects.count(),
        'total_revenue': total_revenue,
        'avg_order_value': round(avg_order_value, 2),
        'low_stock_products': low_stock_products,
    }
    
    return Response(stats)
