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
]
