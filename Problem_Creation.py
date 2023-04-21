#!/bin/env python

import requests
import json

incident_number = "@option.incident@"
token_snow = "Basic @option.token_snow@"

uri = "https://disneyuat.service-now.com/api/now/v2/table/incident"
fields = "?sysparm_fields=number,priority,assignment_group.name,cmdb_ci.name"
query = "&sysparm_query=number={}".format(incident_number)
limit = "&sysparm_limit=10"

headers = {
            "Accept": "application/json",
            "Authorization": token_snow
        }

url = uri+fields+query+limit  

print("API Endpoint: {}".format(url))
print("Fetchng the Details for: {}".format(incident_number))

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
    