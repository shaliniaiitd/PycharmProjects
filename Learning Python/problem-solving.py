#Implement a function to check if a given string is a palindrome.
import string
inpt = 'A man, a plan a canal-Panama'

inpt = inpt.lower()
new_inpt = ""
print(inpt)
exclude_chars = string.whitespace +  string.punctuation
print(exclude_chars)
new_inpt = ''.join(el for el in inpt if el not in exclude_chars)
#new_inpt = ''.join(el for el in inpt if el != " ")
print(new_inpt)

#Question: Given a list of integers, implement a function to find the two numbers that sum up to a specific target. Return their indices.

num_list =

for num in num_list:

# # Write a Python function called find_common_elements(list1, list2) that takes two lists as input and returns a list containing elements that are common to both input lists. The order of elements in the result list should match their order in the first list. If there are no common elements, return an empty list.
# #
# # Example:
# #
# # python
# # Copy code
# list1 = [1, 2, 5, 3, 4, 5]
# list2 = [5, 6, 4, 7,5]
# # result = find_common_elements(list1, list2)
# # print(result)  # Output should be [4, 5]
#
# result = [el for el in list1 if el in list2]
# print(result)
#
# list1 = ['apple', 'Guava', 'orange']
# list2 = ['Apple', 'ORANGE', 'pineapple']
#
# def list_common(list1, list2):
#     list1 = [el.lower() for el in list1 if type(el) == str]
#     list2 = [el.lower() for el in list2 if type(el) == str]
#
#
#     result = [el for el in list1 if el in list2]
#
#     return result
#
# print(list_common(list1,list2))
# #
# # Write a Python function called longest_consecutive_sequence(nums) that takes a list of integers as input and returns
# # the length of the longest consecutive sequence of numbers in the list. You can consider that a sequence is
# # "consecutive" if the elements are sorted in increasing order (e.g., [1, 2, 3, 4]).
# # nums = [100, 4, 200, 1, 3, 2]
# # result = longest_consecutive_sequence(nums)
# # print(result)  # Output should be 4, representing the sequence [1, 2, 3, 4].
#
# def longest_consecutive_sequence(list1):
#     list1.sort()
#     print(list1)
#     cons_list = []
#     bigger_list = []
#     i = 0
#     while i < len(list1)-1:
#         print(i)
#         if  list1[i+1] - list1[i] == 1 :
#             if list1[i] not in cons_list:
#                 cons_list.append(list1[i])
#             cons_list.append(list1[i+1])
#             print(cons_list)
#         else:
#             if cons_list != []:
#                 bigger_list.append(cons_list)
#             cons_list = []
#             #cons_list.append(list1[i])
#         i = i+1
#     bigger_list.sort()
#     print(bigger_list)
#
#     dict1 =   {len(el): el  for el in bigger_list}
#
#     print(max(dict1.keys()))
#
#     return dict1[max(dict1.keys())]
#
#
# print(longest_consecutive_sequence([2,5,6,1,8,9,12,13,56,100,7,57]))
#
# # Problem: Reversed Pairs
# #
# # Write a Python function called reversed_pairs(nums) that takes a list of integers as input and
# # returns the count of all reversed pairs. A reversed pair is a pair of indices (i, j) such that i < j and
# # nums[i] > nums[j].
# # In other words, it counts how many times a smaller element appears after a larger element in the list.
#
# def reversed_pairs(nums):
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i,len(nums)):
#             if nums[i] > nums[j]:
#                 count +=1
#     return count
# print(reversed_pairs([2,4,5,1,4,9,7,8]))
#
# # Problem: Prime Numbers
# # Write a Python program to print all prime numbers less than a given number n.
#
# def is_prime(n):
#
#     for i in range(2,n//2):
#         if n%i == 0:
#             flag = False
#             break
#     else:
#         flag = True
#     return flag
#
# n=50
# result = [el for el in range(n) if is_prime(el)]
#
# print(result)
#
# #using list comprehension find all prime numbers from 1to 50
#
# n=50
# # result = [el for el in range(2,n) if el% i for i in range(2,el)  ]
#
# print(result)
#
# # Problem: Anagrams
# #
# # Write a Python function called are_anagrams that takes two strings as input and returns True if
# # the two strings are anagrams of each other, and False otherwise.
# # Anagrams are words or phrases that are formed by rearranging the letters of another word or phrase,
# # using all the original letters exactly once.
#
# def are_anagrams(s1,s2):
#     l1 = list(s1)
#     l2 = list(s2)
#     for el in l1 :
#         flag = True
#         if el not in l2:
#             flag = False
#             break
#         else:
#             l2.remove(el)
#
#     if l2:
#         flag = False
#     return flag
#
# print(are_anagrams("1silenti", "listeni"))
#
#
# def fact(n):
#
#     if n <=1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))
#
# def fibonacci(n):
#     fib= []
#     a,b = 0,1
#     fib.append(a,b)
#     for i in range(2,n):
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
