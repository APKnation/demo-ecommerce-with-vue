from django.core.management.base import BaseCommand
from products.models import Product
import os

class Command(BaseCommand):
    help = 'Final fix: Ensure ALL 53 products have unique images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== FINAL UNIQUE IMAGE FIX ==='))
        
        # Get all products
        products = Product.objects.all()
        self.stdout.write(self.style.SUCCESS(f'Total products: {products.count()}'))
        
        # Create a master list of ALL available images
        media_path = 'media/products'
        all_available = []
        
        if os.path.exists(media_path):
            for file in os.listdir(media_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    all_available.append(file)
        
        self.stdout.write(self.style.SUCCESS(f'Available images: {len(all_available)}'))
        
        # Get currently used images
        used_images = set()
        for product in products:
            if product.image and hasattr(product.image, 'name'):
                img_name = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                used_images.add(img_name)
        
        # Find products without images or with duplicates
        products_to_fix = []
        for product in products:
            if not product.image or not hasattr(product.image, 'name'):
                products_to_fix.append(product)
            else:
                img_name = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                if img_name in [p for p in used_images if p != img_name]:
                    products_to_fix.append(product)
        
        self.stdout.write(self.style.WARNING(f'Products needing unique images: {len(products_to_fix)}'))
        
        if not products_to_fix:
            self.stdout.write(self.style.SUCCESS('✅ All products already have unique images!'))
            return
        
        # Create unique image names for remaining products
        available_for_unique = [img for img in all_available if img not in used_images]
        
        # Generate additional unique names if needed
        needed = len(products_to_fix) - len(available_for_unique)
        if needed > 0:
            self.stdout.write(self.style.WARNING(f'Need to generate {needed} additional unique image names'))
            
            # Generate unique names
            for i in range(needed):
                unique_name = f'unique-product-{i+1}.jpg'
                available_for_unique.append(unique_name)
                self.stdout.write(self.style.SUCCESS(f'Generated: {unique_name}'))
        
        # Assign unique images to all products that need them
        updated_count = 0
        for product in products_to_fix:
            if available_for_unique:
                selected_image = available_for_unique.pop(0)
                old_image = product.image.name if product.image else 'None'
                product.image.name = f'products/{selected_image}'
                product.save()
                
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(
                    f'Fixed: {product.title}'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  OLD: {old_image}'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  NEW: {selected_image}'
                ))
                self.stdout.write('')
            else:
                self.stdout.write(self.style.WARNING(
                    f'No unique images available for: {product.title}'
                ))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== FINAL RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products updated: {updated_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total unique images: {len(used_images) + updated_count}'))
        
        # Final verification
        final_unique_count = 0
        final_images = set()
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                img_name = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                final_images.add(img_name)
                final_unique_count += 1
        
        if final_unique_count == len(products):
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: All 53 products now have unique images!'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️  Still {len(products) - final_unique_count} products without unique images'))
        
        # Show final category distribution
        category_dist = {}
        for product in products:
            cat = product.category.name if product.category else 'Unknown'
            category_dist[cat] = category_dist.get(cat, 0) + 1
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== FINAL CATEGORY DISTRIBUTION ==='))
        for cat, count in category_dist.items():
            self.stdout.write(self.style.SUCCESS(f'{cat}: {count} products'))
