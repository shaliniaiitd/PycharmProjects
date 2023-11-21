my_list = [1, 2, 3, 4, 5]

other_list = ['a', 1, 1.0, False]

print(my_list + other_list)

my_list[0] = "a"
print(my_list)

my_list += [6, 7, 8, 9, 10]     # ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

my_list[1:3] = ['b', 'c']       # ['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]
print(my_list)

my_list[3:5] = ['d', 'e', 'f'] # this will insert additional elements
print(my_list)   # ['a', 'b', 'c', 'd', 'e', 'f', 6, 7, 8, 9, 10]
my_list[3:5] = ['D']
print(my_list)  #['a', 'b', 'c', 'D', 'f', 6, 7, 8, 9, 10]


my_list[4:] = []    # removing the elements: index 4 onwards
print(my_list)      # ['a', 'b', 'c', 'D']

del my_list[0]  # deleting first element
print(my_list)  # ['b', 'c', 'd']

#del my_list   # deletes object my_list from memory
#print(my_list)

my_list.clear()     # clears only contents of my_list
print(my_list)      # []

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)    #ValueError: attempt to assign sequence of size 6 to extended slice of size 5

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)    ## [10,2,20,4,30,6,40,8,50]

l1 = [10, 25, 15, 30, 10, 20]
print("list contents", l1)

print("reversed object address", reversed(l1))
print("list using reversed object", list(reversed(l1)))
print("sorted - list format", sorted(l1))  # just for printing, it won't change the list contents
print("descending order - list format", sorted(l1, reverse=True))  # just for printing, it won't change the list contents

list = ['a', 'b', 'c', 'd', 'e']
print (list [10:]) # []

l3 = [40, 10, 25, 15, 30, 10, 20]

print("l3 contents", l3, "l3 is a", type(l3))
print("length of l3", len(l3))
print("first element in l3", l3[0])
print("last element in l3", l3[-1])
print("first 3 elements in l3", l3[:3])
print("last 4 elements in l3", l3[-4:])
print("Reverse of l3", l3[::-1])

print("count of 10 in l3", l3.count(10))
print("index of 10 in l3", l3.index(10))

