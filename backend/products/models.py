from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    
    # Updated to support vendor relationship
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='vendor_products',
        help_text="Vendor who owns this product (if applicable)"
    )
    
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=True, help_text="Admin approval required for vendor products")
    
    # Theme-related fields
    featured = models.BooleanField(default=False, help_text="Feature this product in theme display")
    theme_order = models.PositiveIntegerField(default=0, help_text="Order for theme display")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', 'theme_order']
    
    def __str__(self):
        return self.title
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    @property
    def needs_approval(self):
        """Check if product needs admin approval"""
        return self.vendor and not self.is_approved
    
    @property
    def can_be_displayed(self):
        """Check if product can be displayed in frontend"""
        return self.is_active and (not self.needs_approval or self.is_approved)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.product.title}"
