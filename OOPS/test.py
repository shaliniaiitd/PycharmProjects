# person = {
#     "name": "John",
#     "age": 30,
#     "address": {
# 	    "key": {"name_super": "John","age_super": 30},
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA"
#     }
# }
#
#
#
#
# l1 = [1,2,3,4,5,6,7,8,9]
#
# result = sum([ x for x in l1 if x%2])
#
# l2 = [[1,2,3],[4,5,6],[7,8,9]]
# l3 = [el for l in l2 for el in l] # [1,2,3,4,5,6,7,8,9]

l =  [2, 4, 5, 100, 200, 7, 9, 1, 2, 3]
sum = 0
for i in range(1,len(l)+1):
    if l[i] == 5:
        for j in range(i+1,len(l)+1):
            if l[j] == 9:
                break
            else:
                continue
    sum += l[i]

print(sum)

temp = 5

def main():
    def func():
        print(temp)
        temp = temp + 5
        print(temp)

    func()
    print(temp)
import requests
import jsonpath


# url = 'https://reqres.in/api/users?page=2'
#
# resp = requests.get(url)

resp = requests.get('https://reqres.in/api/users',params={"page":2}, )