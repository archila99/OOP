# inheritance = allows a class to inherit attributes and methods from another class 
# helps with code reusability and extensibility
# class Child(Parent)
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    

class Dog(Animal):
    def speak(self):
        print(f"My name is {self.name} and I am a dog.")

class Cat(Animal):
    def speak(self):
        print(f"My name is {self.name} and I am a cat.")

dog = Dog("Momo")
cat = Cat("Garfield")

# this methods is inherited from parent class 
dog.eat() 
cat.eat()

# this methods is added in children classes
dog.speak()
cat.speak()