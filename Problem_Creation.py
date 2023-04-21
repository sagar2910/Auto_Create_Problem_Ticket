#!/bin/env python

import requests
import json

#To take Incident number as a input
incident_number = "@option.incident@"

#To Fetch the service now token
token_snow = "Basic @option.token_snow@"

#Header Information
headers = {
            "Accept": "application/json",
            "Authorization": token_snow
        }

#Define a Global variable url so we can acess it within a class,class methods and outside a class.
url=''

#Class to create an API based on fields & query parameters
class API():

    # init method or constructor
    def __init__(self, uri, fields, query, limit):
        self.uri = uri
        self.fields = fields
        self.query = query
        self.limit = limit

    def build(self):
        url = self.uri + self.fields + self.query + self.limit
        print("API Endpoint: {}".format(url))


uri = "https://disneyuat.service-now.com/api/now/v2/table/incident"
fields = "?sysparm_fields=number,priority,assignment_group.name,cmdb_ci.name"
query = "&sysparm_query=number={}".format(incident_number)
limit = "&sysparm_limit=10"

#Passing required parameter to calss.
api_endpoint = API(uri,fields,query,limit)

#Calling API class method - build
api_endpoint.build()

print("Fetchng the Details for: {}".format(incident_number))

try:
    #Below statement may throw an error so putting in in a try block
    response = requests.get(url=url, headers=headers)
    incidents = response.json()["result"]
    print("Response Status Code: {}".format(response.status_code))
    print
    print("Details fetched from Incident:")
    print
    for record in incidents:
        print(record)
        print("Assignment Group: {}".format(record["assignment_group.name"]))
        print("Priority: {}".format(record["priority"]))
        print("Incident Number: {}".format(record["number"]))
        print("Configuration Item: {}".format(record["cmdb_ci.name"]))
except Exception as e:
    #Exception is a base class for all exception so whatever exception we would encouter it will be catch by this except block.
    print(e)
    