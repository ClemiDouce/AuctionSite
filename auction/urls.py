from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, auction_detail

app_name = 'auction'

urlpatterns = [
    path("", index, name="auction_list"),
    path("<int:auction_id>", auction_detail, name="auction_detail")
]
