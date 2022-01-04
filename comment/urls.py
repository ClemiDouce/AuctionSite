from django.urls import path
from .views import CommentAuctionView, CommentAuctionCreate

app_name = 'comment'

urlpatterns = [
    #path('', comment_view, name='comment' ),
    path('', CommentAuctionView.as_view(), name='comment' ),
    path('new-comment/', CommentAuctionCreate.as_view(), name='new-comment'),
    #path('new-comment/', create_comment, name='new-comment')
]
