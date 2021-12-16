from django.db import models

# Create your models here.
from account.models import CustomUser


class Auction(models.Model):
    DURATION_TYPE = [
        ("short", "Short"),
        ("medium", "Medium"),
        ("long", "Long"),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="auction/", blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    duration_type = models.CharField(max_length=6, choices=DURATION_TYPE)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Auction"
        verbose_name_plural = "Auctions"

    def __str__(self):
        return f"{self.title} - {self.base_price} - {self.author.username}"


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    auction = models.ForeignKey(to=Auction, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bid"
        verbose_name_plural = "Bids"

    def __str__(self):
        return f"{self.auction.title} - {self.amount} - {self.author.username}"
