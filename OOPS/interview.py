import subprocess
#d = subprocess.Popen()


with  open('data', "a") as f :

    f.write("Agarwal")

aaa = {1: '111', 2: '222'}
# dict2 = {}
# # for key,value in aaa.items():
# #     dict2[value] = key

dict2 = {value:key for key,value in aaa.items()}
print(dict2)

import random
import string

def gen_ran_str(n):
    result = ""
    for _ in range(n):
        result += random.choice(string.ascii_letters)

    return result

print(gen_ran_str(3))

inpt = [1,2,3,4]
output = [(index,value) for index,value in enumerate(inpt) ]
print(output)

def tax_explainer(func):
    def inner(self):
        print("This is a tax calculator")
        return func(self)
    return inner

class Car:

    def __init__(self,model,c_owner,year,power):
        self.model = model
        self.c_owner = c_owner
        self.year = year
        self.power = power

    def __repr__(self):
        return (f"{self.c_owner}'s {self.model}")

    @property
    def owner(self):
        return self.c_owner

    @owner.setter
    def owner(self,owner):
        self.c_owner = owner

    @tax_explainer
    def tax(self):
        if self.power <75:
            tax = 100
        else:
            tax = 200
        return tax





car1 = Car("Toyota","shalini",2023,1234)
car1.owner = "new_owner"
print(car1.tax())















#
