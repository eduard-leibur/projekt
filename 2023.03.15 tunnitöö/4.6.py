def summa(järjend, indeks):
    if len(järjend) == 0:
        return 0
    else:
        return järjend[0] * indeks + summa(järjend[1:], indeks + 1)


print(summa([2, 5, 0, 1, 3], 1))
