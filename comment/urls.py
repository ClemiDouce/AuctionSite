from django.urls import path
from .views import comment_view, create_comment

urlpatterns = [
    path('', comment_view, name='comment' ),
    path('new-comment/', create_comment, name='new-comment')
]
