#How to compare two unordered lists in python

from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("is two list are equal", Counter(one) == Counter(two))

#How to check if all elements in a list are unique

def check_unique(list1):
    l = list(set(list1))
    if len(l) == len(list1):
        return True
    else:
        return False

listOne = [123, 345, 456, 23, 567]
print(check_unique(listOne))
listTwo = [123, 345, 567, 23, 567]
print(check_unique(listTwo))

#Convert Byte to String

byte_var1 = r"shalini"
byte_var2 = f"shalini"
byte_var3 = b"shalini"
print(byte_var1)
st = str(byte_var2.decode("utf-8"))
print(st)
