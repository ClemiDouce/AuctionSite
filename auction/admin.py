from django.contrib import admin

# Register your models here.
from auction.models import Auction, Bid


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "base_price", "image"]

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bid._meta.get_fields()]