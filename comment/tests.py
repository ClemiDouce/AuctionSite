from django.test import TestCase
from account.models import CustomUser
from auction.models import Auction
from comment.models import Comment

# Create your tests here.


class TestComment(TestCase):
    """"""
    def setUp(self):
        user = CustomUser.object.create(username='Usertest', 
                                        email='test@test.fr',
                                        password='motdepasse445')
        auction = Auction.objects.create(title='AuctionTest', base_price=12, author=user)
        comment = Comment.objects.create(content="je fais un test", author=user, auction=auction)
        comment.save()
        
    def test_comment_model(self):
        """test the model content text"""
        comment_test = Comment.objects.get(content="je fais un test")
        self.assertEqual(comment_test.content, "je fais un test")
       