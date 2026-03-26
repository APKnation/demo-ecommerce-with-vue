from django.core.management.base import BaseCommand
from products.models import Product, Category
from accounts.models import User
import os

class Command(BaseCommand):
    help = 'Create products for ALL remaining images that are not yet used'

    def handle(self, *args, **options):
        # Get all images in the folder
        images_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/images'
        all_images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        # Get images already used by products
        used_images = set()
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                used_images.add(filename)
        
        # Find unused images
        unused_images = [img for img in all_images if img not in used_images]
        
        self.stdout.write(self.style.WARNING('=== IMAGE USAGE ANALYSIS ==='))
        self.stdout.write(self.style.SUCCESS(f'Total images in folder: {len(all_images)}'))
        self.stdout.write(self.style.SUCCESS(f'Images already used: {len(used_images)}'))
        self.stdout.write(self.style.WARNING(f'Unused images: {len(unused_images)}'))
        
        if not unused_images:
            self.stdout.write(self.style.SUCCESS('All images are already used by products!'))
            return
        
        self.stdout.write(self.style.WARNING('\\nUnused images that need products:'))
        for img in sorted(unused_images):
            self.stdout.write(self.style.WARNING(f'  - {img}'))
        
        # Get admin user
        admin_user = User.objects.filter(role='admin').first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found!'))
            return
        
        # Get categories
        categories = {cat.name: cat for cat in Category.objects.all()}
        
        # Product templates for different image types
        product_templates = {
            'laptops': [
                {'name': 'Premium Laptop', 'base_price': 1200000},
                {'name': 'Business Laptop', 'base_price': 900000},
                {'name': 'Gaming Laptop', 'base_price': 1500000},
                {'name': 'Student Laptop', 'base_price': 700000},
                {'name': 'UltraBook', 'base_price': 1100000},
            ],
            'phones': [
                {'name': 'Smartphone Pro', 'base_price': 800000},
                {'name': 'Budget Phone', 'base_price': 400000},
                {'name': 'Flagship Phone', 'base_price': 1200000},
                {'name': 'Camera Phone', 'base_price': 600000},
                {'name': '5G Phone', 'base_price': 900000},
            ],
            'accessories': [
                {'name': 'Premium Accessory', 'base_price': 150000},
                {'name': 'Tech Gadget', 'base_price': 200000},
                {'name': 'Electronic Device', 'base_price': 180000},
                {'name': 'Digital Accessory', 'base_price': 120000},
                {'name': 'Smart Device', 'base_price': 250000},
            ]
        }
        
        confirm = input('\\nDo you want to create products for all unused images? (yes/no): ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return
        
        created_count = 0
        for image_filename in unused_images:
            # Determine category based on filename
            category_name = 'accessories'  # default
            
            filename_lower = image_filename.lower()
            if any(keyword in filename_lower for keyword in ['laptop', 'computer']):
                category_name = 'laptops'
            elif any(keyword in filename_lower for keyword in ['phone', 'iphone']):
                category_name = 'phones'
            elif any(keyword in filename_lower for keyword in ['watch', 'shirt']):
                category_name = 'accessories'
            elif any(keyword in filename_lower for keyword in ['placeholder']):
                category_name = 'accessories'
            elif filename_lower in ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg', 'f.jpg', 'g.jpg', 'h.jpg', 'i.jpg', 'j.jpg', 'k.jpg', 'l.jpg', 'm.jpg', 'n.jpg', 'o.jpg', 'p.jpg', 'q.jpg', 'r.jpg', 's.jpg', 't.jpg', 'u.jpg', 'v.jpg', 'w.jpg']:
                # Distribute single letters evenly
                category_name = ['laptops', 'phones', 'accessories'][hash(image_filename) % 3]
            
            category = categories[category_name]
            
            # Get template for this category
            template = product_templates[category_name][hash(image_filename) % len(product_templates[category_name])]
            
            # Create unique product name
            base_name = image_filename.split('.')[0].upper()
            product_name = f"{template['name']} - {base_name}"
            
            # Add price variation
            import random
            price_variation = random.uniform(0.7, 1.5)
            final_price = int(template['base_price'] * price_variation)
            
            # Create product
            product = Product.objects.create(
                title=product_name,
                description=f"High-quality {category_name[:-1]} with excellent features and modern design. Perfect for everyday use.",
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
            self.stdout.write(self.style.SUCCESS(f'Created: {product_name} ({category_name})'))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} new products'))
        self.stdout.write(self.style.SUCCESS(f'Total products now: {Product.objects.count()}'))
        
        # Show final category breakdown
        self.stdout.write(self.style.SUCCESS('\\n=== FINAL PRODUCT BREAKDOWN ==='))
        for category_name, category in categories.items():
            count = Product.objects.filter(category=category).count()
            self.stdout.write(self.style.SUCCESS(f'{category_name}: {count} products'))
