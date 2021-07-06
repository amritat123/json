import json
dict={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
my_file=open("sort_key.json","w")
json.dump(dict,my_file,sort_keys=True, indent=4)
my_file.close()
