from django.shortcuts import render

from .models import Auction

# Create your views here.
def index(request):
    auction_list = Auction.objects.all()
    return render(request, "auction/auction_list.html", {"auction_list": auction_list})