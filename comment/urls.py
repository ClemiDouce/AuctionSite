from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CommentAuctionView, CommentAuctionCreate

app_name = 'comment'

urlpatterns = [
    path('', CommentAuctionView.as_view(), name='comment' ),
    path('new-comment/<int:auction_id>', CommentAuctionCreate.as_view(), name='new-comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
