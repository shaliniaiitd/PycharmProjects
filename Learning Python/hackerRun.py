
x = 1
y = 1
z = 1
n = 3

result = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=3]
print(result)