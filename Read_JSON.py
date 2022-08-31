import json

with open('Contoh.json','r') as openfile:

    json_object = json.load(openfile)

print(json_object)
print(type(json_object))