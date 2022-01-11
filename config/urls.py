"""AuctionSite URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

def test(request):
    return render(request, "auction/basetemplate.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test", test),
    path('', include('auction.urls')),
    path('comment/', include('comment.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
