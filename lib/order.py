class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    #customer instance
    @property
    def customer(self):
        return self._customer
    
    #customer setter instance
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("customer must be a Customer instance.")

    #coffee instance
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("coffee must be a Coffee instance.")
        
      #price getter method
    @property
    def price(self):
        return self._price
    
    #price setter method
    @price.setter
    def price(self, value):
        if not isinstance(value, float) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = value

    def __repr__(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"






