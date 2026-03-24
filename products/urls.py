from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('categories/create/', views.category_create, name='category-create'),
    path('', views.product_list, name='product-list'),
    path('<int:pk>/', views.product_detail, name='product-detail'),
    path('create/', views.product_create, name='product-create'),
    path('<int:pk>/manage/', views.product_manage, name='product-manage'),
    path('my-products/', views.my_products, name='my-products'),
]
