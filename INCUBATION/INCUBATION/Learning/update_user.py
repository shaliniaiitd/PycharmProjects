import requests
import json

payload = {"name": "new_name", "job": "my_job"}
resp  = requests.put("https://reqres.in/api/users/40", data = payload)

print(resp)
print(resp.json())

load_patch = {"name": "new_shalini"}
resp = requests.patch("https://reqres.in/api/users/40", data = load_patch)

print(resp)
print(resp.json())
