from django.core.management.base import BaseCommand
from products.models import Product, Category
from accounts.models import User
import json
import os

class Command(BaseCommand):
    help = 'Transfer all products from local storage to backend database'

    def handle(self, *args, **options):
        # Check for local storage products
        local_storage_paths = [
            '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/src/storage.js',
            '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/public/storage.js',
            '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/storage.json',
        ]
        
        local_products = []
        
        for path in local_storage_paths:
            if os.path.exists(path):
                self.stdout.write(self.style.SUCCESS(f'Found local storage file: {path}'))
                try:
                    with open(path, 'r') as f:
                        if path.endswith('.js'):
                            # Parse JavaScript file for products
                            content = f.read()
                            # Look for products array in JS
                            if 'products:' in content or 'const products' in content:
                                self.stdout.write(self.style.WARNING('Found products in JS file'))
                                # Extract products array (simplified)
                                import re
                                products_match = re.search(r'products:\s*\[(.*?)\]', content, re.DOTALL)
                                if products_match:
                                    try:
                                        products_data = json.loads(products_match.group(1))
                                        if isinstance(products_data, list):
                                            local_products.extend(products_data)
                                    except:
                                        pass
                        else:
                            # Parse JSON file
                            data = json.load(f)
                            if isinstance(data, list):
                                local_products.extend(data)
                            elif isinstance(data, dict) and 'products' in data:
                                local_products.extend(data['products'])
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error reading {path}: {str(e)}'))
        
        # Also check localStorage simulation in HTML/JS files
        frontend_dir = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/frontend/src'
        for root, dirs, files in os.walk(frontend_dir):
            for file in files:
                if file.endswith(('.vue', '.js', '.html')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Look for localStorage.setItem with products
                            if 'localStorage.setItem' in content and 'products' in content:
                                self.stdout.write(self.style.WARNING(f'Found localStorage usage in: {file_path}'))
                                # Extract product data if possible
                                import re
                                storage_matches = re.findall(r'localStorage\.setItem\([\'"]products[\'"]\s*,\s*(.*?)\)', content, re.DOTALL)
                                for match in storage_matches:
                                    try:
                                        if match.strip().startswith('['):
                                            products_data = json.loads(match.strip())
                                            if isinstance(products_data, list):
                                                local_products.extend(products_data)
                                                self.stdout.write(self.style.SUCCESS(f'Found {len(products_data)} products in {file_path}'))
                                    except:
                                        pass
                    except:
                        pass
        
        self.stdout.write(self.style.WARNING(f'\\nFound {len(local_products)} products in local storage'))
        
        if not local_products:
            self.stdout.write(self.style.WARNING('No products found in local storage'))
            return
        
        # Get admin user
        admin_user = User.objects.filter(role='admin').first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found!'))
            return
        
        # Get categories
        categories = {cat.name: cat for cat in Category.objects.all()}
        
        # Process local products
        transferred_count = 0
        skipped_count = 0
        
        for i, local_product in enumerate(local_products):
            try:
                # Extract product data (handle different formats)
                if isinstance(local_product, dict):
                    title = local_product.get('title') or local_product.get('name') or f'Product {i+1}'
                    price = float(local_product.get('price', 0))
                    category_name = local_product.get('category', 'accessories')
                    description = local_product.get('description', f'Transferred from local storage: {title}')
                    image = local_product.get('image', '/images/Computer.jpeg')
                    stock = int(local_product.get('stock', 10))
                else:
                    # Skip if not a dict
                    skipped_count += 1
                    continue
                
                # Map category
                if category_name not in categories:
                    category_name = 'accessories'  # default
                category = categories[category_name]
                
                # Check if product already exists (by title)
                existing = Product.objects.filter(title__iexact=title).first()
                if existing:
                    self.stdout.write(self.style.WARNING(f'Skipping (already exists): {title}'))
                    skipped_count += 1
                    continue
                
                # Create product
                product = Product.objects.create(
                    title=title,
                    description=description,
                    price=price,
                    category=category,
                    condition='new',
                    author=admin_user,
                    image=image,
                    stock=stock,
                    is_active=True,
                    is_approved=True,
                    featured=False,
                    theme_order=Product.objects.count() + 1,
                )
                
                transferred_count += 1
                self.stdout.write(self.style.SUCCESS(f'Transferred: {title} - Tsh {price}'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error transferring product {i}: {str(e)}'))
                skipped_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'\\n=== TRANSFER RESULTS ==='))
        self.stdout.write(self.style.SUCCESS(f'Products transferred: {transferred_count}'))
        self.stdout.write(self.style.WARNING(f'Products skipped: {skipped_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total products in backend: {Product.objects.count()}'))
        
        # Show category breakdown
        self.stdout.write(self.style.SUCCESS('\\n=== CATEGORY BREAKDOWN ==='))
        for category_name, category in categories.items():
            count = Product.objects.filter(category=category).count()
            if count > 0:
                self.stdout.write(self.style.SUCCESS(f'{category_name}: {count} products'))
