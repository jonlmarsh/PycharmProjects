import unittest

import unittest
from 'src/Basket.py' import Basket

class Item:
    def __init__(self, price, quantity):
        pass

class BasketTest(unittest.TestCase):
    def test_total_of_empty_basket(self):
        basket = Basket([])
        total = basket.total()
        self.assertEqual(total,0.0)

    def test_total_of_single_item(self):
        basket = Basket([Item(100.0,1)])
        total = basket.total()
        self.assertEqual(total,100.00)

if __name__ == '__main__':
    unittest.main()
class coordinate
def start(x, y)

class MyTestCase(unittest.TestCase):
    def test_starting_position(self):
        self.assertEqual([x,y])


if __name__ == '__main__':
    unittest.main()



import unittest
from 'src/Basket.py' import Basket

class Item:
    def __init__(self, price, quantity):
        pass

class BasketTest(unittest.TestCase):
    def test_total_of_empty_basket(self):
        basket = Basket([])
        total = basket.total()
        self.assertEqual(total,0.0)

    def test_total_of_single_item(self):
        basket = Basket([Item(100.0,1)])
        total = basket.total()
        self.assertEqual(total,100.00)

if __name__ == '__main__':
    unittest.main()