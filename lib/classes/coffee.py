class Coffee:
    def __init__(self, name):
        self._name = name
        self.all_orders = []
        self.all_customer = []

    def get_name(self):
        return self._name
    def set_name(self,value):
        raise Exception("Cannot change name")
    name = property(get_name,set_name)


    def orders(self, new_order=None):
        from classes.order import Order
        if type(new_order) is Order:
            self.all_orders.append(new_order)
        return self.all_orders

    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if type(new_customer) is Customer and new_customer not in self.all_customer:
            self.all_customer.append(new_customer)
        return self.all_customer
    
    def num_orders(self):
        all_orders = self.orders()
        return len(all_orders)
    
    def average_price(self):
        sum = 0
        for order in self.all_orders:
            sum += order.price
        return sum/self.num_orders()