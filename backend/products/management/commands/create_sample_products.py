from django.core.management.base import BaseCommand
from products.models import Product, Category
from django.contrib.auth import get_user_model
import requests
from django.core.files.base import ContentFile

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample products with real images'

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
            'Laptops': 'Laptops and notebook computers',
            'Phones': 'Smartphones and mobile devices',
            'Accessories': 'Electronic accessories and peripherals',
            'Electronics': 'Electronic devices and gadgets'
        }
        
        created_categories = {}
        for name, description in categories.items():
            category = Category.objects.create(name=name, description=description)
            created_categories[name] = category
            self.stdout.write(
                self.style.SUCCESS(f'Created category: {category.name} (ID: {category.id})')
            )
        
        # Create sample products with real images
        products = [
            {
                'title': 'MacBook Pro 14"',
                'price': 2500000,
                'description': 'Apple MacBook Pro with M2 Pro chip, 16GB RAM, 512GB SSD. Perfect for professionals and creators.',
                'condition': 'new',
                'category': created_categories['Laptops'],
                'author': admin_user,
                'stock': 5,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=600&fit=crop'
            },
            {
                'title': 'iPhone 15 Pro',
                'price': 1800000,
                'description': 'Latest iPhone with A17 Pro chip, 48MP camera, titanium design. Premium smartphone experience.',
                'condition': 'new',
                'category': created_categories['Phones'],
                'author': admin_user,
                'stock': 8,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1592286115803-a1c3b552ee43?w=800&h=600&fit=crop'
            },
            {
                'title': 'Sony WH-1000XM5',
                'price': 450000,
                'description': 'Premium noise-cancelling headphones with 30-hour battery life, superior sound quality.',
                'condition': 'new',
                'category': created_categories['Accessories'],
                'author': admin_user,
                'stock': 15,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=600&fit=crop'
            },
            {
                'title': 'Dell XPS 15',
                'price': 2200000,
                'description': 'High-performance laptop with Intel Core i7, 32GB RAM, 1TB SSD, 4K display. Excellent for creative work.',
                'condition': 'new',
                'category': created_categories['Laptops'],
                'author': admin_user,
                'stock': 3,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=600&fit=crop'
            },
            {
                'title': 'Samsung Galaxy S24 Ultra',
                'price': 1600000,
                'description': 'Flagship Android phone with S Pen, 200MP camera, Snapdragon 8 Gen 3. Ultimate smartphone.',
                'condition': 'new',
                'category': created_categories['Phones'],
                'author': admin_user,
                'stock': 6,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1592286115803-a1c3b552ee43?w=800&h=600&fit=crop'
            },
            {
                'title': 'Logitech MX Master 3S',
                'price': 180000,
                'description': 'Advanced wireless mouse with precision scrolling, ergonomic design, multi-device connectivity.',
                'condition': 'new',
                'category': created_categories['Accessories'],
                'author': admin_user,
                'stock': 20,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800&h=600&fit=crop'
            },
            {
                'title': 'iPad Air',
                'price': 900000,
                'description': 'Apple iPad Air with M1 chip, 10.9-inch display, 64GB storage. Perfect tablet for work and entertainment.',
                'condition': 'new',
                'category': created_categories['Electronics'],
                'author': admin_user,
                'stock': 10,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=600&fit=crop'
            },
            {
                'title': 'AirPods Pro 2',
                'price': 350000,
                'description': 'Apple wireless earbuds with active noise cancellation, spatial audio, 6-hour battery life.',
                'condition': 'new',
                'category': created_categories['Accessories'],
                'author': admin_user,
                'stock': 25,
                'is_active': True,
                'image_url': 'https://images.unsplash.com/photo-1606236517996-35c9ac89b5e0?w=800&h=600&fit=crop'
            }
        ]
        
        created_count = 0
        for product_data in products:
            try:
                # Download image
                image_url = product_data.pop('image_url', None)
                image_content = None
                
                if image_url:
                    response = requests.get(image_url, timeout=30)
                    if response.status_code == 200:
                        image_name = f"{product_data['title'].lower().replace(' ', '_').replace('/', '_')}.jpg"
                        image_content = ContentFile(response.content, name=image_name)
                        self.stdout.write(f'Downloaded image for {product_data["title"]}')
                
                # Create product
                product = Product.objects.create(**product_data, image=image_content)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product.title} (ID: {product.id})')
                )
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating product {product_data["title"]}: {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} products with real images!')
        )
