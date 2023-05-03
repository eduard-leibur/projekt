import json
import tkinter
from tkinter import scrolledtext
from funktsioonid.geomeetria import geomeetria_keskele

class Kategooria:
    def __init__(self, pealkiri, kasutaja, valikuriba_värv, fail, osastav_k, mitmuses):
        self.pealkiri = pealkiri
        self.kasutaja = kasutaja
        self.fail = fail
        self.osastav_k = osastav_k
        self.mitmuses = mitmuses

        self.valikuriba_värv = valikuriba_värv
        self.põhikuva_värv = "lightgreen"

        self.kuva = tkinter.Tk()
        self.põhikuva = tkinter.Frame(self.kuva, bg=self.põhikuva_värv)
        self.valikuriba = tkinter.Frame(self.kuva, bg=valikuriba_värv)

        self.soovikiri_indikaator = tkinter.Label(self.valikuriba, bg=valikuriba_värv)
        self.vaadatud_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri1_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri2_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)

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
        lisatud_kirje = tkinter.StringVar()
        lisatud_kirje.set("Lisatava " + self.osastav_k + " pealkiri")
        lisamise_kast = tkinter.Entry(lisamise_raam, textvariable=lisatud_kirje, font=("calibre", 14))
        lisamise_nupp = tkinter.Button(lisamise_raam, text="Lisa",
                                       command=lambda: self.kirje_lisamine(lisatud_kirje.get(), nimekiri))

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
                                          command=lambda: self.kirje_kustutamine(kustutatud_kirje.get(), nimekiri))

        kustutamise_nupp.pack(side=tkinter.RIGHT, padx=10)
        kustutamise_kast.pack(side=tkinter.RIGHT)
        kustutamise_kast.pack_propagate(False)
        kustutamise_kast.configure(width=7)
        kustutamise_silt.pack(side=tkinter.RIGHT)

        nimekirja_kast = scrolledtext.ScrolledText(leht, font=("Bold", 16))

        if self.kasutaja == "":
            print("Pole kasutajat!")
            quit(2)     # 2 - pole kasutajat

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

    def peameetod(self):
        self.kuva.title(self.pealkiri)
        geomeetria_keskele(self.kuva, 1000, 700)

        with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
            kasutaja = kasutaja_fail.read()
        print(kasutaja + "'i " + self.mitmuses)

        self.valikuriba.pack_propagate(False)
        self.valikuriba.pack(side="top", fill="x")
        self.valikuriba.configure(width=1000, height=150)

        nuppude_vahe = 30

        soovikiri_nupp = tkinter.Button(self.valikuriba, text="Soovikiri",
                                        command=lambda: self.lehe_avamine(self.soovikiri_indikaator, "Soovikiri"))
        soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        vaadatud_nupp = tkinter.Button(self.valikuriba, text="Vaadatud",
                                       command=lambda: self.lehe_avamine(self.vaadatud_indikaator, "Vaadatud"))
        vaadatud_nupp.pack(side=tkinter.LEFT, padx=0)

        nimekiri1_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 1",
                                        command=lambda: self.lehe_avamine(self.nimekiri1_indikaator, "Nimekiri 1"))
        nimekiri1_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        nimekiri2_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 2",
                                        command=lambda: self.lehe_avamine(self.nimekiri2_indikaator, "Nimekiri 2"))
        nimekiri2_nupp.pack(side=tkinter.LEFT, padx=0)
        self.valikuriba.update()

        self.soovikiri_indikaator.place(x=nuppude_vahe, y=45, width=soovikiri_nupp.winfo_width(), height=6)

        self.vaadatud_indikaator.place(x=2*nuppude_vahe+soovikiri_nupp.winfo_width(), y=45,
                                       width=vaadatud_nupp.winfo_width(), height=6)

        self.nimekiri1_indikaator.place(x=3*nuppude_vahe+soovikiri_nupp.winfo_width()+vaadatud_nupp.winfo_width(), y=45,
                                        width=nimekiri1_nupp.winfo_width(), height=6)

        self.nimekiri2_indikaator.place(x=4 * nuppude_vahe + soovikiri_nupp.winfo_width() +
                                        vaadatud_nupp.winfo_width() + nimekiri1_nupp.winfo_width(),
                                        y=45, width=nimekiri2_nupp.winfo_width(), height=6)

        väljumisnupp = tkinter.Button(self.valikuriba, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
        väljumisnupp.pack(side=tkinter.RIGHT, padx=nuppude_vahe)

        kasutaja_sildi_tekst = "Kasutaja: " + kasutaja
        kasutaja_silt = tkinter.Label(self.valikuriba, text=kasutaja_sildi_tekst, font=("Bold", 12))
        kasutaja_silt.pack(side=tkinter.RIGHT)

        self.põhikuva.pack(side="top", fill="both")
        self.põhikuva.pack_propagate(False)
        self.põhikuva.configure(width=1000, height=550)

        põhikuva_silt = tkinter.Label(self.põhikuva, text="Palun valige ülevalt nimekiri.",
                                      font=("Bold", 12), bg=self.põhikuva_värv)
        põhikuva_silt.pack(fill="none", expand=True)

        self.kuva.mainloop()
