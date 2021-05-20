import json
jsonRow = '{"name": "hello"}'
obj = {'a':1,'b':2}
print(json.loads(jsonRow))
print(json.dumps(obj))