import abc

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
    
    def __str__(self):
        return "Make: " + self.make + ", Model: " + self.model + ", Price: " + str(self.price)

    @abc.abstractmethod
    def show_details(self):
        print("This calls the base class")

class Maruti(Car):
    def __init__(self, model, price):
        Car.__init__(self, "Maruti", model, price)
    
    def __str__(self):
        return super(Maruti, self).__str__()

    def show_details(self) :
        print ("You are in Sub Class - 1 ")

class Santro(Car):
    def __init__(self, model, price):
        Car.__init__(self, "Hyundai", model, price)

    def __str__(self):
        return super(Santro, self).__str__()
    
    def show_details(self) :
        print ("You are in Sub Class - 2")

maruti = Maruti("WagonR", 4500000)
santro = Santro("Santro", 3500000)

print(maruti)
print(santro)

maruti.show_details()
santro.show_details()