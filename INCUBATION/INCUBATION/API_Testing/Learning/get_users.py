import requests
#import jsonpath


# url = 'https://reqres.in/api/users?page=2'
#
# resp = requests.get(url)

resp = requests.get('https://reqres.in/api/users',params={"page":2})
print(resp.url)
print(resp.json())  # can view at https://jsonviewer.stack.hu/
assert resp.json()['data'][0]["first_name"] == "Michael", "name did not match"
# print(dir(resp))    #list of all properties(methods) available
# print(resp.text)    #text format
# print(type(resp))
# print(resp.headers)
# #print(resp.json())
# print(resp.request)
print(resp.url) #url that is made
print(resp.cookies)

json_resp = resp.json()
print(json_resp.keys())
print(json_resp.values())
print(json_resp.items())
print(json_resp['total_pages'])

print(resp.json()['support']['url'])











# r = requests.put(url , data={'key': 'value'})
#
# r = requests.delete()
#
# r = requests.head()
#
# r = requests.options()