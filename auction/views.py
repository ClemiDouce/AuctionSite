from django.shortcuts import render

from .models import Auction
from comment.models import Comment

# Create your views here.
def index(request):
    auction_list = Auction.objects.all()
    return render(request, "auction/auction_list.html", {"auction_list": auction_list})

def auction_detail(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    comments = Comment.objects.filter(auction=auction)
    return render(request, "auction/auction_detail.html", {"auction": auction, "comments": comments})