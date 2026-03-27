from django.core.management.base import BaseCommand
import os
import shutil

class Command(BaseCommand):
    help = 'Create default product images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== CREATING DEFAULT PRODUCT IMAGES ==='))
        
        media_products_path = '/media/apknation/APKnation/PROJECT/VUE/demo-ecommerce/backend/media/products'
        
        # Create default images by copying existing ones
        image_mappings = {
            'laptop-default.jpg': 'laptop-placeholder.jpg',
            'phone-default.jpg': 'phone-placeholder.jpg', 
            'accessory-default.jpg': 'electronics-placeholder.jpg',
            'default-product.jpg': 'placeholder.jpg'
        }
        
        for new_name, source_name in image_mappings.items():
            source_path = os.path.join(media_products_path, source_name)
            target_path = os.path.join(media_products_path, new_name)
            
            if os.path.exists(source_path) and not os.path.exists(target_path):
                try:
                    shutil.copy2(source_path, target_path)
                    self.stdout.write(self.style.SUCCESS(f'✅ Created: {new_name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'❌ Failed to create {new_name}: {str(e)}'))
            elif os.path.exists(target_path):
                self.stdout.write(self.style.SUCCESS(f'✅ Already exists: {new_name}'))
            else:
                self.stdout.write(self.style.ERROR(f'❌ Source not found: {source_name}'))
        
        self.stdout.write(self.style.SUCCESS('\\n=== DEFAULT IMAGES CREATION COMPLETE ==='))
