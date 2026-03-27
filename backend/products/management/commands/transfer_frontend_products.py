from django.core.management.base import BaseCommand
from products.models import Product, Category
from accounts.models import User

class Command(BaseCommand):
    help = 'Transfer default frontend products to backend database'

    def handle(self, *args, **options):
        # Default products from Home.vue
        default_products = [
            { id: 1, name: 'Mac Book', price: 1000000, category: 'laptops', image: '/images/w.jpg' },
            { id: 2, name: 'HP-Brand', price: 150000, category: 'laptops', image: '/images/j.jpg' },
            { id: 3, name: 'Dell', price: 200000, category: 'laptops', image: '/images/k.jpg' },
            { id: 4, name: 'Apple', price: 1000000, category: 'phones', image: '/images/d.jpg' },
            { id: 5, name: 'HP-Elite', price: 1500000, category: 'laptops', image: '/images/a.jpg' },
            { id: 6, name: 'Sony', price: 200000, category: 'accessories', image: '/images/f.jpg' },
            { id: 7, name: 'Infinix', price: 400000, category: 'phones', image: '/images/g.jpg' },
            { id: 8, name: 'iPhone', price: 1500000, category: 'phones', image: '/images/p.jpg' },
            { id: 9, name: 'Samsung', price: 3000000, category: 'phones', image: '/images/l.jpg' }
        ]
        
        self.stdout.write(self.style.WARNING('=== TRANSFER DEFAULT FRONTEND PRODUCTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Found {len(default_products)} default products'))
        
        # Get admin user
        admin_user = User.objects.filter(role='admin').first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found!'))
            return
        
        # Get categories
        categories = {cat.name: cat for cat in Category.objects.all()}
        
        transferred_count = 0
        skipped_count = 0
        
        for frontend_product in default_products:
            try:
                # Check if product already exists
                existing = Product.objects.filter(title__iexact=frontend_product['name']).first()
                if existing:
                    self.stdout.write(self.style.WARNING(f'Skipping (already exists): {frontend_product["name"]}'))
                    skipped_count += 1
                    continue
                
                # Map category
                category_name = frontend_product['category']
                if category_name not in categories:
                    category_name = 'accessories'  # default
                category = categories[category_name]
                
                # Convert frontend image path to backend path
                image_path = frontend_product['image']
                if image_path.startswith('/images/'):
                    filename = image_path.replace('/images/', '')
                    backend_image_path = f'products/{filename}'
                else:
                    backend_image_path = image_path
                
                # Create product
                product = Product.objects.create(
                    title=frontend_product['name'],
                    description=f'Transferred from frontend local storage: {frontend_product["name"]}. High-quality product with excellent features.',
                    price=frontend_product['price'],
                    category=category,
                    condition='new',
                    author=admin_user,
                    image=backend_image_path,
                    stock=20,
                    is_active=True,
                    is_approved=True,
                    featured=False,
                    theme_order=Product.objects.count() + 1,
                )
                
                transferred_count += 1
                self.stdout.write(self.style.SUCCESS(f'Transferred: {frontend_product["name"]} - Tsh {frontend_product["price"]:,}'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error transferring {frontend_product.get("name", "Unknown")}: {str(e)}'))
                skipped_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== TRANSFER RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products transferred: {transferred_count}'))
        self.stdout.write(self.style.WARNING(f'Products skipped: {skipped_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total products in backend: {Product.objects.count()}'))
        
        # Also check for any localStorage adminProducts
        self.stdout.write(self.style.WARNING('\\n=== CHECKING LOCALSTORAGE ==='))
        self.stdout.write(self.style.WARNING('Note: localStorage products are stored in browser and cannot be accessed from server'))
        self.stdout.write(self.style.WARNING('To transfer localStorage products:'))
        self.stdout.write(self.style.WARNING('1. Open browser developer tools'))
        self.stdout.write(self.style.WARNING('2. Go to Application tab → Local Storage'))
        self.stdout.write(self.style.WARNING('3. Copy the adminProducts value'))
        self.stdout.write(self.style.WARNING('4. Create a JSON file and run transfer command again'))
