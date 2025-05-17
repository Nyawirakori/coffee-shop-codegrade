class Order:
    list_of_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    #price getter method
    @property
    def price(self):
        return self._price
    
    #price setter method
    def price(self, value):
        if not isinstance(value, float) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = value

    #customer instance
    @property
    def customer(self):
        from customer import Customer

    




