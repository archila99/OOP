class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"I am {self.name} and I am {self.age} years old"
        


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    
    def show(self):
        return f"I am {self.name} and I am {self.age} years old and my color {self.color}"


    def speak():
        print("bark")

class Cat(Pet):
    def speak(self):
        print("Meov")


d = Dog("Fozz", 2, "Dark")
print(d.show())

