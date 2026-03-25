from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart-detail'),
    path('cart/add/', views.add_to_cart, name='add-to-cart'),
    path('cart/items/<int:pk>/', views.cart_item_manage, name='cart-item-manage'),
    path('create/', views.create_order, name='create-order'),
    path('', views.order_list, name='order-list'),
    path('<int:pk>/', views.order_detail, name='order-detail'),
    path('admin/all/', views.all_orders, name='all-orders'),
    path('admin/<int:pk>/status/', views.update_order_status, name='update-order-status'),
    # New order management endpoints
    path('<int:pk>/update-status/', views.update_order_status_user, name='update-order-status-user'),
    path('<int:pk>/cancel/', views.cancel_order, name='cancel-order'),
    path('<int:pk>/mark-paid/', views.mark_order_paid, name='mark-order-paid'),
    path('<int:pk>/mark-shipped/', views.mark_order_shipped, name='mark-order-shipped'),
    path('<int:pk>/mark-delivered/', views.mark_order_delivered, name='mark-order-delivered'),
]
