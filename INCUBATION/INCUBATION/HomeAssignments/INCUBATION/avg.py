import sys

args = sys.argv[1:]
iarg = []
try:
    for arg in args:
        if arg.isnumeric() == False:
            print("Please enter numbers only")
            iarg = []
            break
        else:
            iarg.append(int(arg))
    print(sum(iarg))
    avg = sum(iarg)/len(args)
    print("average of input numbers =", avg)
except ZeroDivisionError:
    print("Please provide some input")

