class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, person_obj, role, salary, dept):
        super().__init__(person_obj.name, person_obj.age)
        self.dept = dept
        self.role = role
        self.salary = salary

# Create a Person object
shalini = Person("Shalini", 45)

# Create an Employee object using the shalini Person object
emp1 = Employee(shalini, "QA", 23000, "IT")

# Accessing attributes of the Employee object
print(emp1.name)   # Output: Shalini
print(emp1.age)    # Output: 45
print(emp1.role)   # Output: QA
print(emp1.salary) # Output: 23000
print(emp1.dept)   # Output: IT

class Student(Person):
    def __init__(self,person, dept):
        self.dept = dept
        super().__init__(person.name,person.age)

stud1 = Student(shalini,"Physics")
print(stud1.age)    # Output: 45
print(stud1.dept)   # Output: Physics

class Manager(Employee,Student):
    def __init__(self,emp,stud):
        Employee.__init__(self,emp,emp.role,emp.salary,emp.dept)
        Student.__init__(self,stud,stud.dept)

mg1 = Manager(emp1,stud1)
print(mg1.name)



# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
# class Class4(Class2, Class3):
#     pass


# obj = Class4()
# obj.m()