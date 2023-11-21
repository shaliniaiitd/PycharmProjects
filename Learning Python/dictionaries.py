# directory = [{"name":'emp1', "age": 12, "dept": "hr"}, {"name":"emp2", "age" :23, "dept": "it"}, {"name":"emp3", "age":67,"dept": "hr"}]
#
# sum_ages =   sum([emp["age"] for emp in directory])
# av = sum_ages/len(directory)
# print(av)
#
# max_age = max([emp["age"] for emp in directory])
# print(max_age)
#
# #department_employees(employees, department): Return a list of employees from a specific department.
# print([emp for emp in directory if emp["dept"] == "it"])
#
# #add_employee(employees, employee_info): Add a new employee to the directory.
# employee_info = {'name': 'emp4', 'age': 43, 'dept': 'fin'}
# directory.append(employee_info)
# print(directory)

#
# user_records = [
#     {"name": "Alice", "email": "alice@example.com", "purchases": 3},
#     {"name": "Bob", "email": "bob@example.com", "purchases": 5},
#     {"name": "Alice", "email": "alice@example.com", "purchases": 2},
#     {"name": "Bob", "email": "bob@example.com", "purchases": 1},
#     {"name": "Charlie", "email": "charlie@example.com", "purchases": 4},
#     {"name": "Bob", "email": "bob@example.com", "purchases": 2},
# ]
#
# # Expected Output
# # {
# #     "Alice": 5,
# #     "Bob": 8,
# #     "Charlie": 4
# # }
#
# ex_output = {}
#
# for record in user_records:
#
#     key = record["name"]
#     value = record["purchases"]
#
#     if key in ex_output.keys():
#         ex_output[key] +=  record["purchases"]
#     else:
#         ex_output[key] = value
#
# print(ex_output)

'''Write a Python function that takes a list of sentences as input and returns a dictionary of word frequencies.
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "The dog barks, and the fox runs away.",
    "Fox and dog are friends."
]

# Expected Output
# {
#     "the": 5,
#     "quick": 1,
#     "brown": 1,
#     "fox": 3,
#     "jumps": 1,
#     "over": 1,
#     "lazy": 1,
#     "dog": 3,
#     "barks": 1,
#     "and": 2,
#     "runs": 1,
#     "away": 1,
#     "are": 1,
#     "friends": 1
# }
'''
# sentences = sentences = [
#     "The quick brown fox jumps over the lazy dog.",
#     "The dog barks, and the fox runs away.",
#     "Fox and dog are friends."
# ]
# ex_output = {}
# words = []
#
# for sentence in sentences:
#     words += sentence.strip('.').split(" ")
#
# for word in words:
#         if word.lower() in ex_output.keys():
#             ex_output[word.lower()] += 1
#         else:
#             ex_output[word.lower()] = 1
#
# print(ex_output)

# items = {
#     "item1": {
#         "name": "Product A",
#         "price": 10.99,
#         "quantity": 100,
#     },
#     "item2": {
#         "name": "Product B",
#         "price": 5.99,
#         "quantity": 50,
#     },
#     "item3": {
#         "name": "Product C",
#         "price": 15.99,
#         "quantity": 200,
#     },
# }
#
# def find_item(dict1,item):
#     if item in dict1.keys():
#         return dict1[item]
#     else:
#           print(f"{item} not in dict")
#
# def del_item(dict1,item):
#     if item in dict1.keys():
#         del dict1[item]
#     else:
#           print(f"{item} not in dict")
#
# print(find_item(items,"item2"))
# del_item(items,"item3")
# print(items)

# Write a Python function that takes a list of connections as input and performs the following tasks:
#
# Find the number of friends for each user.
# Find the user with the most friends.
# Find the number of mutual friends between each pair of users.

connections = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Eve", "Charlie"),
    ("Eve", "Frank"),
    ("Grace", "David"),
    ("Grace", "Eve"),
]
# 1. Number of friends for each user:
friends = {}
for connection in connections:
    if connection[0] in friends.keys():
        friends[connection[0]] += 1
    else:
        friends[connection[0]] = 1
    if connection[1] in friends.keys():
        friends[connection[1]] += 1
    else:
        friends[connection[1]] = 1
print(friends)

# 2. User with the most friends: "Eve" (3 friends)

print({key:value for key,value in friends.items() if value == max([value for value in friends.values()])})

# 3. Number of mutual friends between each pair of users:



# Expected Output:
# 1. Number of friends for each user:
# {
#     "Alice": 2,
#     "Bob": 2,
#     "Charlie": 2,
#     "David": 2,
#     "Eve": 3,
#     "Frank": 1,
#     "Grace": 2,
# }
#
# 2. User with the most friends: "Eve" (3 friends)
#
# 3. Number of mutual friends between each pair of users:
# {
#     ("Alice", "Eve"): 1,
#     ("Alice", "Grace"): 1,
#     ("Alice", "Bob"): 1,
#     ("Alice", "Charlie"): 1,
#     ("Alice", "David"): 1,
#     ("Alice", "Frank"): 0,
#     ("Bob", "Charlie"): 1,
#     ("Bob", "David"): 1,
#     ("Bob", "Frank"): 0,
#     ("Charlie", "David"): 1,
#     ("Charlie", "Frank"): 0,
#     ("David", "Eve"): 1,
#     ("David", "Grace"): 2,
#     ("David", "Frank"): 0,
#     ("Eve", "Frank"): 0,
#     ("Grace", "Eve"): 2,
#     ("Grace", "Frank"): 0,
# }







