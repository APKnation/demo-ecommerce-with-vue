from django.core.management.base import BaseCommand
import os
import random
from django.conf import settings
from products.models import Product

class Command(BaseCommand):
    help = 'Extract and assign real images to products instead of placeholders'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== EXTRACTING REAL IMAGES FOR PRODUCTS ==='))
        
        media_products_path = os.path.join(settings.MEDIA_ROOT, 'products')
        
        # Get all existing real images (excluding placeholders)
        real_images = []
        if os.path.exists(media_products_path):
            for file in os.listdir(media_products_path):
                if (file.endswith(('.jpg', '.jpeg', '.png', '.webp')) and 
                    not any(placeholder in file.lower() for placeholder in [
                        'default-product.jpg', 'laptop-default.jpg', 'phone-default.jpg', 'accessory-default.jpg'
                    ])):
                    real_images.append(file)
        
        self.stdout.write(self.style.SUCCESS(f'Found {len(real_images)} real images'))
        
        # Find products with placeholder images
        products_with_placeholders = Product.objects.filter(
            image__in=['products/default-product.jpg', 'products/laptop-default.jpg', 'products/phone-default.jpg', 'products/accessory-default.jpg']
        )
        
        self.stdout.write(self.style.WARNING(f'Found {products_with_placeholders.count()} products with placeholder images'))
        
        # Assign real images to products with placeholders
        for product in products_with_placeholders:
            if real_images:
                # Select a random real image
                selected_image = random.choice(real_images)
                product.image = f'products/{selected_image}'
                product.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Updated {product.title}: {product.image}'))
            else:
                self.stdout.write(self.style.ERROR(f'❌ No real images available for {product.title}'))
        
        # Also check for products with no images at all
        products_without_images = Product.objects.filter(image__isnull=True) | Product.objects.filter(image='')
        if products_without_images.exists():
            self.stdout.write(self.style.WARNING(f'Found {products_without_images.count()} products with no images'))
            for product in products_without_images:
                if real_images:
                    selected_image = random.choice(real_images)
                    product.image = f'products/{selected_image}'
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'✅ Updated {product.title}: {product.image}'))
        
        self.stdout.write(self.style.SUCCESS('\\n=== IMAGE EXTRACTION COMPLETE ==='))
