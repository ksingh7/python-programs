import json

# Open file
file = open('/Users/ksingh/temp/data.json')
# Loading the contents of JSON file using load method
JsonToString = json.load(file)


# Another way to do this , is open file , read file and use json.load method
# json_file = file.read()
# JsonToString = json.load(json_file)

# Printing JSON content as python values

#print JsonToString
print JsonToString["deployments_url"]
print JsonToString["has_wiki"]
print JsonToString["branches_url"]
print JsonToString["permissions"]
print JsonToString["permissions"]["admin"]


# To Dump Python Dictonary Strings in the form of JSON use dumps method

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print stringOfJsonData



