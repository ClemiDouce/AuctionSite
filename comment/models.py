from django.db import models

from account.models import CustomUser
from auction.models import Auction

# Create your models here.
class Comment(models.Model):
    """"""
    content = models.TextField(max_length=255, blank=False, null=False)
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(to=Auction, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'