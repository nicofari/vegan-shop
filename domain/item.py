class Item:
    def __init__(self, product_name, quantity, buy_price, sell_price):
        self.product_name = product_name
        self.quantity = quantity
        self.buy_price = buy_price 
        self.sell_price = sell_price

    def get_key(self):
        return self.product_name
    
    def __eq__(self, other) -> bool:
        is_item = isinstance(other, self.__class__)
        if not is_item:
            return False

        return self.product_name == other.product_name and self.quantity == other.quantity and self.buy_price == other.buy_price

    def __str__(self) -> str:
        return f'product_name: {self.product_name}, quantity: {self.quantity}, buy_price: {self.buy_price}, sell_price: {self.sell_price}'
    