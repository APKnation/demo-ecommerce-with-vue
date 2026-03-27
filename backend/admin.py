# Django Admin Configuration for KAFUKA Electronics Store

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Product, Category, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'condition', 'created_at')
    search_fields = ('title', 'description', 'category__name')
    list_editable = ('price', 'stock', 'is_active')
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
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',),
        }),
        ('Status', {
            'fields': ('is_active', 'is_approved'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    def get_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "No Image"
    
    get_image.short_description = 'Product Image'
    list_display = ('title', 'category', 'get_image', 'price', 'stock', 'is_active')
    
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} products marked as active")
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} products marked as inactive")
    
    make_active.short_description = "Mark selected as active"
    make_inactive.short_description = "Mark selected as inactive"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'customer__username', 'customer__email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'customer', 'status'),
            'classes': ('wide',),
        }),
        ('Pricing', {
            'fields': ('total_amount', 'items'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

# Customize Admin Site
admin.site.site_header = "KAFUKA Electronics Store Administration"
admin.site.site_title = "KAFUKA Electronics Admin"
admin.site.index_title = "Welcome to KAFUKA Electronics Store Admin Panel"
