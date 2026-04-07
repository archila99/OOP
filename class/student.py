# class variables: shared among all 
# instances of class defined outside 
# the constructor allow you to share data among all objects 
# created that class

class Student:
    class_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alibek", 29)
student2= Student("Ahsen", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)

print(Student.class_year)
