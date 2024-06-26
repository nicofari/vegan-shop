import json
from domain.store import Store
from domain.product import Product

class JsonStorage:
    """Serialize/deserialize Store instances to/from json"""
    """see https://stackoverflow.com/questions/70525815/json-serialization-of-dictionary-with-complex-objects for tech details"""
    
    @staticmethod
    def write(store, file_name):
        with open(file_name, "w") as output:
            newdict = {i:j.__dict__ for i,j in store.store.items()}
            json.dump(newdict, output)

    @staticmethod
    def read(file_name):
        try:
            with open(file_name, "r") as input:
                d = json.load(input)
                store = {}
                for k, v in d.items():
                    item = Product('', 0, 0.0, 0.0)
                    item.__dict__.update(v)
                    store[item.name] = item

                return Store(store)
        except FileNotFoundError:
            return Store()        
