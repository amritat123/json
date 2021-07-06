import json 
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]

list5=["name","Designation","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        dict1[list5[i]]=list1[j]
        dict2[list5[i]]=list2[j]
        dict3[list5[i]]=list3[j]
        dict4[list5[i]]=list4[j]
       
        j+=1
    dict5["emp1"]=dict1
    dict5["emp2"]=dict2
    dict5["emp3"]=dict3
    dict5["emp4"]=dict4
    i+=1
dict5=json.dumps(dict5,indent=5)
print(dict5)
print(type(dict5))
