from simple_salesforce import Salesforce
import json
import sys

sf_username = ""
sf_password = ""
sf_security_token = "" # Generate this by going into your "personal user" settings > Reset my security token
domain = "Test" # for sandbox
sf = Salesforce(username=sf_username, password=sf_password, security_token=sf_security_token, domain=domain)

data = sf.query("Select Id From Account Limit 10")

print(data)
