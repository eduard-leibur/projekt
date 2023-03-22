def a(sõne):
    lõplik_sõne = ""
    for i in range(len(sõne)):
        täht = sõne[i]
        if täht not in sõne[:i] or täht not in sõne[i + 1:]:
            lõplik_sõne += täht
    return lõplik_sõne


def b(sõne):
    tähed = []
    lõplik_sõne = ""
    for täht in sõne:
        if täht not in tähed:
            lõplik_sõne += täht
            tähed.append(täht)
    return lõplik_sõne


def c(sõne):
    lõplik_sõne = ""
    for i in range(len(sõne)):
        täht = sõne[i]
        if i > 1 and i + 3 <= len(sõne):
            if täht != sõne[i - 2] and täht != sõne[i + 2]:
                lõplik_sõne += täht
        elif i < 2:
            if täht != sõne[i + 2]:
                lõplik_sõne += täht
        else:
            if täht != sõne[i - 2]:
                lõplik_sõne += täht
    return lõplik_sõne


def d(sõne):
    lõplik_sõne = ""
    for i in range(len(sõne)):
        kas_täht_läheb = True
        if sõne[i] == "a":
            if i + 1 < len(sõne) and sõne[i + 1] == "j":
                kas_täht_läheb = False
                if i >= 1 and sõne[i - 1] == "a":
                    kas_täht_läheb = True
        elif sõne[i] == "j":
            if i >= 1 and sõne[i - 1] == "a":
                kas_täht_läheb = False
                if i >= 2 and sõne[i - 2] == "a":
                    kas_täht_läheb = True
        else:
            kas_täht_läheb = True
        if kas_täht_läheb:
            lõplik_sõne += sõne[i]
    return lõplik_sõne


print(a("cacdacea"))
print(b("Java keel on tore"))
print(c("vanaema"))
print(d("maja"))
print(d("maaja"))
