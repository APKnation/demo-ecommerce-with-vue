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
        images_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/images'
        all_images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        # Find products using placeholder images
        products_with_placeholders = []
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                if filename in placeholder_images:
                    products_with_placeholders.append((product, filename))
        
        self.stdout.write(self.style.WARNING('=== PLACEHOLDER IMAGE ANALYSIS ==='))
        self.stdout.write(self.style.WARNING(f'Found {len(products_with_placeholders)} products using placeholder images'))
        
        if not products_with_placeholders:
            self.stdout.write(self.style.SUCCESS('No products using placeholder images found!'))
            return
        
        for product, placeholder_name in products_with_placeholders:
            self.stdout.write(self.style.WARNING(f'  - {product.title} -> {placeholder_name}'))
        
        # Get available unique images (not placeholders and not already used)
        used_images = set()
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                used_images.add(filename)
        
        available_images = [img for img in all_images 
                          if img not in placeholder_images 
                          and img not in used_images]
        
        self.stdout.write(self.style.SUCCESS(f'\\nAvailable unique images: {len(available_images)}'))
        
        if len(available_images) < len(products_with_placeholders):
            self.stdout.write(self.style.ERROR(f'Not enough unique images! Need {len(products_with_placeholders)}, have {len(available_images)}'))
            return
        
        # Confirm the change
        confirm = input('\\nDo you want to replace placeholder images with unique images? (yes/no): ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return
        
        # Shuffle available images for random assignment
        random.shuffle(available_images)
        
        updated_count = 0
        for (product, placeholder_name), new_image in zip(products_with_placeholders, available_images):
            old_image = product.image.name
            product.image.name = f'products/{new_image}'
            product.save()
            updated_count += 1
            
            self.stdout.write(self.style.SUCCESS(f'Updated: {product.title}'))
            self.stdout.write(self.style.SUCCESS(f'  OLD: {old_image}'))
            self.stdout.write(self.style.SUCCESS(f'  NEW: products/{new_image}'))
            self.stdout.write('')
        
        self.stdout.write(self.style.SUCCESS(f'=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Updated {updated_count} products with unique images'))
        self.stdout.write(self.style.SUCCESS(f'Products still using placeholders: {len([p for p, _ in products_with_placeholders]) - updated_count}'))
        
        # Verify no more placeholder conflicts
        remaining_placeholders = 0
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                if filename in placeholder_images:
                    remaining_placeholders += 1
        
        if remaining_placeholders == 0:
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: No more products using placeholder images!'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️  Still {remaining_placeholders} products using placeholder images'))
