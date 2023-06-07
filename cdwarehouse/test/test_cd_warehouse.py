import unittest

from src.cd import CD


class FakeCreditCard:
    def pay(self, card_valid):
        return card_valid


class PurchaseCDTests(unittest.TestCase):
    def test_user_purchase_in_stock_check_credit_card(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: True
        cd.buy(5, credit_card)
        self.assertEqual(cd.stock, 5)

    def test_user_purchase_not_in_stock_check_credit_card(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: True
        cd.buy(11, credit_card)
        self.assertEqual(cd.stock, 10)

    def test_user_purchase_in_stock_check_credit_card_fail(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: False
        cd.buy(5, credit_card)
        self.assertEqual(cd.stock, 10)


if __name__ == '__main__':
    unittest.main()
