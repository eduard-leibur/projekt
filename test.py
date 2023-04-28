import json
import tkinter


def soovikiri_leht():
    soovikiri = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(soovikiri, text="Soovikiri", font=("Bold", 12), pady=20)
    pealkiri.pack()

    soovikiri.pack()
    soovikiri.pack_propagate(False)
    soovikiri.configure(width=1000, height=550)


def uus_leht(leht):
    tekst = leht
    leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(leht, text=tekst, font=("Bold", 12), pady=20)
    pealkiri.pack()

    leht.pack()
    leht.pack_propagate(False)
    leht.configure(width=1000, height=550)


kuva = tkinter.Tk()
kuva.title("Filmid")
kuva.configure(width=1000, height=700)

with open("test_nimekirjad.json", "r") as nimekirjade_fail:
    nimekirjad = json.load(nimekirjade_fail)


põhikuva = tkinter.Frame(kuva, bg="lightgreen")
põhikuva.pack(side="bottom", fill="both")
põhikuva.pack_propagate(False)
põhikuva.configure(width=1000, height=550)


valikuriba = tkinter.Frame(kuva, bg="lightblue")

soovikiri_nupp = tkinter.Button(valikuriba, text="Soovikiri", command=lambda: soovikiri_leht())
soovikiri_nupp.place(x=20, y=20)

väljumisnupp = tkinter.Button(valikuriba, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack(side="right")

i = 1
for nimekiri in nimekirjad:
    nimekirja_nupp = tkinter.Button(valikuriba, text=nimekiri,
                                    command=lambda: uus_leht(nimekiri))
    nimekirja_nupp.place(x=i*100+20, y=20)
    i += 1

valikuriba.pack_propagate(False)
valikuriba.configure(width=1000, height=150)
valikuriba.pack(side="top", fill="x")

kuva.mainloop()
