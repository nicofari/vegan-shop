import unittest

from ..domain.item import Item
from ..domain.store import Store
from ..domain.too_many_exception import TooManyException

class TestDomain(unittest.TestCase):

    def test_item(self):
        target = Item('Tofu', 1756, 2.20, 4.19)
        
        self.assertEqual('Tofu', target.product_name)
        self.assertEqual(1756, target.quantity)
        self.assertEqual(2.20, target.buy_price)
        self.assertEqual(4.19, target.sell_price)
        self.assertEqual('Tofu', target.get_key())


    def test_store_put_find(self):
        target = Store()

        item1 = Item('tofu', 500, 2.20, 4.19)
        target.put_item(item1)

        self.assertEqual(item1, target.find_item(item1))

        item2 = Item('tofu', 25, 2.20, 4.19)
        target.put_item(item2)

        self.assertEqual(525, target.find_item(item2).quantity)

    def test_store_get(self):
        target = Store()

        item1 = Item('tofu', 500, 2.20, 4.19)
        target.put_item(item1)

        itemToSell = Item('latte di soia', 12, 1, 2)

        actual = target.get_item(itemToSell)

        self.assertEqual(None, actual)

        itemToSell = Item('tofu', 1500, 2.20, 4.19)

        with self.assertRaises(TooManyException):
            target.get_item(itemToSell)

        itemToSell = Item('tofu', 300, 2.20, 4.19)

        target.get_item(itemToSell)

        itemAfterSell = target.find_item(itemToSell)

        self.assertEqual(200, itemAfterSell.quantity)

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
