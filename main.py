import sys

from console_app import ConsoleApp
from domain.store import Store
from services.json_storage import JsonStorage
from services.validator import Validator
from commands.add_item_command import AddItemCommand
from commands.list_command import ListCommand
from commands.sell_command import SellCommand
from domain.registry import Registry
from commands.income_list_command import IncomeListCommand
from resources.messages import SUPPORTED_LANGUAGES

def main():
    data_file = sys.argv[1]
    country_code = sys.argv[2]

    if country_code not in SUPPORTED_LANGUAGES:
        print("%s is not supported: available languages are %s" %(country_code, ','.join(SUPPORTED_LANGUAGES)))
        return

    store = JsonStorage.read(data_file)
    validator = Validator()
    registry = Registry()

    console_app = ConsoleApp(
        store, 
        country_code, 
        AddItemCommand(store, country_code, validator),
        ListCommand(store, country_code, validator),
        SellCommand(store, country_code, validator, registry),
        IncomeListCommand(store, country_code, validator, registry)
    )

    console_app.run()

    JsonStorage.write(store, data_file)

if __name__ == '__main__':
    main()