import tkinter
from funktsioonid.geomeetria import geomeetria_keskele


def soovikiri_leht():
    soovikiri = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(soovikiri, text="Soovikiri", font=("Bold", 12), pady=20)
    pealkiri.pack()

    soovikiri.pack()
    soovikiri.pack_propagate(False)
    soovikiri.configure(width=1000, height=550)


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

soovikiri_nupp = tkinter.Button(valikuriba, text="Soovikiri", command=lambda: soovikiri_leht())
soovikiri_nupp.place(x=20, y=20)

väljumisnupp = tkinter.Button(valikuriba, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack(side="right")


põhikuva = tkinter.Frame(kuva, bg="lightgreen")
põhikuva.pack(side="top", fill="both")
põhikuva.pack_propagate(False)
põhikuva.configure(width=1000, height=550)

kuva.mainloop()
