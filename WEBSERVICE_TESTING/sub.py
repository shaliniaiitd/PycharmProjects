import requests
import json
import xml

apiurl = "http://www.dneonline.com//calculator.asmx"

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://tempuri.org/Sub'
}

# file = open('payload.xml', 'r')
# xml_input = file.read()

xml_input='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Subtract xmlns="http://tempuri.org/">
      <intA>2</intA>
      <intB>3</intB>
    </Subtract>
  </soap:Body>
</soap:Envelope>'''

r = requests.post(apiurl, headers=headers, data= xml_input)

print(r.content)
print(r.status_code)