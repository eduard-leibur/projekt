def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    with open(laste_fail, "r") as laste_andmed:
        vanemad = {}
        for rida in laste_andmed:
            vanem = rida.split()[0]
            laps = rida.split()[1]
            if vanem not in vanemad:
                vanemad[vanem] = []
            vanemad[vanem].append(laps)

    with open(nimede_fail, "r") as nimede_andmed:
        nimed = {}
        for rida in nimede_andmed:
            isikukood = rida.split()[0]
            eesnimi = rida.split()[1]
            perenimi = rida.split()[2]
            nimi = eesnimi + " " + perenimi
            nimed[isikukood] = nimi

    nimedega_vanemad = {}
    for vanem in vanemad:
        vanema_nimi = nimed[vanem]
        laste_isikukoodid = vanemad[vanem]
        laste_nimed = []
        for isikukood in laste_isikukoodid:
            laps = nimed[isikukood]
            laste_nimed.append(laps)
        nimedega_vanemad[vanema_nimi] = laste_nimed

    return nimedega_vanemad


sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for lapsevanem in sõnastik:
    sõne = lapsevanem + ": "
    for lapsuke in sõnastik[lapsevanem]:
        if lapsuke == sõnastik[lapsevanem][-1]:
            sõne += lapsuke
        else:
            sõne += lapsuke + ", "
    print(sõne)
