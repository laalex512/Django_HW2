from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Return Client by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Client ID")
        parser.add_argument("name", type=str, help="New Name")

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        name = kwargs.get("name")
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.name = name
            client.save()
            self.stdout.write(f"{client} succlessfully changed")
        else:
            self.stdout.write(f"Client with id = {pk} doesn't exists")
