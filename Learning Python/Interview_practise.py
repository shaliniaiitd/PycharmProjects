#Given a list of integers, implement a function to find the two numbers that sum up to a specific target. Return their indices.

list1 = [1,6,12,5,9,10,34,2,3]
target = 14
def sum_target(l, t):
    result = set()
    seen = {}  # Dictionary to store index of elements

    for i, num in enumerate(l):
        target = t - num
        if target in seen:  # Check if target was seen before
            result.add(tuple(sorted((i, seen[target]))))  # Store tuple instead of list
        seen[num] = i  # Store index of current number

    return result

print(sum_target(list1,target)

#5. Try following code and note down the observations:
t6 = 1, 2, 3
print(f"type of t6 is {type(t6)}")

#6. Try following code and note down the observations:
t7 = ()
#print type and length of t7
print(f"type of t7 is {type(t7)}, length = {len(t7)}")



# st='India'
# print(st[-1])
# print(st[::-1])
# print(st[:-1])
#
# list1 = ['my','name']
# list2 = ['is','john']
# print(" ".join(list1 + list2))
#
# list1 = ['a', 'b', 'c']
# list2 = [1,2,3]
#
# result = {key:value for key,value in zip(list1,list2)}
#
# print(result)
#
# #Program to call number of instances of a class
#
# class MyClass():
#     count = 0
#     def __init__(self):
#         MyClass.count += 1
#         print()
#
#
# a= MyClass()
# a= MyClass()
# print(MyClass.count)
#
# # Write a program to print duplicate words within a list
#
# st  = 'Shalini is a good girl and a good person'
# list1 = st.split(' ')
# print(list1)
# result = [el for el in list1 if el in list1[list1.index(el)+1::]]
#
# print(result)
#
# # Write a program to print duplicate/uique characters within a list
# result = []
# str = " ".join(list1)
# for el in str:
#         if str.count(el)>1  and el not in result:
#             result.append(el)  # for unique use condition str.count(el)==1
# print(result)
#
# #Write a one line loop to print all the words in the list that star with character 'i'
# str = 'My country is India'
# list2 = str.split(" ")
#
# result = [word for word in list2  if word.lower().startswith('i') ]
#
# print(result)
#
#
