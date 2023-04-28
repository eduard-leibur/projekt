import tkinter
from funktsioonid.geomeetria import geomeetria_keskele


def leht_soovikiri():
    soovikiri = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(soovikiri, text="Soovikiri", font=("Bold", 12), pady=20)
    pealkiri.pack()

    soovikiri.pack()
    soovikiri.pack_propagate(False)
    soovikiri.configure(width=1000, height=550)


def leht_vaadatud():
    vaadatud_leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(vaadatud_leht, text="Vaadatud", font=("Bold", 12), pady=20)
    pealkiri.pack()

    vaadatud_leht.pack()
    vaadatud_leht.pack_propagate(False)
    vaadatud_leht.configure(width=1000, height=550)


kuva = tkinter.Tk()
kuva.title("Filmid")
geomeetria_keskele(kuva, 1000, 700)

with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
print(kasutaja + "'i filmid.")


valikuriba = tkinter.Frame(kuva, bg="lightblue")
valikuriba.pack_propagate(False)
valikuriba.pack(side="top", fill="x")
valikuriba.configure(width=1000, height=150)

nuppude_vahe = 30
soovikiri_nupp = tkinter.Button(valikuriba, text="Soovikiri", command=lambda: leht_soovikiri())
soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

vaadatud_nupp = tkinter.Button(valikuriba, text="Vaadatud", command=lambda: leht_vaadatud())
vaadatud_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

väljumisnupp = tkinter.Button(valikuriba, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack(side=tkinter.RIGHT, padx=nuppude_vahe)


põhikuva = tkinter.Frame(kuva, bg="lightgreen")
põhikuva.pack(side="top", fill="both")
põhikuva.pack_propagate(False)
põhikuva.configure(width=1000, height=550)

kuva.mainloop()
