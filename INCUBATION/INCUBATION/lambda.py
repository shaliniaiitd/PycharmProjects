my_func = lambda x : print("Hello", x)

my_func("shalini")

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

even_list = [el for el in my_list if el%2 ==0]

print(even_list)

#using lambda function
filtered_list = list(filter(lambda x : x%2 == 0 , my_list))
print(filtered_list)

# Program to double each item in a list using map()
doubled_list = list(map(lambda x : 2*x , my_list))
print(doubled_list)

