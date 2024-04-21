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

        sell_1 = Product('latte di soia', 5, 0.80, 1.40)
        sell_2 = Product('tofu', 2, 2.20, 4.19) 

        target.add_to_current_sale(sell_1)
        target.add_to_current_sale(sell_2)

        self.assertAlmostEqual(6.98, target.get_current_sale_net_income())
        self.assertAlmostEqual(15.38, target.get_current_sale_gross_income())
        
        self.assertEqual("""- 5 X latte di soia: €1.40
- 2 X tofu: €4.19
""", target.get_current_sale_report())

        target.clear_current_sale()

        sell_3 = Product('seitan', 2, 1.0, 4.0)
        target.add_to_current_sale(sell_3)

        self.assertAlmostEqual(6.0, target.get_current_sale_net_income())
        self.assertAlmostEqual(8.0, target.get_current_sale_gross_income())

        self.assertAlmostEqual(23.38, target.total_gross_income)
        self.assertAlmostEqual(12.98, target.total_net_income)

        self.assertEqual("- 2 X seitan: €4.00\n", target.get_current_sale_report())

if __name__ == '__main__':
    unittest.main()
