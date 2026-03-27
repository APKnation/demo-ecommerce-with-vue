from django.core.management.base import BaseCommand
import os
import shutil
from django.conf import settings

class Command(BaseCommand):
    help = 'Create diverse product images by copying existing ones'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== CREATING DIVERSE PRODUCT IMAGES ==='))
        
        media_products_path = os.path.join(settings.MEDIA_ROOT, 'products')
        
        # Define base images to copy from
        base_images = [
            'a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg', 'f.jpg', 'g.jpg', 'h.jpg',
            'i.jpg', 'j.jpg', 'k.jpg', 'l.jpg', 'm.jpg', 'n.jpg', 'o.jpg', 'p.jpg',
            'q.jpg', 'r.jpg', 's.jpg', 't.jpg', 'u.jpg', 'v.jpg', 'w.jpg'
        ]
        
        # Create multiple variations
        variations_created = 0
        for base_name in base_images:
            for i in range(1, 4):  # Create 3 variations of each
                new_name = f'{base_name}_var{i}.jpg'
                source_path = os.path.join(media_products_path, base_name)
                target_path = os.path.join(media_products_path, new_name)
                
                if os.path.exists(source_path):
                    try:
                        shutil.copy2(source_path, target_path)
                        self.stdout.write(self.style.SUCCESS(f'✅ Created: {new_name}'))
                        variations_created += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'❌ Failed to copy {new_name}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'\\nCreated {variations_created} new image variations'))
        self.stdout.write(self.style.SUCCESS('=== IMAGE DIVERSITY COMPLETE ==='))
