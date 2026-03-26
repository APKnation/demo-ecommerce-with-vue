from django.core.management.base import BaseCommand
from products.models import Product
import os
import shutil
from PIL import Image

class Command(BaseCommand):
    help = 'Create unique image copies for products using placeholder images'

    def handle(self, *args, **options):
        # Identify placeholder images
        placeholder_images = [
            'phone-placeholder.jpg',
            'laptop-placeholder.jpg', 
            'accessory-placeholder.jpg',
            'placeholder.jpg',
            'electronics-placeholder.jpg'
        ]
        
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
        
        # Media folder paths
        media_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/backend/media/products'
        frontend_folder = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/images'
        
        # Confirm the change
        confirm = input('\\nDo you want to create unique image copies for placeholder images? (yes/no): ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return
        
        updated_count = 0
        
        for product, placeholder_name in products_with_placeholders:
            # Find a good source image based on product category
            source_image = None
            
            if product.category.name == 'phones':
                # Use an existing phone image as source
                phone_images = ['iPhone.jpg', 'iPhone-16-Pro-max-300x300.jpg', 'IMG-20240518-WA0001.jpg', 'IMG-20240518-WA0002.jpg', 'IMG-20240518-WA0004.jpg']
                for img in phone_images:
                    if os.path.exists(os.path.join(frontend_folder, img)):
                        source_image = img
                        break
            elif product.category.name == 'laptops':
                # Use an existing laptop image as source
                laptop_images = ['Computer.jpeg', 'k.jpg', 'l.jpg']
                for img in laptop_images:
                    if os.path.exists(os.path.join(frontend_folder, img)):
                        source_image = img
                        break
            else:  # accessories
                # Use an existing accessory image as source
                accessory_images = ['watch1.jpeg', 'watch3.jpeg', 'Shirt2.jpeg']
                for img in accessory_images:
                    if os.path.exists(os.path.join(frontend_folder, img)):
                        source_image = img
                        break
            
            if not source_image:
                self.stdout.write(self.style.ERROR(f'No source image found for {product.title}'))
                continue
            
            # Create unique filename
            base_name = product.title.split(' - ')[-1].lower().replace(' ', '_')
            source_ext = source_image.split('.')[-1]
            unique_filename = f'unique_{base_name}_{product.id}.{source_ext}'
            
            # Copy the source image to create unique version
            source_path = os.path.join(frontend_folder, source_image)
            dest_path = os.path.join(frontend_folder, unique_filename)
            
            try:
                # Copy and slightly modify the image to make it unique
                if source_image.lower().endswith(('.jpg', '.jpeg')):
                    # Open image, apply slight modification, and save
                    with Image.open(source_path) as img:
                        # Apply a slight color adjustment to make it unique
                        from PIL import ImageEnhance
                        enhancer = ImageEnhance.Brightness(img)
                        modified_img = enhancer.enhance(0.95 + (product.id % 10) * 0.01)  # Slight brightness change
                        modified_img.save(dest_path, quality=85)
                else:
                    # For PNG and other formats, just copy
                    shutil.copy2(source_path, dest_path)
                
                # Copy to media folder as well
                media_dest_path = os.path.join(media_folder, unique_filename)
                shutil.copy2(dest_path, media_dest_path)
                
                # Update product image
                old_image = product.image.name
                product.image.name = f'products/{unique_filename}'
                product.save()
                
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(f'Updated: {product.title}'))
                self.stdout.write(self.style.SUCCESS(f'  OLD: {old_image}'))
                self.stdout.write(self.style.SUCCESS(f'  NEW: products/{unique_filename} (copied from {source_image})'))
                self.stdout.write('')
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing {product.title}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Updated {updated_count} products with unique image copies'))
        
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
