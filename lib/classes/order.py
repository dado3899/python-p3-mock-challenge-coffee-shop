
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)
        Order.all.append(self)

    def get_price(self):
        return self._price
    def set_price(self,value):
        if type(value) is int and 1 <= value <= 10:
            self._price = value
        else:
            raise Exception("Not valid price")
    price = property(get_price,set_price)

    def get_cust(self):
        return self._customer
    def set_cust(self,value):
        from classes.customer import Customer
        if type(value) is Customer:
            self._customer = value
        else:
            raise Exception("Not valid customer")
    customer = property(get_cust,set_cust)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self,value):
        from classes.coffee import Coffee
        if type(value) is Coffee:
            self._coffee = value
        else:
            raise Exception("Not valid coffee")
    coffee = property(get_coffee,set_coffee)