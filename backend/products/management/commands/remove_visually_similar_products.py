from django.core.management.base import BaseCommand
from products.models import Product
from collections import defaultdict

class Command(BaseCommand):
    help = 'Remove products with essentially the same images (same product type)'

    def handle(self, *args, **options):
        # Group products by visual similarity/product type
        similar_groups = defaultdict(list)
        
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if product.image.name else 'None'
                
                # Group by visual similarity
                if 'iphone' in filename.lower() or 'phone' in filename.lower():
                    similar_groups['smartphones'].append(product)
                elif 'watch' in filename.lower():
                    similar_groups['watches'].append(product)
                elif 'computer' in filename.lower() or 'laptop' in filename.lower():
                    similar_groups['computers'].append(product)
                elif 'shirt' in filename.lower():
                    similar_groups['clothing'].append(product)

        self.stdout.write(self.style.WARNING('=== VISUALLY SIMILAR PRODUCTS ANALYSIS ==='))
        
        groups_to_process = []
        for group_name, products in similar_groups.items():
            if len(products) > 1:
                groups_to_process.append((group_name, products))
                self.stdout.write(self.style.WARNING(f'\\n{group_name.upper()} GROUP ({len(products)} products):'))
                for product in products:
                    filename = product.image.name.split('/')[-1] if product.image.name else 'None'
                    self.stdout.write(self.style.WARNING(f'  - {product.title} -> {filename}'))
        
        if not groups_to_process:
            self.stdout.write(self.style.SUCCESS('No visually similar products found!'))
            return

        self.stdout.write(self.style.WARNING(f'\\nFound {len(groups_to_process)} groups with similar products'))
        
        # Ask for confirmation
        confirm = input('\\nDo you want to remove duplicates from these groups? (yes/no): ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return

        # Process each group
        total_deleted = 0
        for group_name, products in groups_to_process:
            self.stdout.write(self.style.WARNING(f'\\nProcessing {group_name} group...'))
            
            # Sort by ID to keep the oldest
            products.sort(key=lambda x: x.id)
            keep_product = products[0]
            delete_products = products[1:]
            
            self.stdout.write(self.style.SUCCESS(f'  KEEP: {keep_product.title}'))
            for product in delete_products:
                self.stdout.write(self.style.ERROR(f'  DELETE: {product.title}'))
                product.delete()
                total_deleted += 1

        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {total_deleted} duplicate products'))
        self.stdout.write(self.style.SUCCESS(f'Remaining products: {Product.objects.count()}'))
        
        # Show final product list
        self.stdout.write(self.style.SUCCESS(f'\\n=== FINAL PRODUCT LIST ==='))
        from products.models import Category
        for category in Category.objects.all():
            products = Product.objects.filter(category=category).order_by('title')
            if products.exists():
                self.stdout.write(self.style.SUCCESS(f'{category.name} ({products.count()}):'))
                for product in products:
                    filename = product.image.name.split('/')[-1] if product.image.name else 'None'
                    self.stdout.write(self.style.SUCCESS(f'  - {product.title} -> {filename}'))
