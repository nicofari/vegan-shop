from .base_command import BaseCommand
from domain.item import Item
from resources.messages import MESSAGES

class AddItemCommand(BaseCommand):

    def run(self):
        messages = MESSAGES[self.country_code]

        l_name = input(messages["PRODUCT_NAME_INPUT"])
        if not self.validator.validate_string(l_name):
            print(messages["INVALID_STRING"])
            return
        
        if l_name.strip() == "":
            return
        
        l_quantity = input(messages["QUANTITY_INPUT"])
        if not self.validator.validate_not_negative_integer(l_quantity):
            print(messages["INVALID_INTEGER"] %(l_quantity))
            return

        l_item_in_store = self.store.find_item_by_name(l_name)
        if l_item_in_store is None:
            l_buy_price = input(messages["BUY_PRICE_INPUT"])
            if not self.validator.validate_not_negative_float(l_buy_price):
                print(messages["INVALID_FLOAT"] %(l_buy_price))
                return
           
            l_sell_price = input(messages["SELL_PRICE_INPUT"])
            if not self.validator.validate_not_negative_float(l_sell_price):
                print(messages["INVALID_FLOAT"] %(l_sell_price))
                return

            l_new_item = Item(l_name, l_quantity, l_buy_price, l_sell_price)
        else:
            l_new_item = Item(l_name, l_quantity, l_item_in_store.buy_price, l_item_in_store.sell_price)

        self.store.put_item(l_new_item)
