import tempfile

from django.test import TestCase

from account.models import CustomUser
from auction.models import Auction, Bid


class AuctionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.object.create_user(username="test", password="test124", email="test@email.fr")

    def test_creation_auction(self):
        auction = Auction.objects.create(
            title="Action1",
            description="Description test",
            base_price=100.00,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            duration_type="short",
            author=self.user
        )
        self.assertEqual(auction.title, "Action1")
        auction.save()
        temp_auction = Auction.objects.first()
        self.assertEqual(temp_auction.base_price, 100.00)

    def test_create_bid(self):
        auction = Auction.objects.create(
            title="Action1",
            description="Description test",
            base_price=100.00,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            duration_type="short",
            author=self.user
        )
        bid = Bid.objects.create(
            amount=200.00,
            author=self.user,
            auction=auction
        )
        self.assertEqual(bid.amount, 200.00)
        bid.save()
        temp_bid = Bid.objects.first()
        self.assertEqual(temp_bid.auction, auction)
