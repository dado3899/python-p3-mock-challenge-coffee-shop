class Coffee:
    all =[]

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
        
    def orders(self):
        # ndfjaipfndiadfsnjf
        # return [Order(),Order()]
        # coffee.customer
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        # IF ORDERS IS WORKING I"D DO THIS
        # Find all of our orders (self.orders)
        # count them
        # len(self.orders())
        return len(self.orders())
    
    def average_price(self):
        # IF ORDERS IS WORKING
        sum = 0
        # Orders is a list of orders
        for order in self.orders():
            sum = sum + order.price 
        return sum/len(self.orders())

    def get_name(self):
        return self._name
    def set_name(self, value):
        print(1<len(value)<15)
        if type(value) is str and 1<len(value)<15:
            self._name = value
        else:
            print("NOT VALID NAME")
    name = property(get_name,set_name)
    

    
latte = Coffee("Latte")
lette2 = Coffee("Latte2")

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        for order in Order.all:
            if order.customer is self:
                pass
        pass
    
    def coffees(self):
        reciepts = []
        # I'll look through all the orders
        # I'll check every order and see if the customer is the same as myself
        # Then I'll check if the coffeee for that one order is in my pile of reciepts
        # If it is, do nothing, if it isn't add that coffee to that list 
        for x in Order.all:
            if x.customer is self and x.coffee not in reciepts:
                reciepts.append(x.coffee)
            else:
                pass
        return reciepts
        pass
    
    def create_order(self, coffee, price):
        # customer, coffee, price
        return Order(self, coffee, price)
        pass
    
    @classmethod
    def most_aficionado(cls, coffee_to_check):
        # GO THROUGH ALL THE ORDERS
        # Check if that coffee is the order/ or use coffee.orders()
        # Save customer and order count together (dictionary)
        # see max
        # option 2
        # GO THROUGH ALL THE CUSTOMERS
        # CALL CUSTOMER.orders
        # Filter that array down to just this coffee
        # Check length
        curr_max_count = 0
        curr_max_cust = None
        for curr_customer in Customer.all:
            this_cust_orders = curr_customer.order()
            count = 0
            for order in this_cust_orders:
                if order.coffee is coffee_to_check:
                    count +=1
            if curr_max_count < count:
                curr_max_count = count
                curr_max_cust = curr_customer
        return curr_max_cust
        
            
                
        pass
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # self.customer = "Value"
        Order.all.append(self)
    
    
    def get_customer(self):
        return self._customer
    def set_customer(self, value):
        if type(value) is Customer:
            self._customer = value
        else:
            print("NOT VALID CUSTOMER")
    customer = property(get_customer,set_customer)