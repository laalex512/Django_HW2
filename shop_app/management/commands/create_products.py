import random
from decimal import Decimal
from django.core.management.base import BaseCommand, CommandParser

from shop_app.models import Product


class Command(BaseCommand):
    help = "Created products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", type=int, help="Count products")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for i in range(1, count + 1):
            product = Product(
                name=f"prodName{i}",
                description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptas esse, autem nam aperiam culpa repellat consectetur unde quod voluptate asperiores beatae nobis illum voluptates saepe? Nulla repellat perspiciatis dolores numquam.",
                price=Decimal(random.uniform(1, 5000)).quantize(Decimal(".01")),
                count=random.randint(1, 100),
            )
            product.save()

        self.stdout.write(f"{count} products created")
