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

           

