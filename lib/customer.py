from order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        
    #getter method
    @property
    def name(self):
        return self._name
    
    #setter method
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 15 characters.")
        
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        #Returns a unique list of Coffee instances that the customer has ordered.
        return list(set(order.coffee for order in self.orders()))

        
    def create_order(self,coffee,price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_spending[order.customer] = (
                customer_spending.get(order.customer, 0) + order.price)
        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None

    def __repr__(self):
        return f"Customer(name={self.name})"

