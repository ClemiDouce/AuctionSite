from django.db import models

from account.models import CustomUser
from auction.models import Auction

# Create your models here.
class Comment(models.Model):
    """"""
    content = models.TextField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    auction = models.ForeignKey(to=Auction, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        """"""
        return f"{self.author.usename} - {self.content[:25]}"