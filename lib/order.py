class Order:

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
        return self._customer
    
    #customer setter instance
    @customer.setter
    def customer(self, new_customer):
        from customer import Customer
        if not isinstance(new_customer, Customer):
            raise ValueError("customer must be a Customer instance.")
        self._customer = new_customer

    #coffee instance
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from coffee import Coffee
        if not isinstance(new_coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        self._coffee = new_coffee






