#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    cu1 = Customer(name="Grey")
    cu2 = Customer(name="Ben")
    cu3 = Customer(name="Justin")
    co1 = Coffee(name="Latte")
    co2 = Coffee(name="Black")
    co3 = Coffee(name="Pumpkin Spice")
    # co1.name = "Latte 2"

    Order(cu1,co2,5.50)
    Order(cu1,co2,5.25)
    Order(cu1,co2,5.00)
    Order(cu1,co2,5.00)

    Order(cu2,co1,7.50)
    Order(cu2,co2,5.50)
    Order(cu2,co3,10.0)

    Order(cu3,co3,10.0)
    Order(cu3,co3,10.0)
    Order(cu3,co3,10.0)
    o1 = Order(cu3,co3,10.0)
    # o1.price = 5.25
    # cu3.create_order(co2,5.50)
    # print("Printing Price", o1.price)
    print(Customer.most_aficionado(co3).name)
    # print(len(cu3.orders()))
    # print(len(cu2.coffees()))
