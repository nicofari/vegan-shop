SUPPORTED_LANGUAGES = ["it", "en"]

MESSAGES = {
    "it": {
        "COMMAND_PROMPT": "Inserisci un comando: ",
        "UNRECOGNIZED_COMMAND": "Comando non valido [%s]. I comandi disponibili sono [%s]",

        "PRODUCT_NAME_INPUT": "Nome del prodotto (<INVIO> per tornare indietro): ",
        "QUANTITY_INPUT": "Quantità: ",
        "BUY_PRICE_INPUT": "Prezzo di acquisto: ",
        "SELL_PRICE_INPUT": "Prezzo di vendita: ",

        "INVALID_STRING": "Input non valido: sono accettati solo spazi e numeri o lettere",
        "INVALID_INTEGER": "[%s] non è un intero valido",
        "INVALID_FLOAT": "[%s] non è un numero decimale valido",
        "INVALID_BOOLEAN": "Scelta non valida. I valori possibili sono [%s]",

        "INSERT_SUCCESSFUL_FEEDBACK": "AGGIUNTO %d X %s",
        "SELL_FEEDBACK_HEADER": "VENDITA REGISTRATA",
        "SELL_FEEDBACK_FOOTER": "Totale: €%.2f",

        "STORE_LIST_HEADER": "PRODOTTO QUANTITÀ PREZZO",
        "PRODUCT_NOT_FOUND": "Il prodotto [%s] non è presente in magazzino",
        "STOCK_EXCEEDED": "Il prodotto [%s] è disponibile solo in [%s] unità",
        "ADD_ANOTHER_PRODUCT_YES_NO": "Aggiungere un altro prodotto? (si/no)",

        "REVENUE_LINE": "Profitto: lordo=€%.2f netto=€%.2f",

        "COMMAND_HELP": """
I comandi disponibili sono i seguenti:
- aggiungi: aggiungi un prodotto al magazzino
- elenca: elenca i prodotto in magazzino
- vendita: registra una vendita effettuata
- profitti: mostra i profitti totali
- aiuto: mostra i possibili comandi
- chiudi: esci dal programma
"""
    },
    "en": {
        "COMMAND_PROMPT": "Insert command: ",
        "UNRECOGNIZED_COMMAND": "Unknown command [%s]. Available commands are [%s]",

        "PRODUCT_NAME_INPUT": "Product name (ENTER to go back): ",
        "QUANTITY_INPUT": "Amount: ",
        "BUY_PRICE_INPUT": "Buy price: ",
        "SELL_PRICE_INPUT": "Sell price: ",

        "INVALID_STRING": "Invalid input: alphanumeric characters only are allowed",
        "INVALID_INTEGER": "[%s] is not a valid integer value",
        "INVALID_FLOAT": "[%s] is not a valid float value",
        "INVALID_BOOLEAN": "Invalid choice: valid input are [%s]",

        "INSERT_SUCCESSFUL_FEEDBACK": "ADDED %d X %s",
        
        "SELL_FEEDBACK_HEADER": "SELL RECORDED",
        "SELL_FEEDBACK_FOOTER": "Total: €%.2f",

        "STORE_LIST_HEADER": "PRODUCT QUANTITY PRICE",
        "PRODUCT_NOT_FOUND": "Product [%s] is not present",
        "STOCK_EXCEEDED": "Product [%s] has [%s] items only in stock",
        "ADD_ANOTHER_PRODUCT_YES_NO": "Aggiungere un altro prodotto? (si/no)",

        "REVENUE_LINE": "Revenue: gross=€%.2f net=€%.2f",

        "COMMAND_HELP": """
Available commands:
- insert: add a new item to the store
- list: list store's content
- sell: sell an item
- revenue: show current revenue
- help: print this message
- exit: close the program
"""
    }
}

BOOLEAN_VALUES = {
    "it": ["si", "no"],
    "en": ["yes", "no"]
}