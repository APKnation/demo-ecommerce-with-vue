from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = 'Test product creation API'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== TESTING PRODUCT CREATION ==='))
        
        # Test data
        product_data = {
            'title': 'Test Product',
            'description': 'This is a test product',
            'price': '99.99',
            'category': 4,  # Using valid laptops category ID
            'condition': 'new',
            'stock': 10,
            'is_active': True
        }
        
        try:
            # Get auth token (you'll need to replace with actual token)
            response = requests.post(
                'http://localhost:8000/api/accounts/login/',
                json={'username': 'admin', 'password': 'admin123'}
            )
            
            if response.status_code == 200:
                token = response.json().get('token')
                self.stdout.write(self.style.SUCCESS('✅ Authentication successful'))
                
                # Test product creation
                headers = {'Authorization': f'Token {token}'}
                response = requests.post(
                    'http://localhost:8000/api/products/create/',
                    json=product_data,
                    headers=headers
                )
                
                self.stdout.write(self.style.SUCCESS(f'Status Code: {response.status_code}'))
                
                if response.status_code == 201:
                    self.stdout.write(self.style.SUCCESS('✅ Product creation successful!'))
                    self.stdout.write(self.style.SUCCESS(f'Product: {response.json()}'))
                else:
                    self.stdout.write(self.style.ERROR(f'❌ Product creation failed: {response.status_code}'))
                    self.stdout.write(self.style.ERROR(f'Response: {response.text}'))
            else:
                self.stdout.write(self.style.ERROR('❌ Authentication failed'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {str(e)}'))
