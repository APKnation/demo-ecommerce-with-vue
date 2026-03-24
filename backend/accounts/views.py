from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer

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
    
    stats = {
        'total_users': User.objects.count(),
        'total_customers': User.objects.filter(role='customer').count(),
        'total_authors': User.objects.filter(role='author').count(),
        'total_admins': User.objects.filter(role='admin').count(),
        'total_orders': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='Pending').count(),
        'confirmed_orders': Order.objects.filter(status='Confirmed').count(),
        'completed_orders': Order.objects.filter(status='Completed').count(),
        'total_products': Product.objects.count(),
        'total_revenue': sum(float(order.total_amount) for order in Order.objects.filter(status__in=['Confirmed', 'Completed'])),
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
