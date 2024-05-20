# # Problem: Timing Function Execution
# #
# # Write a Python decorator function called calculate_time that can be used to measure the time taken for the
# # execution of another function. The decorator should print the time in seconds that the decorated function
# # takes to run.
# #
# # Use the time module to track the execution time.
#
# def calculate_time(func):
#     import time
#     def inner(*args):
#         t1 = time.time()
#         fact = func(*args)
#         t2 = time.time()
#         print(f"time taken to execute {str(func)} = {t2-t1}")
#         return fact
#     return inner
# @calculate_time
# def fact(n):
#     import time
#     time.sleep(2)
#     fact = 1
#     if n <=1:
#         return fact
#     else:
#         for i in range(2,n+1):
#             fact =  i*fact
#     return fact
#
# print(fact(100))


# import operator
#
# def person_lister(f):
#     def inner(*peoples):
#         for people in peoples :
#             f(people)
#
#     return inner
#
# @person_lister
# def name_format(persons):
#     for person in persons:
#         print (person)
#         print (("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1])
#
# if __name__ == '__main__':
#     peoples = [input().split() for i in range(int(input()))]
#     #print(people)
#     name_format(peoples)

import operator
def person_lister(f):
        def inner(people):
            msg = []
            for person in people:
                a = f(person)
                msg.append(a)
            return msg
        return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')