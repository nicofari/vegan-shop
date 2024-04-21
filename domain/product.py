from domain.invalid_argument_exception import InvalidArgumentException

class Product:
    """Product"""
    """Represents a product item saved in the store"""

    def __init__(self, name, quantity, buy_price, sell_price):
        if not isinstance(quantity, int):
            raise InvalidArgumentException("Quantity must be int")

        if not isinstance(buy_price, float):
            raise InvalidArgumentException("Buy price must be a float")
        
        if not isinstance(sell_price, float):
            raise InvalidArgumentException("Sell price must be a float")
        
        self.name = name
        self.quantity = quantity
        self.buy_price = buy_price 
        self.sell_price = sell_price

    def get_key(self):
        return self.name
    
    def __eq__(self, other) -> bool:
        is_item = isinstance(other, self.__class__)
        if not is_item:
            return False

        return self.name == other.name and self.quantity == other.quantity and self.buy_price == other.buy_price

    def __str__(self) -> str:
        return f'name: {self.name}, quantity: {self.quantity}, buy_price: {self.buy_price}, sell_price: {self.sell_price}'
    