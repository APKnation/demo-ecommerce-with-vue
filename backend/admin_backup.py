# Django Admin Configuration for KAFUKA Electronics Store

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from products.models import Product, Category
from orders.models import Order
from accounts.models import User as CustomUser

# Register Custom User from accounts
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone'),
            'classes': ('wide',),
        }),
        ('Role & Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )

# Register Django User (for super admin access)
@admin.register(User)
class DjangoUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    def has_module_permission(self, request):
        return request.user.is_superuser

# Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

# Register Product with full super admin capabilities
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'vendor', 'price', 'stock', 'is_active', 'is_approved', 'created_at')
    list_filter = ('category', 'is_active', 'is_approved', 'condition', 'created_at', 'author', 'vendor')
    search_fields = ('title', 'description', 'category__name', 'author__username', 'vendor__username')
    list_editable = ('price', 'stock', 'is_active', 'is_approved')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category'),
            'classes': ('wide',),
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock', 'condition'),
            'classes': ('collapse',),
        }),
        ('Authors & Vendors', {
            'fields': ('author', 'vendor'),
            'classes': ('collapse',),
        }),
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',),
        }),
        ('Status & Approval', {
            'fields': ('is_active', 'is_approved', 'featured', 'theme_order'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    def get_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;" />'
        return "No Image"
    
    get_image.short_description = 'Product Image'
    get_image.allow_tags = True
    
    def get_author(self, obj):
        return obj.author.username if obj.author else "No Author"
    
    get_author.short_description = 'Author'
    
    def get_vendor(self, obj):
        return obj.vendor.username if obj.vendor else "No Vendor"
    
    get_vendor.short_description = 'Vendor'
    
    actions = ['make_active', 'make_inactive', 'approve_products', 'disapprove_products', 'feature_products', 'unfeature_products']
    
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} products marked as active")
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} products marked as inactive")
    
    def approve_products(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} products approved")
    
    def disapprove_products(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()} products disapproved")
    
    def feature_products(self, request, queryset):
        queryset.update(featured=True)
        self.message_user(request, f"{queryset.count()} products featured")
    
    def unfeature_products(self, request, queryset):
        queryset.update(featured=False)
        self.message_user(request, f"{queryset.count()} products unfeatured")
    
    make_active.short_description = "Mark selected as active"
    make_inactive.short_description = "Mark selected as inactive"
    approve_products.short_description = "Approve selected products"
    disapprove_products.short_description = "Disapprove selected products"
    feature_products.short_description = "Feature selected products"
    unfeature_products.short_description = "Unfeature selected products"
    
    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

# Register Order with full super admin capabilities
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'total_amount', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'customer__username', 'customer__email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'customer', 'status'),
            'classes': ('wide',),
        }),
        ('Pricing & Payment', {
            'fields': ('total_amount', 'payment_method'),
            'classes': ('collapse',),
        }),
        ('Shipping & Notes', {
            'fields': ('shipping_address', 'notes'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    actions = ['mark_pending', 'mark_paid', 'mark_shipped', 'mark_delivered', 'cancel_orders']
    
    def mark_pending(self, request, queryset):
        queryset.update(status='pending')
        self.message_user(request, f"{queryset.count()} orders marked as pending")
    
    def mark_paid(self, request, queryset):
        queryset.update(status='paid')
        self.message_user(request, f"{queryset.count()} orders marked as paid")
    
    def mark_shipped(self, request, queryset):
        queryset.update(status='shipped')
        self.message_user(request, f"{queryset.count()} orders marked as shipped")
    
    def mark_delivered(self, request, queryset):
        queryset.update(status='delivered')
        self.message_user(request, f"{queryset.count()} orders marked as delivered")
    
    def cancel_orders(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, f"{queryset.count()} orders cancelled")
    
    mark_pending.short_description = "Mark as pending"
    mark_paid.short_description = "Mark as paid"
    mark_shipped.short_description = "Mark as shipped"
    mark_delivered.short_description = "Mark as delivered"
    cancel_orders.short_description = "Cancel orders"
    
    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

# Customize Admin Site for Super Admin
admin.site.site_header = "KAFUKA Electronics Store Administration"
admin.site.site_title = "KAFUKA Electronics Admin"
admin.site.index_title = "Welcome to KAFUKA Electronics Store Admin Panel"

# Enable all admin features for super admin
admin.site.enable_nav_sidebar = True
