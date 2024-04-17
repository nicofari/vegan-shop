import unittest

from ..domain.item import Item

class TestDomain(unittest.TestCase):

    def test_name(self):
        actual = Item('Tofu', 1756, 2.20, 4.19)
        
        self.assertEquals('Tofu', actual.product_name)
        self.assertEquals(1756, actual.quantity)
        self.assertEquals(2.20, actual.buy_price)
        self.assertEquals(4.19, actual.sell_price)



if __name__ == '__main__':
    unittest.main()
