class Store:
    def __init__(self):
        self.store = {}

    def put_item(self, item):
        item_in_store = self.get_item(item)
        if item_in_store is None:
            self.store[item.get_key()] = item
        else:
            item_in_store.quantity += item.quantity

        return self

    def get_item(self, item):
        return self.store.get(item.get_key(), None)
    
    def list(self):
        output = 'PRODOTTO QUANTITÀ PREZZO'
        for k, item in self.store.items():
            output += '\n' + item.product_name + ' ' + str(item.quantity) + ' ' + '€' + str(item.sell_price)
        output += '\n'

        return output