from django.core.management.base import BaseCommand
from products.models import Product, Category
from accounts.models import User
import os
import random

class Command(BaseCommand):
    help = 'Force register ALL images in folder as products - one product per image'

    def handle(self, *args, **options):
        # Get ALL images in the folder
        images_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/images'
        all_images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        self.stdout.write(self.style.WARNING('=== FORCE REGISTER ALL IMAGES ==='))
        self.stdout.write(self.style.SUCCESS(f'Total images found: {len(all_images)}'))
        
        # Get admin user
        admin_user = User.objects.filter(role='admin').first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found!'))
            return
        
        # Get categories
        categories = {cat.name: cat for cat in Category.objects.all()}
        
        # Delete all existing products to start fresh
        existing_count = Product.objects.count()
        if existing_count > 0:
            confirm = input(f'\\nFound {existing_count} existing products. Delete all and recreate? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.ERROR('Operation cancelled.'))
                return
            
            Product.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted {existing_count} existing products'))
        
        # Product templates for different categories
        product_templates = {
            'laptops': [
                {'name': 'Gaming Laptop Pro', 'base_price': 1500000},
                {'name': 'Business Laptop', 'base_price': 1200000},
                {'name': 'Student Laptop', 'base_price': 800000},
                {'name': 'UltraBook Pro', 'base_price': 1100000},
                {'name': 'Premium Laptop', 'base_price': 1800000},
                {'name': 'Workstation Laptop', 'base_price': 2000000},
                {'name': 'Slim Laptop', 'base_price': 900000},
                {'name': 'Power Laptop', 'base_price': 1600000},
            ],
            'phones': [
                {'name': 'Smartphone Pro', 'base_price': 800000},
                {'name': 'Flagship Phone', 'base_price': 1200000},
                {'name': 'Budget Phone', 'base_price': 400000},
                {'name': 'Camera Phone', 'base_price': 600000},
                {'name': '5G Phone', 'base_price': 900000},
                {'name': 'Premium Phone', 'base_price': 1500000},
                {'name': 'Compact Phone', 'base_price': 500000},
                {'name': 'Gaming Phone', 'base_price': 1000000},
                {'name': 'Business Phone', 'base_price': 1100000},
                {'name': 'Camera Pro Phone', 'base_price': 1300000},
                {'name': 'Ultra Phone', 'base_price': 1700000},
                {'name': 'Smart Basic Phone', 'base_price': 350000},
                {'name': 'Pro Max Phone', 'base_price': 1400000},
                {'name': 'Mini Phone', 'base_price': 300000},
                {'name': 'Elite Phone', 'base_price': 1900000},
            ],
            'accessories': [
                {'name': 'Premium Accessory', 'base_price': 150000},
                {'name': 'Tech Gadget', 'base_price': 200000},
                {'name': 'Electronic Device', 'base_price': 180000},
                {'name': 'Smart Device', 'base_price': 250000},
                {'name': 'Digital Accessory', 'base_price': 120000},
                {'name': 'Wireless Gadget', 'base_price': 300000},
                {'name': 'Portable Device', 'base_price': 220000},
                {'name': 'Smart Watch', 'base_price': 350000},
                {'name': 'Phone Case', 'base_price': 80000},
                {'name': 'Charging Cable', 'base_price': 50000},
                {'name': 'Power Bank', 'base_price': 180000},
                {'name': 'Bluetooth Speaker', 'base_price': 280000},
                {'name': 'USB Hub', 'base_price': 160000},
                {'name': 'Laptop Stand', 'base_price': 140000},
                {'name': 'Screen Protector', 'base_price': 60000},
                {'name': 'Wireless Earbuds', 'base_price': 320000},
            ]
        }
        
        # Create products for ALL images
        created_count = 0
        category_distribution = {'laptops': 0, 'phones': 0, 'accessories': 0}
        
        for i, image_filename in enumerate(all_images):
            # Distribute images evenly across categories
            category_names = list(categories.keys())
            category_name = category_names[i % len(category_names)]
            category = categories[category_name]
            category_distribution[category_name] += 1
            
            # Get template for this category
            templates = product_templates[category_name]
            template = templates[hash(image_filename) % len(templates)]
            
            # Create unique product name
            base_name = image_filename.split('.')[0].upper()
            product_name = f"{template['name']} - {base_name}"
            
            # Add price variation
            price_variation = random.uniform(0.7, 1.5)
            final_price = int(template['base_price'] * price_variation)
            
            # Create product
            product = Product.objects.create(
                title=product_name,
                description=f"High-quality {category_name[:-1]} with excellent features and modern design. Perfect for everyday use. This is the {base_name} model with unique specifications.",
                price=final_price,
                category=category,
                condition='new',
                author=admin_user,
                image=f'products/{image_filename}',
                stock=random.randint(5, 50),
                is_active=True,
                is_approved=True,
                featured=random.choice([True, False]),
                theme_order=random.randint(1, 100),
            )
            
            created_count += 1
            if created_count % 10 == 0:
                self.stdout.write(self.style.SUCCESS(f'Created {created_count} products...'))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Total products created: {created_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total images registered: {len(all_images)}'))
        
        # Show category breakdown
        self.stdout.write(self.style.SUCCESS('\\n=== CATEGORY BREAKDOWN ==='))
        for category_name, count in category_distribution.items():
            self.stdout.write(self.style.SUCCESS(f'{category_name}: {count} products'))
        
        # Verify one-to-one mapping
        self.stdout.write(self.style.SUCCESS('\\n=== VERIFICATION ==='))
        image_usage = {}
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                image_usage[filename] = product.title
        
        if len(image_usage) == len(all_images):
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: Each image has exactly one product!'))
        else:
            self.stdout.write(self.style.ERROR(f'❌ MISMATCH: {len(image_usage)} products vs {len(all_images)} images'))
        
        # Show sample products
        self.stdout.write(self.style.SUCCESS('\\n=== SAMPLE PRODUCTS ==='))
        sample_products = Product.objects.all()[:5]
        for product in sample_products:
            filename = product.image.name.split('/')[-1] if product.image.name else 'None'
            self.stdout.write(self.style.SUCCESS(f'  {product.title} -> {filename}'))
