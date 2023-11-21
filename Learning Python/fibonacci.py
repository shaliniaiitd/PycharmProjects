def fib_f(n):
    result = [0,1]

    for i in range(2,n+1):
        result.append(result[-1] + result[-2])
    return result

print(fib_f(7))  #[0, 1, 1, 2, 3, 5, 8, 13]

#using decorator

