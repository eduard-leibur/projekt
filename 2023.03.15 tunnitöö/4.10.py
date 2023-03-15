# a
def nullid_alguses(järjend):
    if len(järjend) == 0:
        return 0
    elif järjend[0] == 0:
        return 1 + nullid_alguses(järjend[1:])
    else:
        return 0


print(nullid_alguses([0, 0, 0, 2, 3]))

# b
def nullid_lõpus(järjend):
    if len(järjend) == 0:
        return 0
    elif järjend[-1] == 0:
        return 1 + nullid_lõpus(järjend[:-1])
    else:
        return 0


print(nullid_lõpus([0, 1, 4, 0, 0]))
