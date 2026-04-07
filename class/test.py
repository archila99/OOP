# multiple inheritance = inherit from more than one parent class
# c(A, B)

# multilevel inheritence = inherit from a parent which inherits from another parent 
# C(B) <- B(A) <- A)

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name
    
class Prey(Animal):
    def flee(self):
        print(f"{self.describe()} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.describe()} is hunting.")
    
class Rabbit(Prey):
    def __init__(self, name, skin):
        super().__init__(name)
        self.skin = skin
    
    def describe(self):
        return f"{self.skin} {super().describe()}"


class Lion(Predator):
    def __init__(self, name, sex):
        super().__init__(name)
        self.sex = sex
    
    def describe(self):
        return f"{self.sex} {self.name}"


class Creature(Prey, Predator):
    pass


rabbit = Rabbit("Rabbit", "Puffy")
lion = Lion("Lion", "Male")
creature = Creature("Alien")

rabbit.flee()
lion.hunt()

creature.hunt()
creature.flee()