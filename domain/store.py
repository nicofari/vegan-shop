class Store:
    def __init__(self):
        self.store = []

    def add(self, item):
        self.store.append(item)


    def findItemByNameAndSellPrice(self, item):
        for it in self.store:
            if it.product_name == item.product_name && it.sell_price == item.sell_price