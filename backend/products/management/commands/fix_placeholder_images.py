from django.core.management.base import BaseCommand
from products.models import Product
import os
import random

class Command(BaseCommand):
    help = 'Fix products using placeholder images by assigning unique images'

    def handle(self, *args, **options):
        # Identify placeholder images
        placeholder_images = [
            'phone-placeholder.jpg',
            'laptop-placeholder.jpg', 
            'accessory-placeholder.jpg',
            'placeholder.jpg',
            'electronics-placeholder.jpg'
        ]
        
        # Get all available images
        media_path = 'media/products'
        available_images = []
        
        if os.path.exists(media_path):
            for file in os.listdir(media_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    available_images.append(file)
        
        # Find products using placeholder images
        products_with_placeholders = []
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                if filename in placeholder_images:
                    products_with_placeholders.append((product, filename))
        
        self.stdout.write(self.style.WARNING(f'Found {len(products_with_placeholders)} products using placeholder images'))
        
        if not products_with_placeholders:
            self.stdout.write(self.style.SUCCESS('No products using placeholder images found!'))
            return
        
        # Get available unique images (not placeholders and not already used)
        used_images = set()
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                used_images.add(filename)
        
        available_images = [img for img in available_images 
                          if img not in placeholder_images 
                          and img not in used_images]
        
        self.stdout.write(self.style.SUCCESS(f'Available unique images: {len(available_images)}'))
        
        if len(available_images) < len(products_with_placeholders):
            self.stdout.write(self.style.ERROR(f'Not enough unique images! Need {len(products_with_placeholders)}, have {len(available_images)}'))
            return
        
        # Shuffle available images for random assignment
        random.shuffle(available_images)
        
        # Assign unique images to placeholder products
        updated_count = 0
        for (product, placeholder_name), new_image in zip(products_with_placeholders, available_images):
            old_image = product.image.name
            product.image.name = f'products/{new_image}'
            product.save()
            
            updated_count += 1
            
            self.stdout.write(self.style.SUCCESS(f'Fixed: {product.title}'))
            self.stdout.write(self.style.SUCCESS(f'  OLD: {old_image}'))
            self.stdout.write(self.style.SUCCESS(f'  NEW: products/{new_image}'))
            self.stdout.write('')
        
        self.stdout.write(self.style.SUCCESS(f'\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products updated: {updated_count}'))
        self.stdout.write(self.style.SUCCESS(f'Products still using placeholders: {len(products_with_placeholders) - updated_count}'))
        
        # Verify no more placeholder conflicts
        remaining_placeholders = 0
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                if filename in placeholder_images:
                    remaining_placeholders += 1
        
        if remaining_placeholders == 0:
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: All placeholder images replaced with unique images!'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️  Still {remaining_placeholders} products using placeholder images'))
