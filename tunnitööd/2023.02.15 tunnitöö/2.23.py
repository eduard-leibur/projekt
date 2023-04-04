järjend = [18, 27, 17, 20, 38, 42]


def täisruudud():
    ruudud = []
    for i in range(100):
        ruudud.append(pow(i, 2))
    return ruudud


def täisruudust_5_kaugusel(sisend):
    arvud = []
    for arv in sisend:
        if arv - 5 in täisruudud() or arv + 5 in täisruudud():
            arvud.append(arv)
    return arvud


print(täisruudust_5_kaugusel(järjend))
