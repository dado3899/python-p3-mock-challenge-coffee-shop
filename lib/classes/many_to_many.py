class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 3 <= len(value) and not hasattr(self,"name"):
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)
        
    def orders(self):
        my_orders = []
        for order in Order.all:
            if order.coffee == self:
                my_orders.append(order)
        return my_orders
    
    def customers(self):
        my_customers=[]
        for order in Order.all:
            if order.coffee == self and order.customer not in my_customers:
                my_customers.append(order.customer)
        return my_customers
    
    def num_orders(self):
        my_orders = self.orders()
        return len(my_orders)
    
    def average_price(self):
        my_orders = self.orders()
        total = 0
        for order in my_orders:
            total = total + order.price
        return total/len(my_orders)



class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1 <= len(value) <=15:
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)
        
    def orders(self):
        my_orders = []
        for order in Order.all:
            if order.customer == self:
                my_orders.append(order)
        return my_orders
    
    def coffees(self):
        my_coffees = []
        for order in Order.all:
            if order.customer == self and order.coffee not in my_coffees:
                my_coffees.append(order.coffee)
        return my_coffees
    
    def create_order(self, coffee, price):
        return Order(
            customer=self,
            coffee=coffee,
            price=price
        )
    
    def count_customer_coffee(self,coffee):
        count = 0
        for order in Order.all:
            if order.customer == self and order.coffee == coffee:
                count+=1
        return count

    @classmethod
    def most_aficionado(cls, coffee):
        # loop through all the customers,
        currMax = 0
        currMaxCust = None
        for customer in Customer.all:
            # Count how many times they have ordered said coffee
            customer_count = customer.count_customer_coffee(coffee)
            # Keep track with the one with the highest
            if  customer_count > currMax:
                currMax = customer_count
                currMaxCust = customer
        return currMaxCust
    
    def __repr__(self):
        return self.name
        
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    def set_price(self,value):
        if type(value) is float and 1.0<=value <=10.0 and not hasattr(self,"price"):
            self._price = value
        else:
            print("Not valid price")
    price = property(get_price,set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self,value):
        if type(value) is Customer:
            self._customer = value
        else:
            print("Not valid customer")
    customer = property(get_customer,set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self,value):
        if type(value) is Coffee:
            self._coffee = value
        else:
            print("Not valid coffee")
    coffee = property(get_coffee,set_coffee)