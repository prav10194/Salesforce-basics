from simple_salesforce import Salesforce
import json
import sys

sf_username = ""
sf_password = ""
sf_security_token = "" # Generate this by going into your "personal user" settings > Reset my security token. The token will be sent to you on email. 
domain = "Test" # for sandbox. Remove the domain attribute from API otherwise.

sf = Salesforce(username=sf_username, password=sf_password, security_token=sf_security_token, domain=domain)

data = sf.query("Select Id, Name From Account Limit 10")

# print(data['totalSize'])

# print Id, Name for the records
for row in data['records']:
    print(f"Entity name: {row['attributes']['type']}, url: {row['attributes']['url']}")
    print(f"Id: {row['Id']} and Name: {row['Name']} \n")
