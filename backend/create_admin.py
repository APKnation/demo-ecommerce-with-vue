import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electronics_cart_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='apk').exists():
    admin_user = User.objects.create_superuser(
        username='apk',
        email='apk@example.com',
        password='apk',
        role='admin'
    )
    print("Admin user 'apk' created successfully")
else:
    print("Admin user 'apk' already exists")
