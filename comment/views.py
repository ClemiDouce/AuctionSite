from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from comment.models import Comment
from auction.models import Auction

from .forms import NewCommentForm


class CommentAuctionView(ListView):
    model = Comment
    context_object_name = "comments"
    template_name = "comment/comment_details.html"

    
class CommentAuctionCreate(CreateView):
    model = Comment
    form_class = NewCommentForm
    template_name = "comment/create_comment.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user

        form.instance.auction_id = self.kwargs['auction_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("auction:auction_detail", kwargs={"auction_id": self.kwargs["auction_id"]})