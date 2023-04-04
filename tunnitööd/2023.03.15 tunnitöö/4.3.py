def summa(järjend):
    if len(järjend) == 0:
        return 0
    elif järjend[0] % 2 == 0:
        return järjend[0] + summa(järjend[1:])
    elif järjend[0] % 2 != 0:
        return järjend[0] * 2 + summa(järjend[1:])
    else:
        quit(1)


print(summa([2, 8, 3, 7, 10]))
