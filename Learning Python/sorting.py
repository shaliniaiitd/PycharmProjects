
inpt = [('a',12),('a',14),('b',10),('c',12),('b',22),('d',11),('e',8),('f',13),('g',21)]
result = {}

for el in inpt:
    if el[0] in result.keys():
        value = result[str(el[0])] + el[1]
    else:
        value = el[1]
    result[str(el[0])] = value
print(result)

# print(result)
result = dict(sorted(result.items(),key=lambda x: x[1]))

print(result)

# max = 0
# res_key = ""
# sort_result = {}
# for key,value in result.items():
#     if value > max:
#         max = value
#         res_key = key
#
#
# print(res_key,max)



