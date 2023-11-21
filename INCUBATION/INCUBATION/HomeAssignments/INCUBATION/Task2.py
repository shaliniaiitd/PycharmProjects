# 1. Write lambdas to:
# a. Square a number x2
# b. Inverse a number 1/x
# c. Negate a number
from functools import reduce

square = lambda x : x*x
inverse = lambda x:1/x
negate = lambda x: -x

print(square(5),inverse(4), negate(3))


# 2. Use reduce function and an appropriate lambda to find the maximum number in a list.
li = [2,3,71,1,0]
max_num = reduce(lambda a,b: a if a>b else b, li)
print (max_num)

# 3. Write a function map_multiple that takes a list of functions/lambdas as first argument and a
# sequence type as second argument.
# The function picks first lambda from list, applies it to first element, then applies the second
# function to the result of first one and ….
# Similarly it does for each element and generates a mapping of input to output
# def map_multiple(functs, sequence):
#  # write definition here
# Ex: let list of lambdas be from question 1 and the list on numbers be [1,2,4]
#  So first function gives [1, 4, 16]
#  Second gives [1, 0.25, 0.0625]
#  Third gives [-1, -0.25, -0.0625]. Which is the final result.
functs = [square,inverse,negate]
def map_multiple(functs,inpt):
    for func in functs:
        inpt = list(map(func ,inpt))
    return inpt

print(map_multiple(functs,[1,2,3,4]))

# 4. Predict the output of following code:
#50
#checking
f = lambda x,y : x if x>y else y

l = [10,30,50,30,10]
num= reduce(f,l)
print(num)
    
# 5. Find output of following:
sqrt = lambda x : x**0.5
functs = [sqrt,inverse]
l = [1,4,16,64]
ans = []
for num in l:
	res = num
	for funct in functs:
		res = funct(res)
	ans.append(res)
print(ans)

#Ans = [1,1/2,1/4,1/8]

# Python
# Gaurav Gupta tuteur.py@gmail.com
# 6. Use filter function to filter a list of numbers and strings such that the result contains only
# numbers. (Hint : Use isinstance method)
mixture = [1,'one',2,'two']

print(list(filter(lambda x: isinstance(x,int), mixture)))

# 7. Assume a list containing heights ft and inches in the form of a list of string
# Example : l = [‘5ft10in’, ‘5ft’, ….]
# Write a function to convert the heights to meter. Use map function along with your function to
# convert everything to m.
l = ['3ft10in','4ft', '7in']
def to_meters(ht):
        ht = ht.split('ft')

        if len(ht)==1:
            ft = 0
            inch = ht[0].split('in')[0]
        elif ht[1] == '':
            ft = ht[0]
            inch = 0
        else:
                ft = ht[0]
                inch = ht[1].split('in')[0]

        meters = int(ft)*0.3048 + int(inch)*0.0254
        return meters

print(list(map(to_meters,l)))


# 8. Write the implementation for the map function yourself by the name my_map

def my_map(func,sequence):
    result = []
    for el in sequence:
        result.append(func(el))
    return result

print(my_map(square,li))