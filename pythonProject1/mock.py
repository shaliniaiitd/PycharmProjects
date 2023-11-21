inpt = 1222311

#out = (1,1),(3,2),(1,3),(2,1)
count = 0
result = []
for i in range(len(inpt)):
	if inpt[i] == inpt[i+1]:
		count += count
	else:
		result.append(count,inpt[i-1])
		count = 1

print(result)


select * from () view where view.count >1

select count(*) as count, id,name,age from table group by (id,name,age) having count >1


delete from table