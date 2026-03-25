from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    ]
    
    THEME_CHOICES = [
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
        ('system', 'System Theme'),
    ]
    
    # Phone number validator for international formats
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(
        max_length=20, 
        blank=False, 
        null=False,
        validators=[phone_validator],
        unique=True,  # Make phone numbers unique
        help_text="Enter phone number with country code (e.g., +255123456789)"
    )
    address = models.TextField(blank=True, null=True)
    
    # Theme preferences
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='system')
    is_active = models.BooleanField(default=True)
    is_vendor_approved = models.BooleanField(default=False)  # For vendor approval
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    @property
    def is_vendor(self):
        return self.role == 'vendor'
    
    @property
    def is_admin_user(self):
        return self.role == 'admin'
    
    @property
    def is_customer(self):
        return self.role == 'customer'
