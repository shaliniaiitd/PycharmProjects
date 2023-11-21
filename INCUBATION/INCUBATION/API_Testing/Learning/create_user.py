import requests
import json

base_url = 'https://reqres.in'
endpoint = '/api/users'
url = base_url+endpoint
print(url)
resp = requests.post(url, data = {"name": 'shalini agarwal', "job": 'sdet'})
print(resp)
print(resp.json())

assert resp.json()['job'] == 'sdet'

#read payload from a file

json_data = open('data.json', 'r').read()
print(json_data)

payload = json.loads(json_data)
print(payload)

resp = requests.post(url, data = payload)

print(resp)
print(resp.json())
print(resp.headers['Content-Length'])

#user with auth, get the token returned from server in response

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
url = base_url + "/api/register"
resp = requests.post(url, data = payload)
print(resp)
print(resp.json()['token'])
print(resp.headers)
