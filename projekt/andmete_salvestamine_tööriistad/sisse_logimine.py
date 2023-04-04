import json

with open("kasutajate andmed.json", "r") as fail:
    andmed = json.load(fail)

print("Sisse logimine.")

while True:
    kasutajanimi = input("Kasutajanimi: ")
    if kasutajanimi == "":
        quit(1)
    parool = input("Parool: ")
    if kasutajanimi in andmed:
        if andmed[kasutajanimi] == parool:
            print("Korras!")
            quit(2)
        else:
            print("Vale parool!\n")
    else:
        print("Sellist kasutajat pole!\n")
