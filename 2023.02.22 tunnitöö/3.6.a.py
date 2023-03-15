maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
indeksid = input("Sisestage indeksid: ")
esimene = int(indeksid.split()[0])
teine = int(indeksid.split()[1])

esimene_element = maatriks[esimene]
teine_element = maatriks[teine]

maatriks[esimene] = teine_element
maatriks[teine] = esimene_element

print(maatriks)
