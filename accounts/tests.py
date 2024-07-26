from django.test import TestCase
from django.contrib.auth import get_user_model

class StockUserTest(TestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='testuser',
            password='testpass123',
            money=15000.00,
            today_money=10000,
            yesterday_money=9000
        )

    def test_change_money(self):
        self.user.change_money()
        self.user.refresh_from_db()
        self.assertEqual(self.user.yesterday_money, 10000)
        self.assertEqual(self.user.today_money, 15000)
