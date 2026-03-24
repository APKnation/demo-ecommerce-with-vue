from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users_list, name='users-list'),
    path('admin/users/<int:pk>/', views.admin_user_detail, name='admin-user-detail'),
    path('admin/users/<int:pk>/update/', views.admin_update_user, name='admin-update-user'),
    path('admin/dashboard-stats/', views.admin_dashboard_stats, name='admin-dashboard-stats'),
    path('admin/orders/<int:pk>/', views.admin_order_detail, name='admin-order-detail'),
]
