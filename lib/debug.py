#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Black")
    coffee3 = Coffee("Expresso")
    coffee4 = Coffee("Cappucino")
    # coffee1._name = "Latte2"

    cust1 = Customer("Sam")
    cust2 = Customer("Zac")
    cust3 = Customer("Sab")
    
    Order(cust1,coffee2, 1.50)
    Order(cust1,coffee2, 1.50)
    Order(cust1,coffee2, 1.50)
    Order(cust3,coffee1, 4.50)
    Order(cust3,coffee1, 4.50)
    Order(cust3,coffee1, 2.50)
    Order(cust3,coffee2, 1.50)
    Order(cust3,coffee1, 4.50)
    Order(cust2,coffee3, 3.50)
    Order(cust2,coffee3, 3.50)
    Order(cust2,coffee3, 3.50)
    Order(cust2,coffee2, 1.50)
    # print(Order.all)
    # print(coffee1.customers())
    cust2.create_order(coffee2, 1.0)
    # print(cust2.orders())
    # print(cust2.coffees())
    # print(coffee4.num_orders())
    # print(coffee4.average_price())
    # print(coffee2.average_price())
    print(Customer.most_aficionado(coffee2))
    # o1.price = 4.50

    # ipdb.set_trace()
