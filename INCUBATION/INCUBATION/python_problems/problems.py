#Write a Python code to find the maximum of two numbers.
#
# import sys
#
# print(type(sys.argv))
#
# a = sys.argv[1]
# b = sys.argv[2]
#
# print(a if a>b else b)

#print(a,b)

#Write a Python code to check prime numbers.

a = int(input("Please enter a number"))

for i in range(2,a):
    if a%i ==0 :
        print(f"{a} is not prime")
        break
else:
    print(f"{a} is Prime")

#Write a Python factorial program without using if-else, for, and ternary operators.
def fact (n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

#How to convert a list into a string?
li = [1,2,3,4]
print(tuple(li))
str1 = ''
li = [str(el) for el in li]
str1 = "".join(li)
print(str1)
print(fact(5))

#How to convert a list into a tuple?
print(tuple(li))