# Problem: Timing Function Execution
#
# Write a Python decorator function called calculate_time that can be used to measure the time taken for the
# execution of another function. The decorator should print the time in seconds that the decorated function
# takes to run.
#
# Use the time module to track the execution time.

def calculate_time(func):
    import time
    def inner(*args):
        t1 = time.time()
        fact = func(*args)
        t2 = time.time()
        print(f"time taken to execute {str(func)} = {t2-t1}")
        return fact
    return inner
@calculate_time
def fact(n):
    import time
    time.sleep(2)
    fact = 1
    if n <=1:
        return fact
    else:
        for i in range(2,n+1):
            fact =  i*fact
    return fact

print(fact(100))