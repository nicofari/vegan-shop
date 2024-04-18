import unittest

from ..domain.item import Item
from ..domain.store import Store

class TestDomain(unittest.TestCase):

    def test_item(self):
        target = Item('Tofu', 1756, 2.20, 4.19)
        
        self.assertEqual('Tofu', target.product_name)
        self.assertEqual(1756, target.quantity)
        self.assertEqual(2.20, target.buy_price)
        self.assertEqual(4.19, target.sell_price)
        self.assertEqual('Tofu_4.19', target.get_key())


    def test_store_put_get(self):
        target = Store()

        item1 = Item('tofu', 500, 2.20, 4.19)
        target.put_item(item1)

        self.assertEqual(item1, target.get_item(item1))

        item2 = Item('tofu', 25, 2.20, 4.19)
        target.put_item(item2)

        self.assertEqual(525, target.get_item(item2).quantity)

    def test_store_list(self):
        target = Store()

        item1 = Item('latte di soia', 20, 0.80, 1.40)
        item2 = Item('seitan', 5, 3, 5.49)

        target.put_item(item1)
        target.put_item(item2)

        expected_output = """PRODOTTO QUANTITÀ PREZZO
latte di soia 20 €1.4
seitan 5 €5.49
"""
        self.assertEqual(expected_output, target.list())

        

if __name__ == '__main__':
    unittest.main()
