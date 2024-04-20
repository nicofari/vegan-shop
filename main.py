from console_app import ConsoleApp
from domain.store import Store
from services.validator import Validator
from commands.add_item_command import AddItemCommand
from commands.list_command import ListCommand

def main():
    store = Store()
    country_code = 'it'
    validator = Validator()

    console_app = ConsoleApp(
        store, 
        country_code, 
        AddItemCommand(store, country_code, validator),
        ListCommand(store, country_code, validator)
    )

    console_app.run()

if __name__ == '__main__':
    main()