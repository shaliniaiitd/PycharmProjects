import requests

base_url = "https://www.yahoo.com"
end_point = "/users/sign_up"
url = base_url + end_point

resp  = requests.options(base_url)
print(resp.text)
#print(resp.content)
print(resp.headers)
# resp = requests.post(url,auth = (username, email, password) )