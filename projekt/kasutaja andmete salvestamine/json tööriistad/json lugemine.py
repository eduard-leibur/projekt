import json

with open("../kasutajate andmed.json", "r") as fail:
    sõnastik = json.load(fail)

print(sõnastik)
