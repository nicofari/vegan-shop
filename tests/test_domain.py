import unittest

from domain.product import Product
from domain.store import Store
from domain.registry import Registry
from domain.stock_exceeded_exception import StockExceededException

class TestDomain(unittest.TestCase):

    def test_product(self):
        target = Product('Tofu', 1756, 2.20, 4.19)
        
        self.assertEqual('Tofu', target.name)
        self.assertEqual(1756, target.quantity)
        self.assertEqual(2.20, target.buy_price)
        self.assertEqual(4.19, target.sell_price)
        self.assertEqual('Tofu', target.get_key())


    def test_store_put_find(self):
        target = Store()

        item1 = Product('tofu', 500, 2.20, 4.19)
        target.put_item(item1)

        self.assertEqual(item1, target.find_item_by_name(item1.name))

        item2 = Product('tofu', 25, 2.20, 4.19)
        target.put_item(item2)

        self.assertEqual(525, target.find_item_by_name(item2.name).quantity)

    def test_store_get(self):
        target = Store()

        item1 = Product('tofu', 500, 2.20, 4.19)
        target.put_item(item1)

        itemToSell = Product('latte di soia', 12, 1.0, 2.0)

        actual = target.get_item(itemToSell)

        self.assertEqual(None, actual)

        itemToSell = Product('tofu', 1500, 2.20, 4.19)

        with self.assertRaises(StockExceededException):
            target.get_item(itemToSell)

        itemToSell = Product('tofu', 300, 2.20, 4.19)

        target.get_item(itemToSell)

        itemAfterSell = target.find_item_by_name(itemToSell.name)

        self.assertEqual(200, itemAfterSell.quantity)

    def test_store_list(self):
        target = Store()

        item1 = Product('latte di soia', 20, 0.80, 1.40)
        item2 = Product('seitan', 5, 3.0, 5.49)

        target.put_item(item1)
        target.put_item(item2)

        expected_output = """PRODOTTO QUANTITÀ PREZZO
latte di soia 20 €1.4
seitan 5 €5.49
"""
        self.assertEqual(expected_output, target.list("PRODOTTO QUANTITÀ PREZZO"))

    def test_registry(self):
        target = Registry()

        self.assertEqual(0.0, target.gross_income)
        self.assertEqual(0.0, target.net_income)

        target.store_income(27.45 - 15, 27.45)
        target.store_income(6.45 - 2, 6.45)

        self.assertEqual(16.9, target.net_income)
        self.assertEqual(33.9, target.gross_income)

if __name__ == '__main__':
    unittest.main()
