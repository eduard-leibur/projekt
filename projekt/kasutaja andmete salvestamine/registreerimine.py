import json

with open("kasutajate andmed.json", "r") as fail_sisse:
    sõnastik = json.load(fail_sisse)

kasutajanimi = input("Kasutajanimi: ")
parool = input("Parool: ")
sõnastik[kasutajanimi] = parool

with open("kasutajate andmed.json", "w") as fail_välja:
    json.dump(sõnastik, fail_välja)
