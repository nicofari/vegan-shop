class Registry:
    def __init__(self):
        self.net_income = 0.0
        self.gross_income = 0.0

    def store_income(self, net_income, gross_income):
        self.net_income += net_income
        self.gross_income += gross_income

    
        
        