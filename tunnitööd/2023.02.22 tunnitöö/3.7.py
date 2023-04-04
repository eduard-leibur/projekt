maatriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# a
def peadiagonaal(sisend_maatriks):
    summa = 0
    for rida in range(len(sisend_maatriks)):
        summa += sisend_maatriks[rida][rida]
    return summa

# b
def kõrvaldiagonaal(sisend_maatriks):
    summa = 0
    for rida in range(len(sisend_maatriks)):
        summa += sisend_maatriks[rida][len(sisend_maatriks) - rida - 1]
    return summa

# c
"""def peadiagonaalist_all(sisend_maatriks):
    summa = 0
    for rida in range(len(sisend_maatriks)):
        if rida > 0:
            for arv in range(len(maatriks[rida]) - rida):
                summa += arv
    return summa"""


print("Peadiagonaal", peadiagonaal(maatriks))
print("Kõrvaldiagonaal", kõrvaldiagonaal(maatriks))
"""print("Allpool peadiagonaali", peadiagonaalist_all(maatriks))"""
