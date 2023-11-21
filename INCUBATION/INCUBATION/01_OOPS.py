# 1.	Find Output of following:
class Student:
    pass
s = Student()
s.name="Guido"
s.age=62
print(s.name)
print(s.age)


class Student:
    pass
s1 = Student()
s1.name="Guido"
s1.age=62
s2 = Student()
s2.name="Bjarne"
s2.age=67
print(s1.name, s1.age)
print(s2.name, s2.age)
# 2.	For the Student class in above example, add constructor with 2 arguments for name and age, to set the name and age attributes. Create a student object, initialize it with some values and print its attributes.


class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("name1", 14)

s2 = Student("name2", 28)

print(s1.name,s1.age)
print(s2.name,s2.age)

#Class variable

class Student():
    class_name = "English"

    def __init__(self):
        self.name = 'student_name'

s3 = Student()

#Print class variable
print(Student.class_name)
print(s3.__class__.class_name)

#set instance variable name
s3.name = "my_name"
print(s3.name)

# 3.	Find Output Again:

# class Test:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
# s1 = Test()   #constructor, destructor
# s2 = Test ()  #constructor, destructor
#

class Test:
    def __init__(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")
s1 = Test() #constructor
Test()      #constructor, destructor
s2 = Test() #constructor, destructor
s3 = s1
del(s1)     # destructor
# 4.	Add a method set_marks(marks_ list), that takes a list of marks in 5 subjects and stores in a
# new attribute marks. Also add a method print_details(), to student class to print average of marks and all details of student.
# (Hint : average will be calculated as (total marks)/5 )
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Constructor")
    def __del__(self):
        print("Destructor")

    def set_marks(self,marks_list):
        self.marks = marks_list

    def print_details(self):
        score = 0
        for mark in self.marks:
            score = score + mark
        av_score = score/5
        print(av_score)

#Test your class against the following code:
if __name__ == "__main__":
    s = Student("abc", 20)
    s.set_marks([80,60,90,70,99])
    s.print_details()


# 5. Create a class Circle, that stores the radius and contains 2 methods:
# get_area, get_perimeter, which give the area and perimeter respectively of the circle.

class Circle():
    pi = 3.14
    def __init__(self,radius):
        self.radius = int(radius)

    def get_area(self):
        return (self.pi*self.radius*self.radius)

    def get_perimeter(self):
        return(2*self.pi*self.radius)

#TEST
c = Circle(7)
print(c.get_area(),c.get_perimeter())


# 6. Create a class SelfManaged such that it keeps track of the number of objects currently alive.
# Create a class method get_current_count(), that gives the number of objects currently alive in
# memory.

class SelfManaged():
    object_count = 0

    def __init__(self):
            #We should change the class variable’s value using the class name only.
        SelfManaged.object_count = SelfManaged.object_count + 1
        #print(SelfManaged.object_count)
        #Because if we try to change the class variable’s value by using an object,
        # a new instance variable is created for that particular object, which shadows the class variables.
    def __del__(self):
        pass
        #SelfManaged.object_count = SelfManaged.object_count - 1

    @classmethod
    def get_current_count(cls):
        return cls.object_count

obj = SelfManaged()
count = SelfManaged.get_current_count()
print(count)
obj1 = SelfManaged()
count = SelfManaged.get_current_count()
print(count)


# [Hint: use a class attribute to keep count of number of objects and use __init__ and __del__
# methods to update the value of count count]
# 7. Create a class BankAccount, which contains attributes balance and name, and methods
# deposit() and withdraw(), to add and deposit some money in account.
# the balance should be set to 0 in the constructor, and withdrawal should be allowed only if
# sufficient balance is there. Also overload the str method to allow printing the details directly.
#
class BankAccount():
    def __init__(self,name):
        self.balance = 0
        self.name = name

    def deposit(self,amount):
        self.balance =+ amount

    def withdraw(self, amount):
            if amount > self.balance:
                raise Exception( "amount exceeds balance")
            else:
                self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

ac = BankAccount("shalini")
ac.deposit(500)
print(ac.get_balance())
ac.withdraw(300)
print(ac.get_balance())

#ENCAPSULATION

#PROTECTED
# defined: using _variable_name
# access: can be accessed and modified by object of the class and its derived class,
# but as a good practise should not be modified by derived class.
# 



