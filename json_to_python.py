import json
dict_1={"name": "David","class":"I","age": 6}

my_file=open("json_to_python.json","w")
json.dump(dict_1,my_file,indent=2)
my_file.close()
print(type(dict_1))
file=open("json_to_python.json","r")
data=json.load(file)
print(data)
file.close()



