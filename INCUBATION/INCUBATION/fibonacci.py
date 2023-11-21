def fib(n):

    if n <2:
        return n
    else:

        return  fib(n-1) + fib(n-2)


m = 5

for i in range(m):
    print(fib(i))