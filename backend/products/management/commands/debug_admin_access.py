from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib import admin

class Command(BaseCommand):
    help = 'Debug admin access and permissions'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== ADMIN ACCESS DEBUG ==='))
        
        # Check admin site configuration
        self.stdout.write(self.style.SUCCESS('Admin Site Configuration:'))
        self.stdout.write(self.style.SUCCESS(f'  Header: {admin.site.site_header}'))
        self.stdout.write(self.style.SUCCESS(f'  Title: {admin.site.site_title}'))
        self.stdout.write(self.style.SUCCESS(f'  Index: {admin.site.index_title}'))
        
        # Check registered models
        self.stdout.write(self.style.SUCCESS('\\nRegistered Admin Models:'))
        for model, model_admin in admin.site._registry.items():
            self.stdout.write(self.style.SUCCESS(f'  ✅ {model.__name__} -> {type(model_admin).__name__}'))
        
        # Check superuser
        User = get_user_model()
        try:
            admin_user = User.objects.get(username='admin')
            self.stdout.write(self.style.SUCCESS('\\nSuperuser Status:'))
            self.stdout.write(self.style.SUCCESS(f'  Username: {admin_user.username}'))
            self.stdout.write(self.style.SUCCESS(f'  Email: {admin_user.email}'))
            self.stdout.write(self.style.SUCCESS(f'  Is Staff: {admin_user.is_staff}'))
            self.stdout.write(self.style.SUCCESS(f'  Is Superuser: {admin_user.is_superuser}'))
            self.stdout.write(self.style.SUCCESS(f'  Is Active: {admin_user.is_active}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('  ❌ Admin user not found!'))
        
        # Test admin URLs
        self.stdout.write(self.style.SUCCESS('\\nAdmin URLs:'))
        for pattern, name in admin.site.get_urls():
            self.stdout.write(self.style.SUCCESS(f'  {pattern}: {name}'))
        
        self.stdout.write(self.style.SUCCESS('\\n=== ADMIN ACCESS INFO ==='))
        self.stdout.write(self.style.SUCCESS('Admin URL: http://localhost:8000/admin/'))
        self.stdout.write(self.style.SUCCESS('Username: admin'))
        self.stdout.write(self.style.SUCCESS('Password: admin123'))
        self.stdout.write(self.style.SUCCESS('If you see issues, clear browser cache and try again.'))
