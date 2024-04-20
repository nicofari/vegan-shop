import unittest

from domain.item import Item
from domain.store import Store
from services.json_storage import JsonStorage
from services.validator import Validator

class TestServices(unittest.TestCase):

    def test_persist_store(self):
        # With
        file_name = '/tmp/store.json'
        store1 = Store()
        item1 = Item('tofu', 500, 2.20, 4.19)
        store1.put_item(item1)
        JsonStorage.write(store1, file_name)

        # When
        store2 = JsonStorage.read(file_name)

        # Then
        self.assertEqual(item1, store2.find_item_by_name(item1.product_name))

        
    def test_validation(self):
        target = Validator()

        self.assertTrue(target.validate_string("latte di soia"))
        self.assertFalse(target.validate_string("Tofu_?"))

        self.assertTrue(target.validate_not_negative_integer("10"))
        self.assertTrue(target.validate_not_negative_integer("0"))
        self.assertFalse(target.validate_not_negative_integer("-1"))
        self.assertFalse(target.validate_not_negative_integer("I am not an int"))

        self.assertTrue(target.validate_not_negative_float("1.24"))
        self.assertTrue(target.validate_not_negative_float("2.4"))
        self.assertTrue(target.validate_not_negative_float("0"))
        self.assertTrue(target.validate_not_negative_float("0.0"))
        self.assertFalse(target.validate_not_negative_float("this is not a float!"))





