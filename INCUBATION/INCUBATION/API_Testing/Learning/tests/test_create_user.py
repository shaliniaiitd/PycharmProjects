import requests
import json
import pytest
from  INCUBATION.API_Testing.Learning.utilities import read_config as rc
from  INCUBATION.API_Testing.Learning.utilities.customLogger import LogGen

def test_user_creation():
    logger = LogGen.loggen()
    logger.info("START test user creation")

    base = rc.get_url('base_url')

    endpoint = '/api/users'
    url = base +endpoint
    print(url)
    resp = requests.post(url, json = {"name": 'shalini agrwal', "job": 'sdet'})
    print(resp.status_code)
    print(resp.json())
    resp.text

    assert resp.json()['job'] == 'sdet'

def test_user_creation_json():
    #read payload from a file
    logger = LogGen.loggen()
    logger.info("START test user creation")

    base = rc.get_url('base_url')

    endpoint = '/api/users'
    url = base + endpoint
    fp = open('../test_data/data.json', 'r')
    json_data = fp.read()
    print("JSON_DATA read directly from file:", json_data)
    payload = json.loads(json_data)  #converts json to python

    py_dic = json.load(fp)

    print(py_dic)
    #print(f"payload from loads: {payload} \n python load from load: {py_load}")
    print("PAYLOAD:",payload)
    dict = {"name": "agrwal", "job": "api tester"}
    print("PYTHON DICT:", dict)
    json_data = json.dumps(dict)    #converts python to json
    print("JSON_DATA:", json_data)
    resp = requests.post(url, data = json_data)
    print(resp.status_code)
    print(resp.json())
    # resp = requests.post(url,json=payload)  #Python payload that needs to be serialized- converted to JSON format.
    # print(resp.status_code)
    # print(resp.json())
#print(resp.headers['Content-Length'])

#user with auth, get the token returned from server in response

# payload = {
#     "email": "eve.holt@reqres.in",
#     "password": "pistol"
# }
# url = base + "/api/register"
# resp = requests.post(url, data = payload)
# print(resp)
# print(resp.json()['token'])
# print(resp.headers)
