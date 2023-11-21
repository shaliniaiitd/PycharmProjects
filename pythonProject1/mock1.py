inpt = '1222311'

#out = (1,1),(3,2),(1,3),(2,1)
count = 1
result = []
for i in range(0,len(inpt)-1):
	if inpt[i] == inpt[i+1]:

		count += 1
	else:
		result.append((count,int(inpt[i])))
		count = 1
result.append((count, int(inpt[i])))
print(result)