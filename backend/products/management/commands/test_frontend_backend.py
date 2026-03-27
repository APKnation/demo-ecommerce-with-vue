from django.core.management.base import BaseCommand
import requests
import json
from io import BytesIO

class Command(BaseCommand):
    help = 'Test frontend-backend connection for product creation'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== TESTING FRONTEND-BACKEND CONNECTION ==='))
        
        # Test data matching frontend
        product_data = {
            'title': 'Frontend Test Product',
            'description': 'This is a test product from frontend simulation',
            'price': '99.99',
            'category': 4,  # laptops category
            'condition': 'new',
            'stock': 10,
            'is_active': True
        }
        
        try:
            # Get auth token
            response = requests.post(
                'http://localhost:8000/api/accounts/login/',
                json={'username': 'admin', 'password': 'admin123'}
            )
            
            if response.status_code == 200:
                token = response.json().get('token')
                self.stdout.write(self.style.SUCCESS('✅ Authentication successful'))
                
                # Simulate FormData like frontend
                files = {}
                
                # Add all fields as FormData would
                for key, value in product_data.items():
                    files[key] = (None, None, str(value))
                
                headers = {'Authorization': f'Token {token}'}
                
                # Test product creation
                response = requests.post(
                    'http://localhost:8000/api/products/create/',
                    files=files,
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
            
        self.stdout.write(self.style.SUCCESS('\\n=== FRONTEND-BACKEND TEST COMPLETE ==='))
