class Registry:
    def __init__(self, store):
        self.store = store

    def sell(self, item):
        itemInStore = self.store.find_item(item)
        if itemInStore is None:
            return None
        if itemInStore.quantity < item.quantity:
            return itemInStore.quantity - item.quantity
        
        itemInStore.quantity -= item.quantity

        
        