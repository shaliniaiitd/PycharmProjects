#Base URL  -> https://jsonplaceholder.typicode.com
import requests
from urllib.parse import urljoin
import json
base_url = "https://jsonplaceholder.typicode.com/"
#Resources available -->
re_list = ["posts","comments","albums","photos","todos","users"]
dict1 = {}
for re in re_list:
    url = urljoin(base_url,re)
    resp = requests.get(url)
    print(resp.status_code)
    # 1. Verify the number of resources at each resource end point
    dict1[re] = len(resp.json())

expected_dict = {'posts': 100, 'comments': 500, 'albums': 100, 'photos': 5000, 'todos': 200, 'users': 10}
assert dict1 == expected_dict


# 2. For each type of resource
# a. Get a specific resource data
url = base_url + "users"
#i. verify the response code
resp = requests.get(url)
assert resp.status_code == 200

#ii. Verify the response body
assert len(resp.json()) == 10

# b. Modify a specific resource data

#modify resource with id=2
url1 = url + '/2'
payload = {"email": 'shalini@gmail.com'}
resp = requests.patch(url1,data = payload )

# i. verify the response code
assert resp.status_code == 200

# ii. Verify the response body
assert resp.json()["email"] == 'shalini@gmail.com'

# d. Create your own resource
# take payload from a file.

fp = open('data.json', 'r')
json_data = fp.read()

data = {
    "name": "Shalini Agarwal",
    "username": "shalini",
    "email": "abc@def.com",
    "address": {
        "street": "Victor Plains1",
        "suite": "Suite 8791",
        "city": "Wisokyburgh1",
        "zipcode": "5350021",
        "geo": {
            "lat": "-43.95091",
            "lng": "-34.46181"
        }
    },
    "phone": "62813009571234",
    "website": "anastasia.net1",
    "company": {
        "name": "Deckow-Crist1",
        "catchPhrase": "Proactive didactic contingency1",
        "bs": "synergize scalable supply-chains1"
    }
}

print("JSON_DATA read directly from file:", json_data)
#resp = requests.post(url,data=json_data)
resp = requests.post(url,data=data)
#print(resp.headers)

# i. verify the response code
assert resp.status_code == 201, f"{resp.status_code}"

# ii. Verify the response body
expected_response = {
    "name": "Shalini Agarwal",
    "username": "shalini",
    "email": "abc@def.com",
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "535002",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
    },
    "phone": "62813009571234",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
    },
    "id": 11
}
print(resp.json())

print(resp.content)
print(resp.text)

# c. Delete a specific resource
url2 = url + '/11'

resp = requests.delete(url2)

# i. verify the response code
assert resp.status_code == 200
# ii. Verify the response body

assert resp.json() == {}

#
#
#
# #That one of the users has a name of “Ervin Howell”
# resp = requests.get(url)
#
# i = 0
# for resp in resp.content:
#     if resp['name'] == 'Ervin Howell':
#         print(f"Found user with id {resp.json()['id']} having name {resp.json()['name']}")
#         break
#     i += 1
#
