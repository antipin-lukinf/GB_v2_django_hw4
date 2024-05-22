from django.core.management.base import  BaseCommand
from hw3_app.models import Client

class Command(BaseCommand):
    help = "Delete user by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")
    def handle (self, *args, **kwargs):

        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(self.style.WARNING(f'Successfully deleted client: {client}'))
