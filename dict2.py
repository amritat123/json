d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'c':400}
print(d1)
print(d2)
import json
with open("dict2.json","w")as file:
    data=json.dump(d1,file,indent=4)
    print(data)
file.close()





