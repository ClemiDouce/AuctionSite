from django.db import models
from django.urls import reverse
from account.models import CustomUser
from auction.models import Auction

# Create your models here.
class Comment(models.Model):
    """"""
    content = models.TextField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    auction = models.ForeignKey(to=Auction, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering =['-date_created']
    
    def __str__(self):
        """"""
        return f"{self.author.username} - {self.content[:25]}"
    
    def get_absolute_url(self):
        return reverse('comment:comment')