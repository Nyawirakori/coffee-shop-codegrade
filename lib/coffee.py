from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = [] #keep track of coffee orders

    #getter method
    @property
    def name(self):
        return self._name
    
    #setter method
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
       return list(set(order.customer for order in self.orders())) #returns instances of customers who have ordered that particular coffe

    def num_orders(self):
        return len(self.orders()) # no of times a particular coffe has been ordered

    def average_price(self):
        #Returns the average price of this coffee based on its orders.
        all_orders = self.orders()
        if not all_orders:
            return 0.0
        total_price = sum(order.price for order in all_orders)
        return total_price / len(all_orders)

    def __repr__(self):
        return f"Coffee(name={self.name})"


           

