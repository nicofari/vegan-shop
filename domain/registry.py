class Registry:
    def __init__(self):
        self.total_net_income = 0.0
        self.total_gross_income = 0.0
        self.current_sale = []

    def clear_current_sale(self):
        self.current_sale.clear()
    
    def add_to_current_sale(self, product):
        self.current_sale.append(product)
        self._store_income(product)
    
    def _store_income(self, product):
        self.total_net_income += product.get_net_income()
        self.total_gross_income += product.get_gross_income()

    def get_current_sale_net_income(self):
        return self._get_current_sale_net_income()

    def get_current_sale_gross_income(self):
        return self._get_current_sale_gross_income()

    def _get_current_sale_net_income(self):
        net_tot = 0.0
        for p in self.current_sale:
            net_tot += p.get_net_income()
        
        return net_tot
    
    def _get_current_sale_gross_income(self):
        gross_tot = 0.0
        for p in self.current_sale:
            gross_tot += p.get_gross_income()
        
        return gross_tot

    def get_current_sale_report(self):
        output = ''
        for p in self.current_sale:
            output += "- %d X %s: €%.2f\n" %(p.quantity, p.name, p.sell_price)

        return output
    