import abc
class Car:
    def Car():
        print ("This is the Base Class Car")
    @abc.abstractmethod
    def show_details(self):
        print("This calls the base class")
        
class Maruti(Car):
    def Maruti():
        print("This is the Sub Class Maruti")
    def show_details(self) :
        print ("You are in Sub Class - 1 ")
class Santro(Car):
    def Santro():
        print("This is the Sub Class Santro")
    #def show_details(self) :
    #   print ("You are in Sub Class - 2 ")

m = Maruti()
s = Santro()
m.show_details()
s.show_details()
