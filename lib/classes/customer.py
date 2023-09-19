class Customer:
    def __init__(self, name):
        self.name = name
        self.all_orders = []
        self.all_coffee = []
        
    def orders(self, new_order=None):
        from classes.order import Order
        if type(new_order) is Order:
            self.all_orders.append(new_order)
        return self.all_orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if type(new_coffee) is Coffee and new_coffee not in self.all_coffee:
            self.all_coffee.append(new_coffee)
        return self.all_coffee

    def create_order(self,coffee,price):
        from classes.order import Order
        Order(self,coffee,price)

    def get_name(self):
        return self._name
    def set_name(self,value):
        print(type(value))
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Not valid customer name")
    name = property(get_name,set_name)