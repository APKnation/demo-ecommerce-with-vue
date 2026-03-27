from django.core.management.base import BaseCommand
from products.models import Product
import os
import random

class Command(BaseCommand):
    help = 'Fix all product-image mappings to ensure phones use phone images, laptops use laptop images, etc.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== FIXING PRODUCT-IMAGE MAPPINGS ==='))
        
        # Define appropriate images for each category
        category_images = {
            'phones': [
                'iPhone.jpg', 'iPhone-16-Pro-max-300x300.jpg', 'IMG-20240518-WA0001.jpg', 
                'IMG-20240518-WA0002.jpg', 'IMG-20240518-WA0004.jpg',
                'd.jpg', 'g.jpg', 'l.jpg', 'p.jpg', 'q.jpg', 'r.jpg'
            ],
            'laptops': [
                'Computer.jpeg', 'k.jpg', 'j.jpg', 'w.jpg', 'a.jpg', 'b.jpg', 
                'c.jpg', 'h.jpg', 'm.jpg', 'n.jpg', 'o.jpg', 's.jpg', 't.jpg'
            ],
            'accessories': [
                'watch1.jpeg', 'watch3.jpeg', 'Shirt2.jpeg', 'f.jpg', 'e.jpg', 
                'i.jpg', 'u.jpg', 'v.jpg', 'IMG-20240518-WA0000.jpg'
            ]
        }
        
        # Get all products
        products = list(Product.objects.all())
        updated_count = 0
        used_images = {}  # Track used images to avoid duplicates
        
        for product in products:
            category_name = product.category.name.lower()
            
            # Get available images for this category
            if category_name in category_images:
                available_images = [img for img in category_images[category_name] 
                                if img not in used_images.get(category_name, set())]
                
                if available_images:
                    # Select a random appropriate image
                    new_image = random.choice(available_images)
                    
                    # Update the product
                    old_image = product.image.name if product.image else 'None'
                    product.image = f'products/{new_image}'
                    product.save()
                    
                    # Track used image
                    if category_name not in used_images:
                        used_images[category_name] = set()
                    used_images[category_name].add(new_image)
                    
                    updated_count += 1
                    
                    self.stdout.write(self.style.SUCCESS(
                        f'Fixed: {product.title} ({category_name})'
                    ))
                    self.stdout.write(self.style.SUCCESS(
                        f'  OLD: {old_image}'
                    ))
                    self.stdout.write(self.style.SUCCESS(
                        f'  NEW: products/{new_image}'
                    ))
                    self.stdout.write('')
                else:
                    self.stdout.write(self.style.WARNING(
                        f'No available images for {product.title} ({category_name})'
                    ))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products updated: {updated_count}'))
        
        # Verify the fixes
        self.stdout.write(self.style.SUCCESS('\\n=== VERIFICATION ==='))
        verification_problems = []
        
        for product in Product.objects.all()[:10]:  # Check first 10
            image_name = product.image.name.split('/')[-1] if product.image else 'None'
            category_name = product.category.name.lower()
            
            # Check if image is appropriate for category
            if category_name == 'phones' and any(laptop_img in image_name.lower() for laptop_img in ['laptop', 'computer']):
                verification_problems.append(f'{product.title} -> {image_name} (PHONE with laptop image)')
            elif category_name == 'laptops' and any(phone_img in image_name.lower() for phone_img in ['phone', 'iphone']):
                verification_problems.append(f'{product.title} -> {image_name} (LAPTOP with phone image)')
        
        if verification_problems:
            self.stdout.write(self.style.WARNING('Still found issues:'))
            for problem in verification_problems:
                self.stdout.write(self.style.WARNING(f'  ❌ {problem}'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ All checked products have appropriate images!'))
        
        # Show unique image count
        unique_images = set()
        for product in Product.objects.all():
            if product.image:
                img_name = product.image.name.split('/')[-1]
                unique_images.add(img_name)
        
        self.stdout.write(self.style.SUCCESS(f'\\nUnique images used: {len(unique_images)}'))
        self.stdout.write(self.style.SUCCESS(f'Total products: {Product.objects.count()}'))
