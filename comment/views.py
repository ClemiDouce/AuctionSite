from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from comment.models import Comment

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
        return super().form_valid(form)