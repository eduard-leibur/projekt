import json

with open("kasutajate andmed.json", "r") as fail:
    andmed = json.load(fail)

print("Sisse logimine.")
kasutajanimi = input("Kasutajanimi: ")
parool = input("Parool: ")

while True:
    if kasutajanimi in andmed:
        if andmed[kasutajanimi] == parool:
            print("Korras!")
            break
        else:
            print("Vale parool!\n")
    else:
        print("Sellist kasutajat pole!\n")
