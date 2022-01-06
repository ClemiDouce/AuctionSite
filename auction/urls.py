from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, auction_detail

urlpatterns = [
    path("", index),
    path("<int:auction_id>", auction_detail)
]
