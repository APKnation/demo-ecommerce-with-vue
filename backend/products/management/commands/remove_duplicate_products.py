from django.core.management.base import BaseCommand
from products.models import Product
from collections import defaultdict

class Command(BaseCommand):
    help = 'Remove duplicate products with same base name, keeping only one per base name'

    def handle(self, *args, **options):
        # Find products with similar names (ignoring the image identifier part)
        name_products = defaultdict(list)
        for product in Product.objects.all():
            # Extract base name before the dash and image identifier
            base_name = product.title.split(' - ')[0] if ' - ' in product.title else product.title
            name_products[base_name].append(product)

        duplicates_found = False
        products_to_delete = []
        products_to_keep = []

        self.stdout.write(self.style.WARNING('=== DUPLICATE PRODUCTS ANALYSIS ==='))
        
        for base_name, products in name_products.items():
            if len(products) > 1:
                duplicates_found = True
                self.stdout.write(self.style.WARNING(f'Base Name: {base_name} - Found {len(products)} products:'))
                
                # Sort by ID to keep the first one (oldest)
                products.sort(key=lambda x: x.id)
                keep_product = products[0]
                delete_products = products[1:]
                
                products_to_keep.append(keep_product)
                products_to_delete.extend(delete_products)
                
                self.stdout.write(self.style.SUCCESS(f'  KEEP: ID {keep_product.id} - {keep_product.title}'))
                for product in delete_products:
                    self.stdout.write(self.style.ERROR(f'  DELETE: ID {product.id} - {product.title}'))
                self.stdout.write('')

        if not duplicates_found:
            self.stdout.write(self.style.SUCCESS('No duplicate products found!'))
            return

        self.stdout.write(self.style.WARNING(f'=== SUMMARY ==='))
        self.stdout.write(self.style.WARNING(f'Products to keep: {len(products_to_keep)}'))
        self.stdout.write(self.style.WARNING(f'Products to delete: {len(products_to_delete)}'))
        self.stdout.write(self.style.WARNING(f'Total products before: {Product.objects.count()}'))
        
        if products_to_delete:
            # Ask for confirmation
            confirm = input('\\nAre you sure you want to delete these duplicate products? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.ERROR('Operation cancelled.'))
                return
            
            # Delete the duplicate products
            deleted_count = 0
            for product in products_to_delete:
                self.stdout.write(self.style.ERROR(f'Deleting: {product.title}'))
                product.delete()
                deleted_count += 1
            
            self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} duplicate products'))
            self.stdout.write(self.style.SUCCESS(f'Total products after: {Product.objects.count()}'))
            
            # Show remaining products by category
            self.stdout.write(self.style.SUCCESS(f'\\n=== REMAINING PRODUCTS BY CATEGORY ==='))
            from products.models import Category
            for category in Category.objects.all():
                count = Product.objects.filter(category=category).count()
                self.stdout.write(self.style.SUCCESS(f'{category.name}: {count} products'))
        else:
            self.stdout.write(self.style.SUCCESS('No products to delete.'))
