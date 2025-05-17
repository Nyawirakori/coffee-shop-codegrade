class Coffee:
    def __init__(self, name):
        self.name = name

    #getter method
    @property
    def name(self):
        return self._name
    
    #setter method
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and  len(name) < 3:
            raise ValueError("Name must be string between 1 and 15 characters.")
        self._name = name

    def orders(self):
        pass

    def customers(self):
        pass

    def num_orders(self):
        pass

    def average_price(self):
        pass


           

