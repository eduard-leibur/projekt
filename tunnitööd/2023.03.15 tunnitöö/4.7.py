def korrutis(järjend):
    if len(järjend) == 0:
        return 1
    elif järjend[0] == 0:
        return korrutis(järjend[1:])
    else:
        return järjend[0] * korrutis(järjend[1:])


print(korrutis([0.0, 4.0, 2.7]))
