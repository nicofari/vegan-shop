from .base_command import BaseCommand
from domain.item import Item
from resources.messages import MESSAGES

class AddItemCommand(BaseCommand):

    def run(self):
        messages = MESSAGES[self.country_code]

        l_name = input(messages["product_name_input"])
        if l_name.strip() == "":
            return
        l_quantity = input(messages["quantity_input"])
        l_item_in_store = self.store.find_item_by_name(l_name)
        if l_item_in_store is None:
            l_buy_price = input(messages["buy_price_input"])
            l_sell_price = input(messages["sell_price_input"])
            l_new_item = Item(l_name, l_quantity, l_buy_price, l_sell_price)
        else:
            l_new_item = Item(l_name, l_quantity, l_item_in_store.buy_price, l_item_in_store.sell_price)

        self.store.put_item(l_new_item)
