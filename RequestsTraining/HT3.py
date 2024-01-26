import requests

# Create a PET using the POST call from http://petstore.swagger.io/#/

url = "http://petstore.swagger.io"
# Request Body:
id = 12345
body = {
"id": id,
 "category": {
"id": 1,
"name": "dog"
},
"name": "snoopie",
"photoUrls": [
"string"
],
"tags": [
{
"id": 0,
"name": "string"
}
],
"status": "pending"
}

resp = requests.post(url,data=body)

assert resp.status_code == 200

# once the pet is created write the test cases using REST assured for the below calls
# https://petstore.swagger.io/v2/pet/12345
# GET call
url = url + f"/v2/pet/{id}"
resp = requests.get(url)
# Validate the below from API response:
# That the status code is equal to ‘200’
resp.status_code == 200
# That the content type is ‘application/json’
resp.headers['content-type'] == 'application/json'

print(resp.json())
# That if the pet is a ‘dog’
resp.json()['category']['name'] == 'dog'
#
# # That its name is ‘snoopie’
#
resp.json()['name'] == 'snoopie'
# # That its current status is ‘pending’
#
resp.json()['status'] == 'pending'