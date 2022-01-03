from django.urls import path
from .views import comment_view

urlpatterns = [
    path('', comment_view)
]
