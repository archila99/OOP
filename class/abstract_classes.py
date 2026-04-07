# abstract class: a class that cannot be instantiated on its own; meant to be subclassed.
# they can contain abstract methods, which are declared but have no implementation.
# abstract classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Requirec children to use inherited abstract mehtods 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    pass

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle.")
    
    def stop(self):
        print("You stop the motorcycle.")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat.")

    def stop(self):
        print("You stop the boat.")

    def horn(self):
        print("You horn.")

car = Car()
motor = Motorcycle()
boat = Boat()

car.stop()
car.go()

motor.stop()
motor.go()

boat.go()
boat.stop()
boat.horn()




