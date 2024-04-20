from resources.messages import MESSAGES

class ConsoleApp:
    COMMANDS = {
        "it": ["aggiungi", "elenca", "chiudi"],
        "en": ["insert", "list", "exit"]
    }

    INSERT_COMMAND_INDEX = 0
    LIST_COMMAND_INDEX = 1

    def __init__(
            self, 
            store, 
            country_code,
            add_item_command,
            list_command
        ):
        self.store = store
        self.country_code = country_code
        self.add_item_command = add_item_command
        self.list_command = list_command

    def run(self):
        messages = MESSAGES[self.country_code]
        commands = self.COMMANDS[self.country_code]

        while (True):
            cmd = input(messages["COMMAND_PROMPT"])
            if cmd not in commands:
                print(messages["UNRECOGNIZED_COMMAND"] %(cmd, ','.join(commands)))
            else:
                cmd_index = commands.index(cmd)
                match cmd_index:
                    case self.INSERT_COMMAND_INDEX:
                        self.add_item_command.run()
                    
                    case self.LIST_COMMAND_INDEX:
                        self.list_command.run()

        