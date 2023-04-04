from math import sqrt

järjend = [1, 2, 3, 4, 5, 6]
ruutude_summa = 0
for i in järjend:
    ruutude_summa += pow(i, 2)
ruutude_keskmine = ruutude_summa / len(järjend)
ruutkeskmine = sqrt(ruutude_keskmine)
print(ruutkeskmine)
