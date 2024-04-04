class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        r_l = []
        for order in Order.all:
            if order.coffee is self:
                r_l.append(order)
        return r_l
    
    def customers(self):
        r_l = []
        for order in Order.all:
            if order.coffee is self and order.customer not in r_l:
                r_l.append(order.customer)
        return r_l
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        my_orders = self.orders()
        if len(my_orders) == 0:
            return 0
        total = 0
        for order in my_orders:
            total+=order.price
        return total/len(my_orders)

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 3<=len(value) and not hasattr(self,"name"):
            self._name = value
        else:
            print("Not valid name")
            # raise ValueError("Not valid name or name cannot be changed")
    name = property(get_name,set_name)

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        # [Return for loop, if statement]
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        r_l = []
        for order in Order.all:
            if order.customer is self and order.coffee not in r_l:
                r_l.append(order.coffee)
        return r_l

    
    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
    @classmethod
    def most_aficionado(cls,coffee):
        all_orders = coffee.orders()
        cust_payout = {}
        for order in all_orders:
            if order.customer in cust_payout:
                # If customer is in
                cust_payout[order.customer] += order.price
            else:
                cust_payout[order.customer] = order.price
        
        maxVal = 0
        maxCust = None
        print(cust_payout)
        for cust in cust_payout:
            if cust_payout[cust] > maxVal:
                maxVal = cust_payout[cust]
                maxCust = cust
        return maxCust


    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else:
            print("Not valid name")
            # raise ValueError("Not valid name")
    name = property(get_name,set_name)

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
        if type(value) is float and 1.0<=value<=10.0:
            if not hasattr(self,"price"):
                self._price = value
            else:
                print("Cannot change price")
                # raise ValueError("Cannot change the price")
        else:
            print("Not valid price")
            # raise ValueError("Not valid price")
    price = property(get_price,set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self,value):
        if type(value) is Customer:
            self._customer = value
        else:
            print("Not valid customer")
            # raise ValueError("Not valid customer")
    customer = property(get_customer,set_customer)
    def get_coffee(self):
        return self._coffee
    def set_coffee(self,value):
        if type(value) is Coffee:
            self._coffee = value
        else:
            print("Not valid coffee")
            # raise ValueError("Not valid coffee")
    coffee = property(get_coffee,set_coffee)

    def __repr__(self):
        return f"{self.coffee.name} ordered by {self.customer.name} for {self.price}"