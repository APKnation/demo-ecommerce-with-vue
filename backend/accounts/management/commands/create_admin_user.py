from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a new admin user'

    def handle(self, *args, **options):
        # Check if admin already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(
                self.style.WARNING('Admin user already exists. Removing existing admin...')
            )
            User.objects.filter(username='admin').delete()
        
        # Create new admin user
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@kafuka.com',
            password='admin123',
            role='admin',
            first_name='Admin',
            last_name='User'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Admin user "{admin_user.username}" created successfully!')
        )
        self.stdout.write(f'Username: {admin_user.username}')
        self.stdout.write(f'Email: {admin_user.email}')
        self.stdout.write(f'Password: admin123')
        self.stdout.write(f'Role: {admin_user.role}')
        self.stdout.write(f'Is Staff: {admin_user.is_staff}')
        self.stdout.write(f'Is Superuser: {admin_user.is_superuser}')
