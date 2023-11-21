dic = {'name':['abc', 'def'], 'edu': ['BTECH', 'BPHARM'], 'city':['hyd', 'ban']}

for key,val in dic.items():
    val = [el.swapcase() for el in val]
    dic[key]= val

print(dic)

#Write python code for li1 = [1,2,3,4,4,4,5,8] li2=[2,2,3,6,7]
#print common elements from both elements do not use sets.

li1 = [1, 2, 3, 4, 4, 4, 5, 8]
li2 = [2, 2, 3, 6, 7]

common = list(filter(lambda el: el in li2 , li1))
print(common)

li1 = set(li1)
li2 = set(li2)

print(li1.intersection(li2))

import mysql.connector
my_db = mysql.connector.connect(host='localhost', port=0, timeout=-999, usr = '', password = '', database = '')

sqlquery = "select * from table1 t1 inner join table2 t2 ON t1.id = t2.id where t1.name like '%shal%'"

#POST request in python
import request
payload = {'one':1,'two':2}
resp = request.post(data = payload )

