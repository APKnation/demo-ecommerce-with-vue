from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Theme management
    path('theme/', views.get_theme, name='get-theme'),
    path('theme/update/', views.update_theme, name='update-theme'),
    
    # Admin user management
    path('users/', views.users_list, name='users-list'),
    path('admin/users/<int:pk>/', views.admin_user_detail, name='admin-user-detail'),
    path('admin/users/<int:pk>/update/', views.admin_update_user, name='admin-update-user'),
    
    # Vendor management
    path('admin/vendors/', views.vendor_list, name='vendor-list'),
    path('admin/vendors/<int:pk>/approve/', views.approve_vendor, name='approve-vendor'),
    path('admin/vendors/<int:pk>/toggle-status/', views.toggle_vendor_status, name='toggle-vendor-status'),
    path('admin/vendors/<int:pk>/products/', views.vendor_products, name='vendor-products'),
    
    # Product approval
    path('admin/products/<int:pk>/approve/', views.approve_product, name='approve-product'),
    
    # Admin dashboard
    path('admin/dashboard-stats/', views.admin_dashboard_stats, name='admin-dashboard-stats'),
    path('admin/orders/<int:pk>/', views.admin_order_detail, name='admin-order-detail'),
]
