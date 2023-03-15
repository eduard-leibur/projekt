vanused = [18, 27, 17, 20, 38, 42]
# a
for töötaja in range(len(vanused)):
    print(str(töötaja + 1) + ". töötajal on 65. eluaastani jäänud " +
          str(65 - vanused[töötaja]) + " aastat")

# b
def keskmine_vanus(vanused_sisend):
    return float(sum(vanused_sisend) / len(vanused_sisend))


print("Keskmine:", keskmine_vanus(vanused))

# c
def mediaanvanus(vanused_sisend):
    if len(vanused_sisend) % 2 == 0:
        esimene_liige = vanused_sisend[len(vanused_sisend) // 2 - 1]
        teine_liige = vanused_sisend[len(vanused_sisend) // 2]
        return (esimene_liige + teine_liige) / 2
    else:
        return vanused_sisend[(len(vanused_sisend) + 1) // 2 - 1]


print("Mediaan:", mediaanvanus(vanused))

# d
def alla_neljakümne(sisend):
    noorukid = []
    for tööline in sisend:
        if tööline < 40:
            noorukid.append(tööline)
    return noorukid


print("Alla 40-aastaseid:", len(alla_neljakümne(vanused)))

# e
print("Alla 40 keskmine vanus:", keskmine_vanus(alla_neljakümne(vanused)))

# f
print("Noorim vanus:", min(vanused))
