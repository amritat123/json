import json

my_json="""{"key1": "value1", "key2": "value2"}"""

data = json.loads(my_json)
print(data['key2'])

