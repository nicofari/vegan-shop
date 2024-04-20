from console_app import ConsoleApp
from domain.store import Store
from commands.add_item_command import AddItemCommand

def main():
    store = Store()
    country_code = 'it'
    
    console_app = ConsoleApp(
        store, 
        country_code, 
        AddItemCommand(store, country_code)
    )

    console_app.run()

if __name__ == '__main__':
    main()