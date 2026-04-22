from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='Bright',
                email='brightohakam2019@gmail.com',
                password='adminpass'  # change this to a strong password
            )
            self.stdout.write('Superuser created successfully')
        else:
            self.stdout.write('Superuser already exists')