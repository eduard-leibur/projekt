sõne = input("Sisestage sõne: ")
tähed = []
for täht in sõne:
    if täht in tähed:
        print("Ei ole heterogramm.")
        quit(1)
    else:
        tähed.append(täht)
print("On heterogramm.")
