from django.core.management.base import BaseCommand, CommandParser

from shop_app.models import Client


class Command(BaseCommand):
    help = "Created clients"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", type=int, help="Count clients")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for i in range(1, count + 1):
            client = Client(
                name=f"clientName{i}",
                email=f"email{i}@gmail.com",
                phone="+" + str(i) * 9,
                address="Bla bla bla",
            )
            client.save()

        self.stdout.write(f"{count} clients created")
