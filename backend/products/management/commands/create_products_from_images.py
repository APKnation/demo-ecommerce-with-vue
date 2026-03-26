from django.core.management.base import BaseCommand
from django.conf import settings
from products.models import Product, Category
from accounts.models import User
import os
import random

class Command(BaseCommand):
    help = 'Create products from images in the images folder'

    def handle(self, *args, **options):
        # Image to category mapping
        image_category_mapping = {
            # Laptops
            'Computer.jpeg': 'laptops',
            'k.jpg': 'laptops',
            'laptop-placeholder.jpg': 'laptops',
            
            # Phones
            'iPhone-16-Pro-max-300x300.jpg': 'phones',
            'iPhone.jpg': 'phones',
            'phone-placeholder.jpg': 'phones',
            'IMG-20240518-WA0000.jpg': 'phones',
            'IMG-20240518-WA0001.jpg': 'phones',
            'IMG-20240518-WA0002.jpg': 'phones',
            'IMG-20240518-WA0004.jpg': 'phones',
            
            # Accessories
            'watch1.jpeg': 'accessories',
            'watch3.jpeg': 'accessories',
            'accessory-placeholder.jpg': 'accessories',
            'electronics-placeholder.jpg': 'accessories',
            'Shirt2.jpeg': 'accessories',
            
            # Generic images (will be distributed)
            'a.jpg': None,
            'b.jpg': None,
            'c.jpg': None,
            'd.jpg': None,
            'e.jpg': None,
            'f.jpg': None,
            'g.jpg': None,
            'h.jpg': None,
            'i.jpg': None,
            'j.jpg': None,
            'l.jpg': None,
            'm.jpg': None,
            'n.jpg': None,
            'o.jpg': None,
            'p.jpg': None,
            'q.jpg': None,
            'r.jpg': None,
            's.jpg': None,
            't.jpg': None,
            'u.jpg': None,
            'v.jpg': None,
            'w.jpg': None,
        }

        # Product templates for different categories
        product_templates = {
            'laptops': [
                {'name': 'MacBook Pro', 'base_price': 1500000, 'condition': 'new'},
                {'name': 'Dell XPS', 'base_price': 1200000, 'condition': 'new'},
                {'name': 'HP Pavilion', 'base_price': 800000, 'condition': 'new'},
                {'name': 'Lenovo ThinkPad', 'base_price': 900000, 'condition': 'new'},
                {'name': 'Asus ROG', 'base_price': 1100000, 'condition': 'new'},
                {'name': 'Acer Swift', 'base_price': 700000, 'condition': 'new'},
                {'name': 'Microsoft Surface', 'base_price': 1300000, 'condition': 'new'},
                {'name': 'Gaming Laptop Pro', 'base_price': 1600000, 'condition': 'new'},
            ],
            'phones': [
                {'name': 'iPhone 16 Pro', 'base_price': 2500000, 'condition': 'new'},
                {'name': 'Samsung Galaxy S24', 'base_price': 1800000, 'condition': 'new'},
                {'name': 'Google Pixel 8', 'base_price': 1200000, 'condition': 'new'},
                {'name': 'OnePlus 12', 'base_price': 900000, 'condition': 'new'},
                {'name': 'Xiaomi 14', 'base_price': 800000, 'condition': 'new'},
                {'name': 'Oppo Find X7', 'base_price': 1000000, 'condition': 'new'},
                {'name': 'Vivo X100', 'base_price': 850000, 'condition': 'new'},
                {'name': 'Tecno Phantom', 'base_price': 600000, 'condition': 'new'},
            ],
            'accessories': [
                {'name': 'Smart Watch Pro', 'base_price': 300000, 'condition': 'new'},
                {'name': 'Wireless Earbuds', 'base_price': 150000, 'condition': 'new'},
                {'name': 'Phone Case Premium', 'base_price': 50000, 'condition': 'new'},
                {'name': 'Laptop Stand', 'base_price': 80000, 'condition': 'new'},
                {'name': 'USB-C Hub', 'base_price': 120000, 'condition': 'new'},
                {'name': 'Bluetooth Speaker', 'base_price': 200000, 'condition': 'new'},
                {'name': 'Power Bank 20000mAh', 'base_price': 180000, 'condition': 'new'},
                {'name': 'Charging Cable Set', 'base_price': 40000, 'condition': 'new'},
            ]
        }

        # Get or create admin user
        admin_user = User.objects.filter(role='admin').first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found. Please create an admin user first.'))
            return

        # Get categories
        categories = {cat.name: cat for cat in Category.objects.all()}
        
        # Images folder path
        images_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/images'
        
        created_products = 0
        updated_products = 0
        
        for image_filename, category_name in image_category_mapping.items():
            image_path = os.path.join(images_folder, image_filename)
            
            if not os.path.exists(image_path):
                self.stdout.write(self.style.WARNING(f'Image not found: {image_filename}'))
                continue
            
            # Determine category
            if category_name is None:
                # Distribute generic images across categories
                category_name = random.choice(['laptops', 'phones', 'accessories'])
            
            if category_name not in categories:
                self.stdout.write(self.style.WARNING(f'Category not found: {category_name}'))
                continue
            
            category = categories[category_name]
            
            # Get a random template for this category
            template = random.choice(product_templates[category_name])
            
            # Add some variation to price and name
            price_variation = random.uniform(0.8, 1.3)  # ±30% variation
            final_price = int(template['base_price'] * price_variation)
            
            # Create unique product name
            product_name = f"{template['name']} - {image_filename.split('.')[0].upper()}"
            
            # Generate description
            descriptions = {
                'laptops': [
                    "High-performance laptop with powerful processor and stunning display. Perfect for work and entertainment.",
                    "Sleek and lightweight design with long battery life. Ideal for professionals and students.",
                    "Gaming powerhouse with dedicated graphics and cooling system. Built for serious gamers.",
                    "Business laptop with enhanced security features and professional design.",
                ],
                'phones': [
                    "Latest smartphone with advanced camera system and 5G connectivity. Capture life's moments in stunning detail.",
                    "Powerful performance with flagship processor and beautiful AMOLED display.",
                    "Budget-friendly smartphone with great features and excellent battery life.",
                    "Premium design with water resistance and wireless charging capabilities.",
                ],
                'accessories': [
                    "High-quality accessory with premium materials and excellent build quality.",
                    "Essential gadget for modern lifestyle with smart features and connectivity.",
                    "Stylish and functional accessory that complements your devices perfectly.",
                    "Innovative design with advanced technology and user-friendly interface.",
                ]
            }
            
            description = random.choice(descriptions[category_name])
            
            # Check if product already exists
            existing_product = Product.objects.filter(title=product_name).first()
            
            if existing_product:
                # Update existing product
                existing_product.description = description
                existing_product.price = final_price
                existing_product.category = category
                existing_product.condition = template['condition']
                existing_product.stock = random.randint(5, 50)
                existing_product.featured = random.choice([True, False])
                existing_product.theme_order = random.randint(1, 100)
                existing_product.save()
                updated_products += 1
                self.stdout.write(self.style.SUCCESS(f'Updated product: {product_name}'))
            else:
                # Create new product
                product = Product.objects.create(
                    title=product_name,
                    description=description,
                    price=final_price,
                    category=category,
                    condition=template['condition'],
                    author=admin_user,
                    image=f'images/{image_filename}',  # Store relative path
                    stock=random.randint(5, 50),
                    is_active=True,
                    is_approved=True,
                    featured=random.choice([True, False]),
                    theme_order=random.randint(1, 100),
                )
                created_products += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {product_name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSummary:'))
        self.stdout.write(self.style.SUCCESS(f'Created products: {created_products}'))
        self.stdout.write(self.style.SUCCESS(f'Updated products: {updated_products}'))
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {Product.objects.count()}'))
        
        # Show category breakdown
        self.stdout.write(self.style.SUCCESS(f'\nProducts by category:'))
        for category_name, category in categories.items():
            count = Product.objects.filter(category=category).count()
            self.stdout.write(self.style.SUCCESS(f'{category_name}: {count} products'))
