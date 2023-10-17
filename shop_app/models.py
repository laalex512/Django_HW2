from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"Client #{self.pk}: {self.name}, phone: {self.phone}, email: {self.email}"
        )

    def str_to_title(self):
        return f"Client #{self.pk}: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="product_photos/", blank=True, null=True)

    def __str__(self) -> str:
        return f"Product #{self.pk}: {self.name}, price: {self.price}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.product} x {self.count} for {self.order}\n"
