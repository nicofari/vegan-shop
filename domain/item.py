class Item:
    def __init__(self, product_name, quantity, buy_price, sell_price):
        self.product_name = product_name
        self.quantity = quantity
        self.buy_price = buy_price 
        self.sell_price = sell_price

    def get_key(self):
        return self.product_name
        
