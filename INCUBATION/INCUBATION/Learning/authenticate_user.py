import requests

resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth = ("admin", "admin") )

print(resp) #200

# resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth = ("admin", "admn") )
# print(resp) #401 - user unauthorised
resp2 = requests.get("https://www.nasdaq.com")
print(resp2)