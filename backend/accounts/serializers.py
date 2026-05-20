from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    phone = serializers.CharField(required=True)  # Make phone required
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='customer')
    theme = serializers.ChoiceField(choices=User.THEME_CHOICES, default='system')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name', 'phone', 'address', 'role', 'theme']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        
        # Validate vendor registration
        if attrs.get('role') == 'vendor':
            # Additional validation for vendors if needed
            pass
            
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        # Set default theme if not provided
        if 'theme' not in validated_data:
            validated_data['theme'] = 'system'
        
        # Set vendor approval status
        if validated_data.get('role') == 'vendor':
            validated_data['is_vendor_approved'] = False
        
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField()
    
    def validate(self, attrs):
        password = attrs.get('password')
        user = None
        
        # Try to authenticate with phone number first
        if attrs.get('phone'):
            phone = attrs.get('phone')
            try:
                user_obj = User.objects.get(phone=phone)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid phone number or password')
        
        # Try to authenticate with username
        elif attrs.get('username'):
            username = attrs.get('username')
            user = authenticate(username=username, password=password)
        
        # Try to authenticate with email
        elif attrs.get('email'):
            email = attrs.get('email')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid email or password')
        
        else:
            raise serializers.ValidationError('Must include phone, username, or email and password')
        
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')
        
        # Check vendor approval
        if user.role == 'vendor' and not user.is_vendor_approved:
            raise serializers.ValidationError('Vendor account is not yet approved by admin')
        
        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone', 
            'address', 'role', 'theme', 'is_active', 'is_vendor_approved', 'is_staff',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'is_vendor_approved']

class UserThemeSerializer(serializers.ModelSerializer):
    """Serializer for updating user theme preferences"""
    class Meta:
        model = User
        fields = ['theme']
        
    def update(self, instance, validated_data):
        instance.theme = validated_data.get('theme', instance.theme)
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    """Extended user profile serializer with theme info"""
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone', 
            'address', 'role', 'theme', 'is_active', 'is_vendor_approved', 'is_staff',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'is_vendor_approved']
