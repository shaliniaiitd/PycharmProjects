import requests
import json
import xml
import xml.etree.ElementTree as ET
import xmltodict
import pytest
from collections import Mapping

apiurl = "http://www.dneonline.com//calculator.asmx"
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://tempuri.org/Add'
}
def test_soap1():
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
    xpars = xmltodict.parse(r1.content)
    print(xpars)

    assert (xpars["soap:Envelope"]["soap:Body"]["AddResponse"]["AddResult"]) ==7


# soap2_input='''<?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <Add xmlns="http://tempuri.org/">
#       <intA>23</intA>
#       <intB>1</intB>
#     </Add>
#   </soap12:Body>
# </soap12:Envelope>'''
# r1 = requests.post(apiurl, headers=headers, data= soap2_input)
#
# print(r1.headers)
# print(r1.status_code)
