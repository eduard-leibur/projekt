import tkinter
import json
from tkinter import messagebox
from tkinter import scrolledtext
from projekt.funktsioonid.geomeetria import geomeetria_keskele
from funktsioonid.värvid import *


class Valikud(tkinter.Tk):
    def __init__(self, kasutaja):
        super().__init__()
        self.kasutaja = kasutaja
        self.title("Avakuva")
        geomeetria_keskele(self, 500, 400)

        self.silt = "Kasutaja: " + self.kasutaja
        self.kasutaja_silt = tkinter.Label(self, text=self.silt)
        self.kasutaja_silt.pack()

        kategooriate_pady = 5

        self.filmid = tkinter.Button(self, text="Filmid", command=lambda: self.avamine("Filmid", self.kasutaja,
                                                                                       värv_filmid, "filmid.json",
                                                                                       "filmi", "filmid", "Vaadatud"))
        self.filmid.pack(pady=kategooriate_pady)

        self.raamatud = tkinter.Button(self, text="Raamatud", command=lambda: self.avamine("Raamatud", self.kasutaja,
                                                                                           värv_raamatud,
                                                                                           "raamatud.json",
                                                                                           "raamatu", "raamatud",
                                                                                           "Loetud"))
        self.raamatud.pack(pady=kategooriate_pady)

        self.mängud = tkinter.Button(self, text="Mängud", command=lambda: self.avamine("Mängud", self.kasutaja,
                                                                                       värv_mängud, "mängud.json",
                                                                                       "mängu", "mängud", "Mängitud"))
        self.mängud.pack(pady=kategooriate_pady)

        self.riigid = tkinter.Button(self, text="Riigid", command=lambda: self.avamine("Riigid", self.kasutaja,
                                                                                       värv_riigid, "riigid.json",
                                                                                       "riigi", "riigid", "Käidud"))
        self.riigid.pack(pady=kategooriate_pady)

        self.väljumisnupp = tkinter.Button(self, text="Välju", command=lambda: quit(2))
        self.väljumisnupp.pack(pady=20)

    def avamine(self, pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses, teine_pealkiri):
        if aktiivne_kasutaja == "":
            print("Pole kasutajat!")
            tkinter.messagebox.showwarning(title="Puudub kastuaja", message="Palun logige esmalt sisse kasutajana.")
        else:
            self.destroy()
            kategooria = Kategooria(pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses,
                                    teine_pealkiri)
            kategooria.mainloop()


class Kategooria(tkinter.Tk):
    def __init__(self, pealkiri, kasutaja, valikuriba_värv, fail, osastav_k, mitmuses, teine_pealkiri):
        super().__init__()
        self.title(pealkiri)
        geomeetria_keskele(self, 1000, 700)

        self.pealkiri = pealkiri
        self.kasutaja = kasutaja
        self.fail = fail
        self.osastav_k = osastav_k
        self.mitmuses = mitmuses
        self.teine_pealkiri = teine_pealkiri

        self.valikuriba_värv = valikuriba_värv
        self.põhikuva_värv = "lightgreen"

        self.põhikuva = tkinter.Frame(self, bg=self.põhikuva_värv)
        self.valikuriba = tkinter.Frame(self, bg=valikuriba_värv)

        self.soovikiri_indikaator = tkinter.Label(self.valikuriba, bg=valikuriba_värv)
        self.vaadatud_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri1_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri2_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)

        print(kasutaja + "'i " + self.mitmuses)

        self.valikuriba.pack_propagate(False)
        self.valikuriba.pack(side="top", fill="x")
        self.valikuriba.configure(width=1000, height=150)

        nuppude_vahe = 30

        self.soovikiri_nupp = tkinter.Button(self.valikuriba, text="Soovikiri",
                                             command=lambda: self.lehe_avamine(self.soovikiri_indikaator, "Soovikiri"))
        self.soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        self.vaadatud_nupp = tkinter.Button(self.valikuriba, text=self.teine_pealkiri,
                                            command=lambda: self.lehe_avamine(self.vaadatud_indikaator,
                                                                              self.teine_pealkiri))
        self.vaadatud_nupp.pack(side=tkinter.LEFT, padx=0)

        self.nimekiri1_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 1",
                                             command=lambda: self.lehe_avamine(self.nimekiri1_indikaator, "Nimekiri 1"))
        self.nimekiri1_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        self.nimekiri2_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 2",
                                             command=lambda: self.lehe_avamine(self.nimekiri2_indikaator, "Nimekiri 2"))
        self.nimekiri2_nupp.pack(side=tkinter.LEFT, padx=0)
        self.valikuriba.update()

        self.soovikiri_indikaator.place(x=nuppude_vahe, y=45, width=self.soovikiri_nupp.winfo_width(), height=6)

        self.vaadatud_indikaator.place(x=2 * nuppude_vahe + self.soovikiri_nupp.winfo_width(), y=45,
                                       width=self.vaadatud_nupp.winfo_width(), height=6)

        self.nimekiri1_indikaator.place(x=3 * nuppude_vahe + self.soovikiri_nupp.winfo_width() +
                                        self.vaadatud_nupp.winfo_width(),
                                        y=45, width=self.nimekiri1_nupp.winfo_width(), height=6)

        self.nimekiri2_indikaator.place(x=4 * nuppude_vahe + self.soovikiri_nupp.winfo_width() +
                                        self.vaadatud_nupp.winfo_width() + self.nimekiri1_nupp.winfo_width(),
                                        y=45, width=self.nimekiri2_nupp.winfo_width(), height=6)

        self.väljumisnupp = tkinter.Button(self.valikuriba, text="Välju", command=lambda: quit(1))  # 1 nupust väljumine
        self.väljumisnupp.pack(side=tkinter.RIGHT, padx=nuppude_vahe)

        self.tagasinupp = tkinter.Button(self.valikuriba, text="Tagasi", command=self.tagasi)
        self.tagasinupp.pack(side=tkinter.RIGHT)

        kasutaja_sildi_tekst = "Kasutaja: " + kasutaja
        self.kasutaja_silt = tkinter.Label(self.valikuriba, text=kasutaja_sildi_tekst, font=("Bold", 12))
        self.kasutaja_silt.pack(side=tkinter.RIGHT, padx=nuppude_vahe)

        self.põhikuva.pack(side="top", fill="both")
        self.põhikuva.pack_propagate(False)
        self.põhikuva.configure(width=1000, height=550)

        self.põhikuva_silt = tkinter.Label(self.põhikuva, text="Palun valige ülevalt nimekiri.",
                                           font=("Bold", 12), bg=self.põhikuva_värv)
        self.põhikuva_silt.pack(fill="none", expand=True)

    def lehe_avamine(self, indikaator, nimekiri):
        self.peida_indikaatorid()
        indikaator.configure(bg="blue")
        self.tühjenda_põhikuva()
        self.lehe_loomine(nimekiri)

    def lehe_loomine(self, nimekiri):
        leht = tkinter.Frame(self.põhikuva, bg="blue")

        lisamise_raami_värv = "yellow"
        lisamise_raam = tkinter.Frame(leht, bg=lisamise_raami_värv)

        lisamise_silt = tkinter.Label(lisamise_raam, text="Uue kirje sisestamine:",
                                      font=("calibre", 14), bg=lisamise_raami_värv)

        lisamise_kast = tkinter.Entry(lisamise_raam, font=("calibre", 14))
        lisamise_nupp = tkinter.Button(lisamise_raam, text="Lisa",
                                       command=lambda: self.kirje_lisamine(lisamise_kast.get(), nimekiri))

        lisamise_raam.pack(side=tkinter.BOTTOM, fill="x")

        lisamise_silt.pack(side=tkinter.LEFT)
        lisamise_kast.pack(side=tkinter.LEFT, pady=5)
        lisamise_kast.pack_propagate(False)
        lisamise_kast.configure(width=30)
        lisamise_nupp.pack(side=tkinter.LEFT, padx=10)

        kustutamise_silt = tkinter.Label(lisamise_raam, text="Kustutatava kirje nr:",
                                         font=("calibre", 14), bg=lisamise_raami_värv)
        kustutamise_kast = tkinter.Entry(lisamise_raam, font=("calibre", 14))
        kustutamise_nupp = tkinter.Button(lisamise_raam, text="Kustuta",
                                          command=lambda: self.kirje_kustutamine(kustutamise_kast.get(), nimekiri))

        kustutamise_nupp.pack(side=tkinter.RIGHT, padx=10)
        kustutamise_kast.pack(side=tkinter.RIGHT)
        kustutamise_kast.pack_propagate(False)
        kustutamise_kast.configure(width=7)
        kustutamise_silt.pack(side=tkinter.RIGHT)

        nimekirja_kast = scrolledtext.ScrolledText(leht, font=("Bold", 16))

        nimekirjade_asukoht = "andmed/kasutajad/" + self.kasutaja + "/" + self.fail
        with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
            nimekirjade_sõnastik = json.load(nimekirjade_fail)

        i = 1
        for element in nimekirjade_sõnastik[nimekiri]:
            element = str(str(i) + ". " + element + "\n")
            nimekirja_kast.insert(tkinter.END, element)
            i += 1

        nimekirja_kast.pack(fill="both", expand=True)
        nimekirja_kast.configure(state="disabled", spacing1=10)
        leht.pack(fill="both")

    def tühjenda_põhikuva(self):
        for leht in self.põhikuva.winfo_children():
            leht.destroy()

    def peida_indikaatorid(self):
        self.soovikiri_indikaator.configure(bg=self.valikuriba_värv)
        self.vaadatud_indikaator.configure(bg=self.valikuriba_värv)
        self.nimekiri1_indikaator.configure(bg=self.valikuriba_värv)
        self.nimekiri2_indikaator.configure(bg=self.valikuriba_värv)

    def kirje_lisamine(self, kirje, nimekiri):
        nimekirjade_asukoht = "andmed/kasutajad/" + self.kasutaja + "/" + self.fail
        with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
            nimekirjad = json.load(nimekirjade_fail)
        nimekirjad[nimekiri].append(kirje)
        with open(nimekirjade_asukoht, "w") as nimekirjade_fail:
            json.dump(nimekirjad, nimekirjade_fail)
        print(kirje + " lisatud nimekirja " + nimekiri)
        self.tühjenda_põhikuva()
        self.lehe_loomine(nimekiri)

    def kirje_kustutamine(self, kirje_nr, nimekiri):
        nimekirjade_asukoht = "andmed/kasutajad/" + self.kasutaja + "/" + self.fail
        with open(nimekirjade_asukoht, "r") as nimekirjade_fail:
            nimekirjad = json.load(nimekirjade_fail)

        kirje_nr = int(kirje_nr) - 1
        del nimekirjad[nimekiri][kirje_nr]

        with open(nimekirjade_asukoht, "w") as nimekirjade_fail:
            json.dump(nimekirjad, nimekirjade_fail)
        print("Kirje nr. " + str(kirje_nr + 1) + " kustutatud nimekirjast " + nimekiri)
        self.tühjenda_põhikuva()
        self.lehe_loomine(nimekiri)

    def tagasi(self):
        self.destroy()
        valikud = Valikud(self.kasutaja)
        valikud.mainloop()
