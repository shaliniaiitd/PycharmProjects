'''Properties of hash() function
Objects hashed using hash() are irreversible, leading to loss of information.
hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.'''

# initializing objects
int_val = 4
str_val = 'shalini'
flt_val = 24.56

# Printing the hash values.
# Notice Integer value doesn't change
# You'll have answer later in article.
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))

print(int_val)
# initializing objects
# tuple are immutable
tuple_val = (1, 2, 3, 4, 5)

# list are mutable
list_val = [1, 2, 3, 4, 5]

# Printing the hash values.
# Notice exception when trying
# to convert mutable object
print("The tuple hash value is : " + str(hash(tuple_val)))
print("The list hash value is : " + str(hash(list_val)))

input_list = [3,'shalini',34.2,(1,2,3),[1,2,3]]
status = None

for el in input_list:
    try:
        if str(hash(el)) != None:
            print(f"{el} is immutable")
    except TypeError:
        print(f"{el} is mutable")
