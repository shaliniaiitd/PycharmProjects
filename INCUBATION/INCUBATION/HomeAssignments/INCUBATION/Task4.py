# 1. Write a for loop to print numbers from 1 to 10. All numbers should be in separate lines.
import random

for i in range(1,11):
    print(i)

# 2. Write a for loop to print numbers from 10 to 1. All numbers should be in separate lines.
for i in range(10,0,-1):
    print(i)

# 3. Print Elements at Odd indexes from a list (Using for loop)
l = [10,11,20, 21,30, 31, 40, 41]
print(l[1::2])

# 4. Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
# a for loop.
l = []
sum = 0
for _ in range(5):
    num = random.randint(1,100)
    #l.append(random.random())
    l.append(num)
    sum =+ num
avg = sum/5
print(l,sum,avg)

# 5. WAP to input a string and print individual characters in the string using for loop.
inpt = input("please eneter a string")

for el in inpt:
    print(el)

# 6. WAP to input a string and print the ASCII value of each character in the string.
inpt = input("please eneter a string")

for el in inpt:
    print(f"Ascii value for character {el} is {ord(el)}")  # chr(ascii) gives string output

# 7. WAP to input a string and store ASCII values of all characters in a tuple.
inpt = input("please eneter a string")
result = ()
for el in inpt:
    result = result + (ord(el),)
print(result)

# 8. Write a function that takes a list of numbers from user as argument and returns the sum of only
# odd numbers (Use only for loop. No need to use if statement).
l = input("please enter a list of numbers")
sum = 0
for num in l:
    sum = sum + int(num)*(int(num)%2)

print(f"sum of odd numbers = {sum}")

# 9. WAP to input a list of numbers and store in a tuple. Now input another number and print the
# index of this number in the tuple.
import sys

l = sys.argv[1]
t = tuple(l)
print(t)
n = input("Input a number")
print(t.index(n))

# 10. WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
# 11. Update the above program to also print the sum of numbers.
sum = 0
li = []
for _ in range(10):
    num = input("enter a number repeatedly")
    sum = sum + int(num)
    li.append(num)
print(li, "sum=", sum)

# 12. WAP to input a number and print all numbers from 1 till that number
m = input("enter a number")
for i in range(1,int(m)+1):
    print(i)

# 13. WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
#     whose factorial is to be found.
#         Ex: if n = 4 output should be 24
#         4! = 1x2x3x4 = 24

n = input("Factorial of which number:")
fact = 1
for i in range(2,int(n)+1):
    fact = fact* i
print(fact)