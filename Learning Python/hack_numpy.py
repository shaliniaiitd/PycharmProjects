import numpy

n,m = map(int,input().split())
print(n,m)
row = []
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
mean = numpy.mean(matrix,axis=1)
var = numpy.var(matrix,axis=0)
std = numpy.std(matrix)

print(mean)
print(var)
print(std)
# n = in_list[0]
# m = in_list[1]
#
# print(n,m)
