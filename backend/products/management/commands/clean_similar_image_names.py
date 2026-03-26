from django.core.management.base import BaseCommand
from products.models import Product
from collections import defaultdict

class Command(BaseCommand):
    help = 'Identify and optionally remove products with similar or confusing image names'

    def handle(self, *args, **options):
        # Group products by image filename patterns
        image_patterns = defaultdict(list)
        
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                image_path = product.image.name
                filename = image_path.split('/')[-1] if '/' in image_path else image_path
                
                # Identify patterns that might be confusing
                patterns = []
                
                # Single letter filenames
                if len(filename.split('.')[0]) == 1:
                    patterns.append('single_letter')
                
                # Generic placeholder names
                if any(keyword in filename.lower() for keyword in ['placeholder', 'default', 'generic']):
                    patterns.append('placeholder')
                
                # Very similar filenames (single letters)
                if filename.split('.')[0].isalpha() and len(filename.split('.')[0]) == 1:
                    patterns.append('single_letter_alpha')
                
                # Add to patterns
                for pattern in patterns:
                    image_patterns[pattern].append(product)
                
                # Also group by base filename without extension
                base_name = filename.split('.')[0]
                image_patterns[f'base_{base_name}'].append(product)

        self.stdout.write(self.style.WARNING('=== IMAGE NAME PATTERN ANALYSIS ==='))
        
        # Show patterns found
        patterns_found = []
        for pattern, products in image_patterns.items():
            if len(products) > 1 and not pattern.startswith('base_'):
                patterns_found.append((pattern, products))
        
        if not patterns_found:
            self.stdout.write(self.style.SUCCESS('No confusing image name patterns found!'))
            return
        
        self.stdout.write(self.style.WARNING('Potentially confusing image name patterns:'))
        for pattern, products in patterns_found:
            self.stdout.write(self.style.WARNING(f'\\nPattern: {pattern} ({len(products)} products)'))
            for product in products:
                filename = product.image.name.split('/')[-1] if product.image.name else 'None'
                self.stdout.write(self.style.WARNING(f'  - {product.title} -> {filename}'))
        
        # Show single letter products specifically
        single_letter_products = [p for p in Product.objects.all() 
                                  if p.image and hasattr(p.image, 'name') 
                                  and len(p.image.name.split('/')[-1].split('.')[0]) == 1]
        
        if single_letter_products:
            self.stdout.write(self.style.WARNING(f'\\n=== SINGLE LETTER IMAGE NAMES ({len(single_letter_products)} products) ==='))
            for product in single_letter_products:
                filename = product.image.name.split('/')[-1] if product.image.name else 'None'
                self.stdout.write(self.style.WARNING(f'  - {product.title} -> {filename} (Category: {product.category.name})'))
        
        # Ask if user wants to delete single letter image products
        if single_letter_products:
            self.stdout.write(self.style.WARNING(f'\\nThese single-letter image names might be confusing.'))
            confirm = input('Do you want to delete products with single-letter image names? (yes/no): ')
            
            if confirm.lower() == 'yes':
                self.stdout.write(self.style.ERROR('Deleting products with single-letter image names...'))
                deleted_count = 0
                for product in single_letter_products:
                    self.stdout.write(self.style.ERROR(f'Deleting: {product.title} (Image: {product.image.name})'))
                    product.delete()
                    deleted_count += 1
                
                self.stdout.write(self.style.SUCCESS(f'\\nSuccessfully deleted {deleted_count} products'))
                self.stdout.write(self.style.SUCCESS(f'Remaining products: {Product.objects.count()}'))
                
                # Show remaining products by category
                self.stdout.write(self.style.SUCCESS(f'\\n=== REMAINING PRODUCTS BY CATEGORY ==='))
                from products.models import Category
                for category in Category.objects.all():
                    count = Product.objects.filter(category=category).count()
                    self.stdout.write(self.style.SUCCESS(f'{category.name}: {count} products'))
            else:
                self.stdout.write(self.style.SUCCESS('No products deleted.'))
        else:
            self.stdout.write(self.style.SUCCESS('No single-letter image names found.'))
