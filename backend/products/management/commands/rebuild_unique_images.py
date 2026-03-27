from django.core.management.base import BaseCommand
from products.models import Product
import os
import random

class Command(BaseCommand):
    help = 'Rebuild Admin and Home pages to use unique images - complete image diversity fix'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== REBUILDING FOR UNIQUE IMAGES ==='))
        
        # Get all products
        products = Product.objects.all()
        self.stdout.write(self.style.SUCCESS(f'Total products: {products.count()}'))
        
        # Create category-specific image pools
        phone_images = [
            'iPhone.jpg', 'iPhone-16-Pro-max-300x300.jpg', 'IMG-20240518-WA0004.jpg',
            'IMG-20240518-WA0001.jpg', 'IMG-20240518-WA0002.jpg', 'l.jpg',
            'IMG-20240518-WA0000.jpg', 'd.jpg', 'p.jpg', 'q.jpg', 'r.jpg'
        ]
        
        laptop_images = [
            'Computer.jpeg', 'Mac Book.jpeg', 'k.jpg', 'j.jpg', 'h.jpg', 'a.jpg',
            't.jpg', 's.jpg', 'o.jpg', 'w.jpg', 'n.jpg', 'm.jpg', 'c.jpg',
            'b.jpg', 'IMG-20240518-WA0002.jpg', 'wa0000-unique.jpg', 'wa0001-unique.jpg',
            'wa0002-unique.jpg', 'computer-unique.jpg'
        ]
        
        accessory_images = [
            'watch1.jpeg', 'watch3.jpeg', 'Shirt2.jpeg', 'f.jpg', 'e.jpg', 'i.jpg',
            'u.jpg', 'v.jpg', 'shirt2-unique.jpg', 'sigin-unique.png'
        ]
        
        # Shuffle each category pool
        random.shuffle(phone_images)
        random.shuffle(laptop_images)
        random.shuffle(accessory_images)
        
        # Assign unique images ensuring no duplicates
        used_images = set()
        updated_count = 0
        
        for product in products:
            category_name = product.category.name.lower() if product.category else 'unknown'
            
            # Select appropriate image pool
            if 'phone' in category_name:
                available = [img for img in phone_images if img not in used_images]
            elif 'laptop' in category_name:
                available = [img for img in laptop_images if img not in used_images]
            elif 'accessory' in category_name:
                available = [img for img in accessory_images if img not in used_images]
            else:
                available = [img for img in (phone_images + laptop_images + accessory_images) if img not in used_images]
            
            if available:
                selected_image = random.choice(available)
                used_images.add(selected_image)
                
                old_image = product.image.name if product.image else 'None'
                product.image.name = f'products/{selected_image}'
                product.save()
                
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(
                    f'Updated: {product.title} ({category_name})'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  OLD: {old_image}'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'  NEW: products/{selected_image}'
                ))
                self.stdout.write('')
            else:
                self.stdout.write(self.style.WARNING(
                    f'No unique images available for: {product.title}'
                ))
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products updated: {updated_count}'))
        self.stdout.write(self.style.SUCCESS(f'Unique images used: {len(used_images)}'))
        
        # Verify no duplicates
        image_counts = {}
        for product in products:
            if product.image:
                img_name = product.image.name.split('/')[-1]
                image_counts[img_name] = image_counts.get(img_name, 0) + 1
        
        duplicates = {img: count for img, count in image_counts.items() if count > 1}
        if duplicates:
            self.stdout.write(self.style.WARNING(f'⚠️  Found duplicates: {duplicates}'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: All products have unique images!'))
        
        # Show category distribution
        category_dist = {}
        for product in products:
            cat = product.category.name if product.category else 'Unknown'
            category_dist[cat] = category_dist.get(cat, 0) + 1
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== CATEGORY DISTRIBUTION ==='))
        for cat, count in category_dist.items():
            self.stdout.write(self.style.SUCCESS(f'{cat}: {count} products'))
