import json 
dict1={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
print(dict1)
user=input("add or buy=")
item=input("which item you want to add or buy= ")
quantity=int(input("how many item you wanna add or buy= "))
if user=="add":
    dict1["shopping_list"][item]=quantity
    print(dict1)
else:
    dict1["shopping_list"].pop(item)
    print(dict1)
shoping_file=open("shoping_lists.json","w")
json.dump(dict1,shoping_file,indent=2)
    