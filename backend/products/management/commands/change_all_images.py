from django.core.management.base import BaseCommand
from products.models import Product
import os
import random

class Command(BaseCommand):
    help = 'Change all product images to different unique images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== CHANGING ALL PRODUCT IMAGES ==='))
        
        # Get all available images from media/products/
        media_path = 'media/products'
        available_images = []
        
        if os.path.exists(media_path):
            for file in os.listdir(media_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    available_images.append(file)
        
        self.stdout.write(self.style.SUCCESS(f'Found {len(available_images)} available images'))
        
        # Shuffle images for random assignment
        random.shuffle(available_images)
        
        # Get all products
        products = Product.objects.all()
        updated_count = 0
        
        # Assign unique images to each product
        for i, product in enumerate(products):
            if i < len(available_images):
                new_image = f'products/{available_images[i]}'
                old_image = product.image.name if product.image else 'None'
                
                # Update product
                product.image = new_image
                product.save()
                
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(
                    f'Updated: {product.title}'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  OLD: {old_image}'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  NEW: {new_image}'
                ))
                self.stdout.write('')
            else:
                self.stdout.write(self.style.WARNING(
                    f'No more images available for: {product.title}'
                ))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products updated: {updated_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total products: {products.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Images used: {min(updated_count, len(available_images))}'))
        
        # Show sample of updated products
        self.stdout.write(self.style.SUCCESS('\\n=== SAMPLE OF UPDATES ==='))
        for product in products[:8]:
            image_name = product.image.name.split('/')[-1] if product.image else 'None'
            self.stdout.write(self.style.SUCCESS(
                f'  {product.category.name}: {product.title} -> {image_name}'
            ))
