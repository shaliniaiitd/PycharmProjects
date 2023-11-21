st='India'
print(st[-1])
print(st[::-1])
print(st[:-1])

list1 = ['my','name']
list2 = ['is','john']
print(" ".join(list1 + list2))

list1 = ['a', 'b', 'c']
list2 = [1,2,3]

result = {key:value for key,value in zip(list1,list2)}

print(result)

#Program to call number of instances of a class

class MyClass():
    count = 0
    def __init__(self):
        MyClass.count += 1
        print()


a= MyClass()
a= MyClass()
print(MyClass.count)

# Write a program to print duplicate words within a list

st  = 'Shalini is a good girl and a good person'
list1 = st.split(' ')
print(list1)
result = [el for el in list1 if el in list1[list1.index(el)+1::]]

print(result)

# Write a program to print duplicate/uique characters within a list
result = []
str = " ".join(list1)
for el in str:
        if str.count(el)>1  and el not in result:
            result.append(el)  # for unique use condition str.count(el)==1
print(result)

#Write a one line loop to print all the words in the list that star with character 'i'
str = 'My country is India'
list2 = str.split(" ")

result = [word for word in list2  if word.lower().startswith('i') ]

print(result)


