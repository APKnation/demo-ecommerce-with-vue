from django.db import models
from django.conf import settings

class Theme(models.Model):
    """Global theme settings for the application"""
    THEME_CHOICES = [
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
        ('auto', 'Auto (System Preference)'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    theme_type = models.CharField(max_length=10, choices=THEME_CHOICES, default='light')
    is_active = models.BooleanField(default=True)
    
    # Theme colors
    primary_color = models.CharField(max_length=7, default='#3B82F6', help_text="Primary color in hex format")
    secondary_color = models.CharField(max_length=7, default='#10B981', help_text="Secondary color in hex format")
    accent_color = models.CharField(max_length=7, default='#F59E0B', help_text="Accent color in hex format")
    background_color = models.CharField(max_length=7, default='#FFFFFF', help_text="Background color in hex format")
    text_color = models.CharField(max_length=7, default='#1F2937', help_text="Text color in hex format")
    
    # Theme settings
    custom_css = models.TextField(blank=True, help_text="Custom CSS for theme")
    custom_js = models.TextField(blank=True, help_text="Custom JavaScript for theme")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_active', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.theme_type})"

class UserThemePreference(models.Model):
    """User-specific theme preferences"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='theme_preference')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)
    custom_settings = models.JSONField(default=dict, blank=True, help_text="User-specific theme settings")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s theme preference"

class FeaturedProduct(models.Model):
    """Products featured in theme display"""
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='featured_products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='theme_features')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        unique_together = ['theme', 'product']
    
    def __str__(self):
        return f"{self.product.title} in {self.theme.name}"

class ThemeSetting(models.Model):
    """Global theme settings"""
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False, help_text="Whether this setting is public (accessible via API)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['key']
    
    def __str__(self):
        return f"{self.key}: {self.value[:50]}..."
