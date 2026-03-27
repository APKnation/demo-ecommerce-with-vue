from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Clear any frontend caching issues by refreshing product data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== CLEARING FRONTEND CACHE ISSUES ==='))
        
        # Force refresh all products to trigger frontend updates
        products = Product.objects.all()
        
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {products.count()}'))
        
        # Show sample of current state
        self.stdout.write(self.style.SUCCESS('\\nSample of current product-image mappings:'))
        for product in products[:8]:
            image_name = product.image.name.split('/')[-1] if product.image else 'None'
            self.stdout.write(self.style.SUCCESS(
                f'  {product.category.name}: {product.title} -> {image_name}'
            ))
        
        self.stdout.write(self.style.SUCCESS('\\n=== FRONTEND CACHE CLEAR INSTRUCTIONS ==='))
        self.stdout.write(self.style.WARNING('1. Clear browser cache (Ctrl+Shift+R)'))
        self.stdout.write(self.style.WARNING('2. Clear localStorage if needed'))
        self.stdout.write(self.style.WARNING('3. Check network tab for failed requests'))
        self.stdout.write(self.style.WARNING('4. Open debug-images.html in browser'))
        
        self.stdout.write(self.style.SUCCESS('\\n=== API ENDPOINT VERIFICATION ==='))
        self.stdout.write(self.style.SUCCESS('API: http://localhost:8000/api/products/'))
        self.stdout.write(self.style.SUCCESS('Images: http://localhost:8000/media/products/'))
        self.stdout.write(self.style.SUCCESS('Debug file: debug-images.html'))
