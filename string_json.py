import json
dict1={"name":"shikha",
"age":23,
"topic":"python"}
my_file=open("string_json.json","w")
a=json.dumps(dict1)
print(a)
my_file.close()
