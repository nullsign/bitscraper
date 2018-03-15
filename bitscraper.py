#!/usr/bin/python

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# elinksrings in the requests library, used for making HTTP calls
import requests


url = 'https://[BITBUCKET URL GOES HERE'

# Loads the JSON from the HTTP endpoint
response = requests.get(url=url, verify=False)

# Parses the HTTP response into a Python dictionary object based on JSON structure
jsondata = response.json()
# print jsondata

# Declares an empty dictionary that we're going to populate
projects = {}

# Traverse all of the sub-objects of the JSON key named "values", and for each one...
for record in jsondata["values"]:

    # Create an entry in the projects dictionary using the "key" field from the record, with the value
    # being the full JSON object (with all of the other fields, "key" included)
    projects[record["key"]] = record

# Prints the lookup keys from the projects dictionary -- which happen to also be the "key" fields from
# all of the records in the dictionary since we set them to that value on the previous line.
# 
# print(projects.keys())

### Notes
# If you just iterate `projects` you will get the key strings. 
# If you iterate `projects.values()` you will get the actual stored objects.
# So if you just want to print the names, it's easier to iterate the keys. 
# If you want to actually access their other properties, use the `.values()` collection to make it simpler.

### print list
# for record in jsondata["values"]:
#    print(record["name"])

file = open(("bitsplatter.log"), "w")

print "creating bitsplatter.log \n"

for record in jsondata["values"]:
    response2 = requests.get("https://git.splunk.com/rest/api/1.0/projects/" + record["key"] + "/repos", verify=False)
    responsejson = response2.json()
   
    for subrecord in responsejson["values"]:
       file.write([x for x in subrecord["links"]["clone"] if x["href"].startswith("http")][0]["href"] + "\n")
