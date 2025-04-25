import json
a = '{"name": "Bob", "languages": "English"}'
y = json.loads(a)
print("JSON string = ", y)
print()
f = open ("C:/Users/nithy/Downloads/data.json", "r")
data = json.loads(f.read())
for i in data['emp_details']:
    print(i)

import json
a = '{"name": "Bob", "languages": "English"}'
y = json.loads(a)
print("JSON string = ", y)
print()
f = open ("C:/Users/nithy/Downloads/data.json", "r")
data = json.loads(f.read())
for i in data['emp_details']:
    print(i)
    f.close()

