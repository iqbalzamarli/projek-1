import json

dictionary = {
    "name": "iqbal",
    "age": 20,
    "city": "Pesisir Selatan"
}

with open("contoh.json", "w") as outfile:
    json.dump(dictionary, outfile)