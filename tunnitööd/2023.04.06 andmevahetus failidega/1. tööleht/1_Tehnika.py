with open("tehnika.txt", "r") as fail:
    for rida in fail:
        rea_osad = rida.split()
        muutus = int(rea_osad[-1]) - int(rea_osad[1])
        if muutus > 10:
            print(rea_osad[0] + " tõusis " + str(muutus) + "% võrra.")
