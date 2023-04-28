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


def indikaator_esile(indikaator):
    peida_indikaatorid()
    indikaator.configure(bg="blue")


def peida_indikaatorid():
    soovikiri_indikaator.configure(bg=valikuriba_värv)
    vaadatud_indikaator.configure(bg=valikuriba_värv)
    nimekiri1_indikaator.configure(bg=valikuriba_värv)
    nimekiri2_indikaator.configure(bg=valikuriba_värv)


kuva = tkinter.Tk()
kuva.title("Filmid")
geomeetria_keskele(kuva, 1000, 700)

with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
print(kasutaja + "'i filmid.")


valikuriba_värv = "lightblue"
valikuriba = tkinter.Frame(kuva, bg=valikuriba_värv)
valikuriba.pack_propagate(False)
valikuriba.pack(side="top", fill="x")
valikuriba.configure(width=1000, height=150)

nuppude_vahe = 30
nuppude_laius = -100

soovikiri_nupp = tkinter.Button(valikuriba, text="Soovikiri", command=lambda: indikaator_esile(soovikiri_indikaator))
soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

vaadatud_nupp = tkinter.Button(valikuriba, text="Vaadatud", command=lambda: indikaator_esile(vaadatud_indikaator))
vaadatud_nupp.pack(side=tkinter.LEFT, padx=0)

nimekiri1_nupp = tkinter.Button(valikuriba, text="Nimekiri 1", command=lambda: indikaator_esile(nimekiri1_indikaator))
nimekiri1_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

nimekiri2_nupp = tkinter.Button(valikuriba, text="Nimekiri 2", command=lambda: indikaator_esile(nimekiri2_indikaator))
nimekiri2_nupp.pack(side=tkinter.LEFT, padx=0)
valikuriba.update()


soovikiri_indikaator = tkinter.Label(valikuriba, bg=valikuriba_värv)
soovikiri_indikaator.place(x=nuppude_vahe, y=45, width=soovikiri_nupp.winfo_width(), height=6)

vaadatud_indikaator = tkinter.Label(valikuriba, bg=valikuriba_värv)
vaadatud_indikaator.place(x=2*nuppude_vahe+soovikiri_nupp.winfo_width(), y=45,
                          width=vaadatud_nupp.winfo_width(), height=6)

nimekiri1_indikaator = tkinter.Label(valikuriba, bg=valikuriba_värv)
nimekiri1_indikaator.place(x=3*nuppude_vahe+soovikiri_nupp.winfo_width()+vaadatud_nupp.winfo_width(), y=45,
                           width=nimekiri1_nupp.winfo_width(), height=6)

nimekiri2_indikaator = tkinter.Label(valikuriba, bg=valikuriba_värv)
nimekiri2_indikaator.place(x=4 * nuppude_vahe + soovikiri_nupp.winfo_width() +
                           vaadatud_nupp.winfo_width() + nimekiri1_nupp.winfo_width(),
                           y=45, width=nimekiri2_nupp.winfo_width(), height=6)


väljumisnupp = tkinter.Button(valikuriba, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack(side=tkinter.RIGHT, padx=nuppude_vahe)


põhikuva = tkinter.Frame(kuva, bg="lightgreen")
põhikuva.pack(side="top", fill="both")
põhikuva.pack_propagate(False)
põhikuva.configure(width=1000, height=550)

kuva.mainloop()
