from .base_command import BaseCommand
from resources.messages import MESSAGES, BOOLEAN_VALUES
from domain.product import Product

class SellCommand(BaseCommand):

    def __init__(self, store, country_code, validator, registry):
        super().__init__(store, country_code, validator)

        self.registry = registry

    def run(self):
        messages = MESSAGES[self.country_code]
        boolean_values = BOOLEAN_VALUES[self.country_code]

        self.registry.clear_current_sale()

        while True:
            l_name = input(messages["PRODUCT_NAME_INPUT"])
            if not self.validator.validate_string(l_name):
                print(messages["INVALID_STRING"])
                return
            
            if l_name.strip() == "":
                return
            
            l_item_in_store = self.store.find_item_by_name(l_name)
            if l_item_in_store is None:
                print(messages["PRODUCT_NOT_FOUND"] %(l_name))
                return

            l_quantity = input(messages["QUANTITY_INPUT"])
            if not self.validator.validate_not_negative_integer(l_quantity):
                print(messages["INVALID_INTEGER"] %(l_quantity))
                return

            l_quantity = int(l_quantity)

            if l_quantity > l_item_in_store.quantity:
                print(messages["STOCK_EXCEEDED"] %(l_name, l_item_in_store.quantity))
                return

            product_to_sell = Product(l_name, l_quantity, l_item_in_store.buy_price, l_item_in_store.sell_price)
            
            self.store.get_item(product_to_sell)

            self.registry.add_to_current_sale(product_to_sell)

            l_continue = input(messages["ADD_ANOTHER_PRODUCT_YES_NO"])

            if l_continue not in boolean_values:
                print(messages["INVALID_BOOLEAN"] %(','.join(boolean_values)))
            
            if boolean_values.index(l_continue) == 1:
                print(messages["SELL_FEEDBACK_HEADER"])
                print(self.registry.get_current_sale_report())
                print(messages["SELL_FEEDBACK_FOOTER"] %(self.registry.get_current_sale_gross_income()))

                return
