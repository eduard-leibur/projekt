maatriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
indeksid = input("Sisestage indeksid: ")
esimene_indeks = int(indeksid.split()[0])
teine_indeks = int(indeksid.split()[1])

for rida in maatriks:
    esimene = rida[esimene_indeks]
    teine = rida[teine_indeks]

    rida[esimene_indeks] = teine
    rida[teine_indeks] = esimene

print(maatriks)
