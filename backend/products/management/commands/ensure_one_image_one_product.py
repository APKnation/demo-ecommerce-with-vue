from django.core.management.base import BaseCommand
from products.models import Product
from collections import defaultdict

class Command(BaseCommand):
    help = 'Ensure each image belongs to only one product (one-to-one image-product mapping)'

    def handle(self, *args, **options):
        # Check current image usage
        image_usage = defaultdict(list)
        
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                image_usage[filename].append(product)

        self.stdout.write(self.style.WARNING('=== IMAGE TO PRODUCT MAPPING ANALYSIS ==='))
        
        # Find images used by multiple products
        conflicts_found = False
        conflicts = []
        
        for filename, products in image_usage.items():
            if len(products) > 1:
                conflicts_found = True
                conflicts.append((filename, products))
                self.stdout.write(self.style.ERROR(f'CONFLICT: {filename} used by {len(products)} products:'))
                for product in products:
                    self.stdout.write(self.style.ERROR(f'  - {product.title} (ID: {product.id})'))

        if not conflicts_found:
            self.stdout.write(self.style.SUCCESS('✅ PERFECT: Each image belongs to exactly one product!'))
            
            # Show current mapping
            self.stdout.write(self.style.SUCCESS('\\n=== CURRENT IMAGE TO PRODUCT MAPPING ==='))
            for filename, products in sorted(image_usage.items()):
                product = products[0]
                self.stdout.write(self.style.SUCCESS(f'  {filename} -> {product.title}'))
            
            return

        # Handle conflicts
        self.stdout.write(self.style.WARNING(f'\\nFound {len(conflicts)} image conflicts'))
        confirm = input('Do you want to resolve these conflicts by keeping the first product for each image? (yes/no): ')
        
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return

        # Resolve conflicts
        total_resolved = 0
        for filename, products in conflicts:
            self.stdout.write(self.style.WARNING(f'\\nResolving conflict for: {filename}'))
            
            # Keep the first product (oldest ID)
            products.sort(key=lambda x: x.id)
            keep_product = products[0]
            remove_products = products[1:]
            
            self.stdout.write(self.style.SUCCESS(f'  KEEP: {keep_product.title} (ID: {keep_product.id})'))
            
            for product in remove_products:
                self.stdout.write(self.style.ERROR(f'  REMOVE IMAGE FROM: {product.title} (ID: {product.id})'))
                product.image = None
                product.save()
                total_resolved += 1

        self.stdout.write(self.style.SUCCESS(f'\\n=== RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Resolved {total_resolved} image conflicts'))
        self.stdout.write(self.style.SUCCESS(f'Products with images: {Product.objects.filter(image__isnull=False).exclude(image="").count()}'))
        self.stdout.write(self.style.SUCCESS(f'Products without images: {Product.objects.filter(image__isnull=True).count()}'))

        # Final verification
        self.stdout.write(self.style.SUCCESS('\\n=== FINAL VERIFICATION ==='))
        final_image_usage = defaultdict(list)
        for product in Product.objects.all():
            if product.image and hasattr(product.image, 'name'):
                filename = product.image.name.split('/')[-1] if '/' in product.image.name else product.image.name
                final_image_usage[filename].append(product)

        conflicts_remaining = len([k for k, v in final_image_usage.items() if len(v) > 1])
        if conflicts_remaining == 0:
            self.stdout.write(self.style.SUCCESS('✅ SUCCESS: Each image now belongs to exactly one product!'))
        else:
            self.stdout.write(self.style.ERROR(f'❌ Still have {conflicts_remaining} conflicts'))
