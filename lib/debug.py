#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    new_cust = Customer("aaaaaaaaaaaaaaa")
    new_coffee = Coffee("Latte")
    # new_coffee.name = "Latte 2"
    new_order = Order(new_cust,new_coffee,5)
    new_orderw = Order(new_cust,new_coffee,5)
    print(new_cust.coffees())
    new_cust.create_order(new_coffee,10)
    print(new_cust.orders())
    print(new_coffee.num_orders())
    print(new_coffee.average_price())
    # ipdb.set_trace()
