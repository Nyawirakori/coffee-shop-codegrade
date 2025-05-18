#This file is for testing
from customer import Customer
from coffee import Coffee
from order import Order


c1 = Customer("Jojo")
c2 = Customer("Kori")
white = Coffee("White coffee")
iced = Coffee("Iced coffee")


c1.create_order(iced, 3.5)
c1.create_order(white, 4.0)
c2.create_order(iced, 4.5)


print(c1.orders())
print(c1.coffees())
print(iced.orders())
print(iced.customers())
print(iced.num_orders())
print(iced.average_price())
print(Customer.most_aficionado(iced)) 