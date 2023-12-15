class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        rlist = []
        for order in Order.all:
            if type(order) is Order and order.coffee is self:
                rlist.append(order)
        return rlist
    
    def customers(self):
        rlist = []
        for our_order in self.orders():
            if our_order.customer not in rlist:
                rlist.append(our_order.customer)
        return rlist
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        sum = 0
        for our_orders in self.orders():
            sum+=our_orders.price
        return sum/self.num_orders()

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 3<=len(value) and not hasattr(self,"name"):
            self._name = value
        else:
            print("Not valid coffee name")
    name = property(get_name,set_name)

    def __repr__(self):
        return f"Coffee Name: {self.name}"

class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        rlist = []
        for order in Order.all:
            if type(order) is Order and order.customer is self:
                rlist.append(order)
        return rlist
    
    def coffees(self):
        rlist = []
        for our_order in self.orders():
            if our_order.coffee not in rlist:
                rlist.append(our_order.coffee)
        return rlist
    
    def create_order(self, coffee, price):
        # Order(c1,latte,9.8)
        # new_order = Order(self,coffee,price)
        return Order(self,coffee,price)

    @classmethod
    def most_aficionado(cls,coffee):
        # loop through coffee orders
        robj = {}
        for order in coffee.orders():
        # check if customer count starter
            # if customer count has started, add price to the sum
            if order.customer in robj:
                robj[order.customer] += order.price
            # if not initialize that customer
            else:
                robj[order.customer] = order.price
        largest_amount = 0
        afficianado = None
        for key in robj:
            if robj[key] > largest_amount:
                largest_amount = robj[key]
                afficianado = key
        return afficianado


    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else:
            print("Not valid customer name")
    name = property(get_name,set_name)

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
        # print(f"inputted Value: {value}")
        if (type(value) is float or type(value) is int) and 1.0<=value<=10.0 and not hasattr(self, "price"):
            self._price = value
        else:
            print("Not valid price")
    price = property(get_price,set_price)


    def get_customer(self):
        return self._customer
    def set_customer(self,value):
        if type(value) is Customer:
            self._customer= value
        else:
            print("not valid customer")
    customer = property(get_customer,set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self,value):
        if type(value) is Coffee:
            self._coffee=value
        else:
            print("not valid coffee")
    coffee = property(get_coffee,set_coffee)




# test = {"a":1,"b":2}
# print("c" in test)
c1 = Customer("John")
c2 = Customer("Bob")
latte = Coffee("Latte")
black = Coffee("Black")

o1 = Order(c1,latte,9.8)
o2 = Order(c1,latte,3.8)
o3 = Order(c1,latte,5.8)
o3 = Order(c2,latte,6.8)
# print((9.8+3.8+5.8+6.8)/4)
c1.create_order(black,2.50)
print(Customer.most_aficionado(latte).name)
# print(c1.coffees())
# print(black.num_orders())
# print(latte.average_price())
# print(type(c1))
# print(latte.customers())
# print(c1.coffees()) 
# o1.price = 5.6
# latte.name = "New Latte"
# print(latte.name)
# print(hasattr(latte, name))