import requests
import json
import xml
import xml.etree.ElementTree as ET
import xmltodict
import pytest


apiurl = "http://www.dneonline.com//calculator.asmx"
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://tempuri.org/Add'
}

soap1_input='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="http://tempuri.org/">
      <intA>1</intA>
      <intB>6</intB>
    </Add>
  </soap:Body>
</soap:Envelope>'''

r1 = requests.post(apiurl, headers=headers, data=soap1_input)
print(r1.status_code)
xpars = xmltodict.parse(r1.text)
print(xpars)

assert (xpars["soap:Envelope"]["soap:Body"]["AddResponse"]["AddResult"]) == '7'

#Test Divide
headers = {
'Content-Type': 'text/xml; charset=utf-8',
'SOAPAction': 'http://tempuri.org/Divide'
}

soap_input='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Divide xmlns="http://tempuri.org/">
      <intA>24</intA>
      <intB>0</intB>
    </Divide>
  </soap:Body>
</soap:Envelope>'''

r1 = requests.post(apiurl, headers=headers, data= soap_input)

# print(r1.headers)
# print(r1.status_code)

xpars = xmltodict.parse(r1.text)
print(xpars)

assert (xpars["soap:Envelope"]["soap:Body"]["DivideResponse"]["DivideResult"]) == '4'

#Test Divide
headers = {
'Content-Type': 'text/xml; charset=utf-8',
'SOAPAction': 'http://tempuri.org/Divide'
}

soap_input='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Divide xmlns="http://tempuri.org/">
      <intA>24</intA>
      <intB>0</intB>
    </Divide>
  </soap:Body>
</soap:Envelope>'''

r1 = requests.post(apiurl, headers=headers, data= soap_input)

# print(r1.headers)
# print(r1.status_code)

xpars = xmltodict.parse(r1.text)
print(xpars)

assert (xpars["soap:Envelope"]["soap:Body"]["DivideResponse"]["DivideResult"]) == '4'