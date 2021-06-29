import json 
dict={"a":  1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}
dict1={}
for i in dict:
    if i in dict:
        dict1[i]=dict[i]    
print(dict1)
files=open("unique_keys.json","w")
json.dump(dict,files,indent=3)
files.close()
