from django.core.management.base import BaseCommand
from products.models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample products for testing'

    def handle(self, *args, **options):
        # Clear existing products and categories
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create or get admin user for products
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Created admin user: {admin_user.username}')
            )
        
        # Create categories
        categories = {
            'laptops': 'Laptops and notebook computers',
            'phones': 'Smartphones and mobile devices',
            'accessories': 'Electronic accessories and peripherals'
        }
        
        created_categories = {}
        for name, description in categories.items():
            category = Category.objects.create(name=name, description=description)
            created_categories[name] = category
            self.stdout.write(
                self.style.SUCCESS(f'Created category: {category.name} (ID: {category.id})')
            )
        
        # Create sample products
        products = [
            {
                'title': 'Mac Book',
                'price': 1000000,
                'description': 'High-performance laptop for professionals',
                'condition': 'new',
                'category': created_categories['laptops'],
                'author': admin_user,
                'stock': 10,
                'is_active': True
            },
            {
                'title': 'HP-Brand',
                'price': 150000,
                'description': 'Reliable laptop for everyday use',
                'condition': 'new',
                'category': created_categories['laptops'],
                'author': admin_user,
                'stock': 15,
                'is_active': True
            },
            {
                'title': 'Dell',
                'price': 200000,
                'description': 'Business laptop with great performance',
                'condition': 'new',
                'category': created_categories['laptops'],
                'author': admin_user,
                'stock': 8,
                'is_active': True
            },
            {
                'title': 'Apple iPhone',
                'price': 1000000,
                'description': 'Latest smartphone with advanced features',
                'condition': 'new',
                'category': created_categories['phones'],
                'author': admin_user,
                'stock': 20,
                'is_active': True
            },
            {
                'title': 'HP-Elite',
                'price': 1500000,
                'description': 'Premium laptop for power users',
                'condition': 'new',
                'category': created_categories['laptops'],
                'author': admin_user,
                'stock': 5,
                'is_active': True
            },
            {
                'title': 'Sony Headphones',
                'price': 200000,
                'description': 'High-quality wireless headphones',
                'condition': 'new',
                'category': created_categories['accessories'],
                'author': admin_user,
                'stock': 25,
                'is_active': True
            },
            {
                'title': 'Infinix Smartphone',
                'price': 400000,
                'description': 'Budget-friendly smartphone with good features',
                'condition': 'new',
                'category': created_categories['phones'],
                'author': admin_user,
                'stock': 30,
                'is_active': True
            },
            {
                'title': 'iPhone Pro',
                'price': 1500000,
                'description': 'Professional smartphone with advanced camera',
                'condition': 'new',
                'category': created_categories['phones'],
                'author': admin_user,
                'stock': 12,
                'is_active': True
            },
            {
                'title': 'Samsung Galaxy',
                'price': 3000000,
                'description': 'Flagship smartphone with premium features',
                'condition': 'new',
                'category': created_categories['phones'],
                'author': admin_user,
                'stock': 7,
                'is_active': True
            }
        ]
        
        created_count = 0
        for product_data in products:
            product = Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Created product: {product.title} (ID: {product.id})')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} products!')
        )
