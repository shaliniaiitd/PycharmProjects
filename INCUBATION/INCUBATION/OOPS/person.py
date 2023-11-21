#single inheritance
import sys


class Person():
    def __init__(self,name,age, func1="default"):
        self.name = name
        self.age = age
        self._func1 = func1

    @property
    def func1(self):
        return self._func1

    @func1.setter
    def func1(self,val):
        self._func1 = val

    @func1.deleter
    def func1(self):
        print("DELETING")
        del(self._func1)


person1 = Person("p1",67)

print("func1=", person1.func1)
person1.func1 = "something"
print("func1=", person1.func1)
del(person1.func1)
#print("func1=", person1.func1)

class Employee(Person):
    count = 0
    def __init__(self,name,role, dept):
        self.count += self.count
        self.emp_id = self.count
        super().__init__(name)


emp1 = Employee("emp1",9)
print(emp1.emp_id)

if __name__ == "__main__":
    person = Person(sys.argv[1],sys.argv[2])
    print(f"person created with name {person.name} and age {person.age}" )


