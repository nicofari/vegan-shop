from .base_command import BaseCommand
from resources.messages import MESSAGES

class ListCommand(BaseCommand):

    def run(self):
        messages = MESSAGES[self.country_code]

        print(self.store.list(messages["STORE_LIST_HEADER"]))
