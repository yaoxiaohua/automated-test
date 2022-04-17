# coding:utf-8
from suds.client import Client
url = 'http://localhost:7080/webservices/WebServiceTestBean?wsdl'
client = Client(url)
print(client)