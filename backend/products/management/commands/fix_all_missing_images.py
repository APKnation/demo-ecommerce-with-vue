from django.core.management.base import BaseCommand
import os
import random
from django.conf import settings
from products.models import Product

class Command(BaseCommand):
    help = 'Fix all missing product images by assigning existing ones'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== FIXING ALL MISSING PRODUCT IMAGES ==='))
        
        media_products_path = os.path.join(settings.MEDIA_ROOT, 'products')
        
        # Get all existing images in media folder
        existing_images = []
        if os.path.exists(media_products_path):
            for file in os.listdir(media_products_path):
                if file.endswith(('.jpg', '.jpeg', '.png', '.webp')):
                    existing_images.append(f'products/{file}')
        
        self.stdout.write(self.style.SUCCESS(f'Found {len(existing_images)} existing images'))
        
        # Get all products
        all_products = Product.objects.all()
        missing_images = []
        
        for product in all_products:
            if not product.image or product.image == '':
                missing_images.append(product)
            elif product.image and not os.path.exists(os.path.join(settings.MEDIA_ROOT, str(product.image))):
                missing_images.append(product)
        
        self.stdout.write(self.style.WARNING(f'Found {len(missing_images)} products with missing images'))
        
        # Assign existing images to products with missing images
        for product in missing_images:
            if existing_images:
                # Select a random existing image
                selected_image = random.choice(existing_images)
                product.image = selected_image
                product.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Fixed {product.title}: {product.image}'))
            else:
                self.stdout.write(self.style.ERROR(f'❌ No existing images available for {product.title}'))
        
        self.stdout.write(self.style.SUCCESS('\\n=== ALL PRODUCT IMAGES FIXED ==='))
