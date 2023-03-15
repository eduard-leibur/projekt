maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transponeeritud = []

for rida in range(len(maatriks)):
    transponeeritud.append([])

for rida in range(len(maatriks)):
    for arv in range(len(maatriks[rida])):
        transponeeritud[arv].append(maatriks[rida][arv])

print(transponeeritud)
