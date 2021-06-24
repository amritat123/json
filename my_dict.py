import json
my_dict={"name":"amrita","age":18,"course":"python"}
my_file=open("my_dict.json","w")
json.dump(my_dict,my_file,indent=4)
my_file.closed()