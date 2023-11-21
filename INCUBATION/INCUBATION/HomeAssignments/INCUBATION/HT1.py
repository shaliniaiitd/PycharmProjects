import builtins
import math
# #1. Predict Output,
# S1 = "Hello"
# S2 = "This is Python"
# print(len(S1), len(S2))
#
# # Ans - 5,14
#
#
#
# #2. WAP to input a string and print its length.
# s = input("Please input a string")
# print(len(s))

#3. WAP to input 2 numbers and print their sum and difference.
# a=int(input("please input a number"))
# b=int(input("please input another number"))

#print(f"sum of {a} and {b} = {a+b}, difference of {a} and {b} = {a-b}")

# 4. Predict Output,
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)
#ANs - 'abde'

# 5. Predict Output,
s1 = 'ab' *4
print(s1)
# Ans - abababab

# 6. WAP to input a string s and a number n. Print the string n times on the screen,
#    each should appear in a separate line (do not use any kind of loops, use the multiplication operator).
# s = input("Please input a string")
# n = int(input("Please input a number"))
#
# print(s*n)

# 7. Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))
# ANS - \
# Hello
# This is India
# str - <class-str>
#19


# 8. Find the name of function to find the square root. (see all the options available in dir() of builtins)
n = 9
print(math.sqrt(9))
print(dir(builtins)) # no options

# 9. WAP to input a number and print its square root ().

n = int(input("Input a number"))
print(math.sqrt(n))

# 10. WAP to input 4 numbers from user and print their average

# 11. Use the help function to check what the abs function in python does.
print(help(abs))

# 12. What is the output of this code when run from python interpreter.
# 	print(__name__)
# should be __main__