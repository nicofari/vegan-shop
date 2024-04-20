from .base_command import BaseCommand
from resources.messages import MESSAGES

class IncomeListCommand(BaseCommand):

    def __init__(self, store, country_code, validator, registry):
        super().__init__(store, country_code, validator)

        self.registry = registry

    def run(self):
        messages = MESSAGES[self.country_code]

        print(messages["REVENUE_LINE"] %(self.registry.gross_income, self.registry.net_income))
        
