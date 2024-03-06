#pulling members from API

import requests
import json
import csv

Auth = ("<Your TOKEN")
headers = {'Authorization': 'token '+ Auth,
           "Accept": "application/vnd.github.v3+json"}
query = requests.get("https://api.github.com/orgs/SLSecurityTesting/members", headers=headers)
data = query.json()
fields = ['Name', 'Type','Admin']
with open('members.csv', 'w', newline='') as result:
     csvfile = csv.writer(result, delimiter=",")
     csvfile.writerow(fields)
     for event in data:
          memberslist = 'User :', event['login'],'Type :',event['type']+'Admin :', event['site_admin']
          Login = str(event['login'])
          Type = str(event['type'])
          Admin = str(event['site_admin'])
          print (memberslist)
          #csvwriter = csv.writer(csvfile)
          csvfile.writerow ([Login,Type, Admin])
