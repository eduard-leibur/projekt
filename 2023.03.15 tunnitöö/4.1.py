# a
def summa(arvud):
    if len(arvud) == 0:  # baas
        return 0
    else:  # samm
        return arvud[0] + summa(arvud[1:])


print(summa([1, 4, 6, 7]))


# b
def miinimum(järjend):
    if len(järjend) == 1:
        return järjend[0]
    else:
        pea = järjend[0]
        saba = järjend[1:]
        sabaVahim = miinimum(saba)
        if pea < sabaVahim:
            return pea
        return sabaVahim


print(miinimum([6, 4, 7, 2, 9]))
