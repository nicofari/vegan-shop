from .too_many_exception import TooManyException
from .item import Item

import json

class Store:
    """Represents a store of items"""
    """API: get|put|find|list items in store """
    
    def __init__(self, store = None):
        if store is None:
            self.store = {}
        else:
            self.store = store

    def put_item(self, item):
        item_in_store = self.find_item_by_name(item.product_name)
        if item_in_store is None:
            self.store[item.get_key()] = item
        else:
            item_in_store.quantity += item.quantity

    def find_item_by_name(self, product_name):
        return self.store.get(product_name, None)
    
    def list(self):
        output = 'PRODOTTO QUANTITÀ PREZZO'
        for k, item in self.store.items():
            output += '\n' + item.product_name + ' ' + str(item.quantity) + ' ' + '€' + str(item.sell_price)
        output += '\n'

        return output
    
    def get_item(self, item):
        item_in_store = self.find_item_by_name(item.product_name)
        if item_in_store is None:
            return None
        else:
            if item_in_store.quantity < item.quantity:
                raise TooManyException()
            else:
                item_in_store.quantity -= item.quantity

        return item_in_store
