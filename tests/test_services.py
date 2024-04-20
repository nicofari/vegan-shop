import unittest

from ..domain.item import Item
from ..domain.store import Store
from ..services.json_storage import JsonStorage

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

        




