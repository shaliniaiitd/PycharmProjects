import requests

resp = requests.delete("https://reqres.in/api/users/40")

print(resp.status_code)