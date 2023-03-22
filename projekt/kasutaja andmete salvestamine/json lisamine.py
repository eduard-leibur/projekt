import json
from registreerimine import registreeritav_kasutaja

with open("kasutajate andmed.json", "r") as fail_sisse:
    sõnastik = json.load(fail_sisse)

sõnastik[registreeritav_kasutaja.kasutajanimi] = registreeritav_kasutaja.parool

with open("kasutajate andmed.json", "w") as fail_välja:
    json.dump(sõnastik, fail_välja)
