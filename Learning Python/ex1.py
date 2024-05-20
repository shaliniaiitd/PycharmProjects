#Class Inheritance and Method Overriding:

#Implement a class hierarchy for a zoo.
# Create a base class Animal with attributes like name and species.
# Then, create subclasses like Mammal, Bird, and Reptile with specific methods and properties.
# Demonstrate method overriding by implementing a sound() method in each subclass.

# class Animal():
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def sound(self):
#         print(f"This is {self.name}'s sound")
#
# class Mammal(Animal):
#     def __init__(self,name,species):
#         super().__init__(name,species)
#
#     def sound(self):
#         print(f"This is Mammal {self.name}'s  sound")
#
# animal = Animal("animal1","species1")
# mammal = Mammal("mammal", "Man")
#
# animal.sound()
# mammal.sound()
#
# Encapsulation and Getter/Setter Methods:
#
# Create a Student class with private attributes like name, age, and a public method to set and get the age.
# Implement getter and setter methods to encapsulate these attributes.

# class Student():
#     def __init__(self):
#         self.__name = ""
#         self.__age = 0
#
#     def get_set_age(self,age = "",):
#         if age == "":
#             return self.__age
#         else:
#             self.__age = age
#
# stud1 = Student()
# print(stud1.get_set_age())
# stud1.get_set_age(12)
# print(stud1.get_set_age())
#
# Multiple Inheritance:
#
# Define a base class Person with attributes like name and age.
# Create two subclasses, Employee and Student. Now, design a class Manager that inherits from both Employee and Student.
# Implement this multiple inheritance and demonstrate its usage.

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,person,role,salary, dept):
        super().__init__(person.name,person.age)
        self.dept = dept
        self.role = role
        self.salary = salary

class Student(Person):
    def __init__(self,person, dept):
        self.dept = dept
        super().__init__(person.name,person.age)

class Manager(Employee, Student):
    pass

#create an object of type manager
shalini = Person("shalini",45)
emp1 = Employee(shalini,"QA", 23000,"IT")
std1 = Student(shalini,"Physics")
mg1 = Manager(emp1,std1)

print(mg1.dept)



# Create a class representing a complex number.
# Implement methods for addition, subtraction, multiplication, and division of complex numbers using operator overloading.
# Test the class by performing various arithmetic operations on complex numbers.

# class Complex():
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#
#     def display(self):
#         print(f"{self.real} + i{self.img}")
#
#     def __add__(self, a):
#         real = self.real + a.real
#         img = self.img + a.img
#         return Complex(real,img)
#
# n1 = Complex(2,3)
# n2 = Complex(4,5)
#
# n1.display()
# n2.display()
#
# n3 = n1+n2
# n3.display()
#
# # Implement a class Temperature that stores temperature values in Celsius.
# # Write a decorator method that allows you to access the temperature value in Fahrenheit.
# # Implement getters and setters with decorators to convert between Celsius and Fahrenheit.
#
# class Temp():
#     def __init__(self,celsius):
#         self.celsius = celsius
# #Implement getters and setters with decorators suggests using property decorator
#     @property
#     def fahren(self):
#         return (self.celsius*9/5) + 32
#
#     @fahren.setter
#     def fahren(self,value):
#         self.celsius = (value -32)*5/9
#
# #desire usage is
#
# t = Temp(25)
# print(t.celsius) #25
# print(t.fahren)  #77
# t.fahren = 77
# print(t.fahren) #77
# print(t.celsius) #25
#
