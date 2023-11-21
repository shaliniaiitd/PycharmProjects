import requests

resp = requests.get("https://httpbin.org/delay/3", timeout=2)

print(resp.status_code)