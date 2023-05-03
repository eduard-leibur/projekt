import json
import tkinter
from tkinter import scrolledtext
from funktsioonid.geomeetria import geomeetria_keskele


def lehe_avamine(indikaator, nimekiri):
    peida_indikaatorid()
    indikaator.configure(bg="blue")
    tühjenda_põhikuva()
    lehe_loomine(nimekiri)


def lehe_loomine(nimekiri):
    leht = tkinter.Frame(põhikuva, bg="blue")

    lisamise_raami_värv = "yellow"
    lisamise_raam = tkinter.Frame(leht, bg=lisamise_raami_värv)

    lisamise_silt = tkinter.Label(lisamise_raam, text="Uue kirje sisestamine:",
                                  font=("calibre", 14), bg=lisamise_raami_värv)
    lisatud_kirje = tkinter.StringVar()
    lisatud_kirje.set("Lisatava raamatu pealkiri")
    lisamise_kast = tkinter.Entry(lisamise_raam, textvariable=lisatud_kirje, font=("calibre", 14))
    lisamise_nupp = tkinter.Button(lisamise_raam, text="Lisa",
                                   command=lambda: kirje_lisamine(lisatud_kirje.get(), nimekiri))

    lisamise_raam.pack(side=tkinter.BOTTOM, fill="x")

    lisamise_silt.pack(side=tkinter.LEFT)
    lisamise_kast.pack(side=tkinter.LEFT, pady=5)
    lisamise_kast.pack_propagate(False)
    lisamise_kast.configure(width=30)
    lisamise_nupp.pack(side=tkinter.LEFT, padx=10)

    kustutamise_silt = tkinter.Label(lisamise_raam, text="Kustutatava kirje nr:",
                                     font=("calibre", 14), bg=lisamise_raami_värv)
    kustutatud_kirje = tkinter.StringVar()
    kustutamise_kast = tkinter.Entry(lisamise_raam, textvariable=kustutatud_kirje, font=("calibre", 14))
    kustutamise_nupp = tkinter.Button(lisamise_raam, text="Kustuta",
                                      command=lambda: kirje_kustutamine(kustutatud_kirje.get(), nimekiri))

    kustutamise_nupp.pack(side=tkinter.RIGHT, padx=10)
    kustutamise_kast.pack(side=tkinter.RIGHT)
    kustutamise_kast.pack_propagate(False)
    kustutamise_kast.configure(width=7)
    kustutamise_silt.pack(side=tkinter.RIGHT)

    nimekirja_kast = scrolledtext.ScrolledText(leht, font=("Bold", 16))

    if kasutaja == "":
        print("Pole kasutajat!")
        quit(2)     # 2 - pole kasutajat

    nimekirjade_asukoht = "andmed/kasutajad/" + kasutaja + "/raamatud.json"
    with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
        nimekirjade_sõnastik = json.load(nimekirjade_fail)

    i = 1
    for raamat in nimekirjade_sõnastik[nimekiri]:
        raamat = str(str(i) + ". " + raamat + "\n")
        nimekirja_kast.insert(tkinter.END, raamat)
        i += 1

    nimekirja_kast.pack(fill="both", expand=True)
    nimekirja_kast.configure(state="disabled", spacing1=10)
    leht.pack(fill="both")


def tühjenda_põhikuva():
    for leht in põhikuva.winfo_children():
        leht.destroy()


def peida_indikaatorid():
    soovikiri_indikaator.configure(bg=valikuriba_värv)
    vaadatud_indikaator.configure(bg=valikuriba_värv)
    nimekiri1_indikaator.configure(bg=valikuriba_värv)
    nimekiri2_indikaator.configure(bg=valikuriba_värv)


def kirje_lisamine(kirje, nimekiri):
    nimekirjade_asukoht = "andmed/kasutajad/" + kasutaja + "/raamatud.json"
    with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
        nimekirjad = json.load(nimekirjade_fail)
    nimekirjad[nimekiri].append(kirje)
    with open(nimekirjade_asukoht, "w") as nimekirjade_fail:
        json.dump(nimekirjad, nimekirjade_fail)
    print(kirje + " lisatud nimekirja " + nimekiri)
    tühjenda_põhikuva()
    lehe_loomine(nimekiri)


def kirje_kustutamine(kirje_nr, nimekiri):
    nimekirjade_asukoht = "andmed/kasutajad/" + kasutaja + "/raamatud.json"
    with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
        nimekirjad = json.load(nimekirjade_fail)

    kirje_nr = int(kirje_nr) - 1
    del nimekirjad[nimekiri][kirje_nr]

    with open(nimekirjade_asukoht, "w") as nimekirjade_fail:
        json.dump(nimekirjad, nimekirjade_fail)
    print("Kirje nr. " + str(kirje_nr + 1) + " kustutatud nimekirjast " + nimekiri)
    tühjenda_põhikuva()
    lehe_loomine(nimekiri)


kuva = tkinter.Tk()
kuva.title("Raamatud")
geomeetria_keskele(kuva, 1000, 700)

with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
print(kasutaja + "'i raamatud.")


valikuriba_värv = "lightblue"
valikuriba = tkinter.Frame(kuva, bg=valikuriba_värv)
valikuriba.pack_propagate(False)
valikuriba.pack(side="top", fill="x")
valikuriba.configure(width=1000, height=150)

nuppude_vahe = 30
nuppude_laius = -100

soovikiri_nupp = tkinter.Button(valikuriba, text="Soovikiri",
                                command=lambda: lehe_avamine(soovikiri_indikaator, "Soovikiri"))
soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

vaadatud_nupp = tkinter.Button(valikuriba, text="Vaadatud",
                               command=lambda: lehe_avamine(vaadatud_indikaator, "Vaadatud"))
vaadatud_nupp.pack(side=tkinter.LEFT, padx=0)

nimekiri1_nupp = tkinter.Button(valikuriba, text="Nimekiri 1",
                                command=lambda: lehe_avamine(nimekiri1_indikaator, "Nimekiri 1"))
nimekiri1_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

nimekiri2_nupp = tkinter.Button(valikuriba, text="Nimekiri 2",
                                command=lambda: lehe_avamine(nimekiri2_indikaator, "Nimekiri 2"))
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

kasutaja_sildi_tekst = "Kasutaja: " + kasutaja
kasutaja_silt = tkinter.Label(valikuriba, text=kasutaja_sildi_tekst, font=("Bold", 12))
kasutaja_silt.pack(side=tkinter.RIGHT)


põhikuva_värv = "lightgreen"
põhikuva = tkinter.Frame(kuva, bg=põhikuva_värv)
põhikuva.pack(side="top", fill="both")
põhikuva.pack_propagate(False)
põhikuva.configure(width=1000, height=550)

põhikuva_silt = tkinter.Label(põhikuva, text="Palun valige ülevalt nimekiri.", font=("Bold", 12), bg=põhikuva_värv)
põhikuva_silt.pack(fill="none", expand=True)

kuva.mainloop()
