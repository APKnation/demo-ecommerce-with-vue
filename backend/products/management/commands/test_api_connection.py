from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = 'Test direct API connection'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== TESTING DIRECT API CONNECTION ==='))
        
        try:
            # Test 1: Simple health check
            response = requests.get('http://localhost:8000/api/products/', timeout=5)
            self.stdout.write(self.style.SUCCESS(f'✅ Products API Status: {response.status_code}'))
            
            # Test 2: Categories API
            response = requests.get('http://localhost:8000/api/products/categories/', timeout=5)
            self.stdout.write(self.style.SUCCESS(f'✅ Categories API Status: {response.status_code}'))
            
            # Test 3: Auth endpoint
            response = requests.post(
                'http://localhost:8000/api/accounts/login/',
                json={'username': 'admin', 'password': 'admin123'},
                timeout=5
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Auth API Status: {response.status_code}'))
            
            if response.status_code == 200:
                token = response.json().get('token')
                
                # Test 4: Product creation with proper headers
                headers = {'Authorization': f'Token {token}'}
                data = {
                    'title': 'Connection Test Product',
                    'description': 'Testing API connection',
                    'price': '99.99',
                    'category': 4,
                    'condition': 'new',
                    'stock': 10,
                    'is_active': True
                }
                
                response = requests.post(
                    'http://localhost:8000/api/products/create/',
                    json=data,
                    headers=headers,
                    timeout=5
                )
                
                self.stdout.write(self.style.SUCCESS(f'✅ Product Creation Status: {response.status_code}'))
                
                if response.status_code == 201:
                    self.stdout.write(self.style.SUCCESS('✅ API CONNECTION WORKING PERFECTLY!'))
                else:
                    self.stdout.write(self.style.ERROR(f'❌ Product Creation Failed: {response.text}'))
            else:
                self.stdout.write(self.style.ERROR('❌ Authentication failed'))
                
        except requests.exceptions.ConnectionError as e:
            self.stdout.write(self.style.ERROR(f'❌ Connection Error: {str(e)}'))
        except requests.exceptions.Timeout as e:
            self.stdout.write(self.style.ERROR(f'❌ Timeout Error: {str(e)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Unknown Error: {str(e)}'))
            
        self.stdout.write(self.style.SUCCESS('\\n=== CONNECTION TEST COMPLETE ==='))
