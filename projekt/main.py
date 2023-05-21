import tkinter
from tkinter import messagebox, scrolledtext
import json
import os
from funktsioonid.geomeetria import geomeetria_keskele
from funktsioonid.värvid import *


class KasutajaSisestamine(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sisse logimine")
        self.configure(bg=värv_põhikuva)
        geomeetria_keskele(self, 400, 300)

        kastike = tkinter.Frame(width=300, height=210, bg=värv_põhikuva)
        kastike.place(x=50, y=50)

        self.kasutajanime_silt = tkinter.Label(kastike, text="Kasutajanimi:", bg=värv_põhikuva,
                                               font=("calibre", 12, "bold"))
        self.parooli_silt = tkinter.Label(kastike, text="Parool:", bg=värv_põhikuva,
                                          font=("calibre", 12, "bold"))

        self.kasutajanime_kast = tkinter.Entry(kastike, font=("calibre", 12))
        self.parooli_kast = tkinter.Entry(kastike, font=("calibre", 12))
        self.kasutajanime_kast.focus()

        self.väljumisnupp = tkinter.Button(kastike, text="Välju", bg=värv_väljumise_nupp, fg="white",
                                           command=lambda: quit(1))  # 1 - nupust väljumine
        self.kinnita_nupp = tkinter.Button(kastike, text="Logi sisse", bg=värv_logimisnupp,
                                           command=lambda: self.kinnita(self.kasutajanime_kast, self.parooli_kast))
        self.registreerimine_nupp = tkinter.Button(kastike, text="Registreeri", bg=värv_regamise_nupp,
                                                   command=lambda: self.registreeri(self.kasutajanime_kast,
                                                                                    self.parooli_kast))
        self.parooli_kast.bind("<Return>", lambda event: self.kinnita(self.kasutajanime_kast, self.parooli_kast))

        self.kasutajanime_silt.grid(row=0, column=0, pady=10)
        self.kasutajanime_kast.grid(row=0, column=1, pady=10)
        self.parooli_silt.grid(row=1, column=0, pady=10)
        self.parooli_kast.grid(row=1, column=1, pady=10)

        self.kinnita_nupp.grid(row=2, column=1, pady=10)
        self.registreerimine_nupp.grid(row=2, column=0, pady=10)
        self.väljumisnupp.grid(row=3, column=1, pady=40)
        kastike.grid_propagate(False)

        self.kasutajanimi = ""
        self.parool = ""

    def kinnita(self, kasutajanime_kast, parooli_kast):
        self.salvestamine(kasutajanime_kast, parooli_kast)
        with open("andmed/kasutajate andmed.json", "r") as fail:
            andmed = json.load(fail)

        if self.kasutajanimi == "":
            print("Kasutajanimi puudu")             # info konsooli
            tkinter.messagebox.showwarning(title=None, message="Sisestage kasutajanimi")
        elif self.parool == "":
            print("Parool puudu")                   # info konsooli
            tkinter.messagebox.showwarning(title=None, message="Sisestage parool")
        else:
            if self.kasutajanimi in andmed:
                if andmed[self.kasutajanimi] == self.parool:
                    print("Kasutaja", self.kasutajanimi, "sisse logitud.")  # info konsooli

                    self.destroy()
                    valikud = Valikud(self.kasutajanimi)
                    valikud.mainloop()
                else:
                    tkinter.messagebox.showerror(title=None, message="Vale parool!")
            else:
                tkinter.messagebox.showwarning(title=None, message="Sellist kasutajat pole!")

    def registreeri(self, kasutajanime_kast, parooli_kast):
        self.salvestamine(kasutajanime_kast, parooli_kast)
        if self.kasutajanimi.isascii():
            if self.kasutajanimi.islower():
                if len(self.parool) >= 3:
                    with open("andmed/kasutajate andmed.json", "r") as fail_sisse:
                        andmed = json.load(fail_sisse)  # olemasolevate kasutajate lugemine
                    andmed[self.kasutajanimi] = self.parool  # uue kasutaja lisamine
                    with open("andmed/kasutajate andmed.json", "w") as fail_välja:
                        json.dump(andmed, fail_välja)  # sõnastiku koos uue kasutajaga salvestamine

                    käsklus = "mkdir .\\andmed\\kasutajad\\" + self.kasutajanimi
                    os.system(käsklus)      # loob kasutaja nimelise kausta kasutaja andmete jaoks
                    print(self.kasutajanimi, "kaust loodud.")

                    asukoht = "andmed/kasutajad/"
                    asukohad = ["/filmid.json", "/raamatud.json", "/mängud.json", "/riigid.json"]
                    teise_nimekirja_pealkiri = ["Vaadatud", "Loetud", "Mängitud", "Käidud"]

                    i = 0
                    for element in asukohad:
                        täielik_asukoht = asukoht + self.kasutajanimi + element
                        with open(täielik_asukoht, "w") as json_fail:
                            json.dump({"Soovikiri": [], teise_nimekirja_pealkiri[i]: [], "Nimekiri 1": [],
                                       "Nimekiri 2": []}, json_fail)
                        i += 1

                    print("Kasutaja", self.kasutajanimi, "registreeritud.")  # info konsooli
                    sõnum = "Kasutaja " + self.kasutajanimi + " registreeritud."
                    tkinter.messagebox.showinfo(title=None, message=sõnum)
                else:
                    tkinter.messagebox.showerror(title="Viga paroolis",
                                                 message="Parool peab koosnema vähemalt "
                                                         "kolmest tähemärgist või numbrist!")
            else:
                tkinter.messagebox.showerror(title="Viga kasutajanimes",
                                             message="Kasutajanimi peab olema ainult väiketähtedes!")
        else:
            tkinter.messagebox.showerror(title="Viga kasutajanimes",
                                         message="Kasutajanimi ei tohi sisaldada täpitähti!")

    def salvestamine(self, kasutajanime_kast, parooli_kast):
        self.kasutajanimi = kasutajanime_kast.get()
        self.parool = parooli_kast.get()

    def kasutaja_sildi_tekst(self):
        tekst = "Kastutaja: " + self.kasutajanimi
        return tekst


class Valikud(tkinter.Tk):
    def __init__(self, kasutaja):
        super().__init__()
        self.kasutaja = kasutaja
        self.title("Avakuva")
        geomeetria_keskele(self, 500, 400)
        self.configure(bg=värv_põhikuva)

        self.silt = "Kasutaja: " + self.kasutaja
        self.kasutaja_silt = tkinter.Label(self, text=self.silt, pady=40, font=("calibre", 13), bg=värv_põhikuva)
        self.kasutaja_silt.pack()

        kategooriate_pady = 5

        self.filmid = tkinter.Button(self, text="Filmid", bg=värv_filmid, fg="white",
                                     command=lambda: self.avamine("Filmid", self.kasutaja, värv_filmid, "filmid.json",
                                                                  "filmi", "filmid", "Vaadatud"))
        self.filmid.pack(pady=kategooriate_pady)

        self.raamatud = tkinter.Button(self, text="Raamatud", bg=värv_raamatud,
                                       command=lambda: self.avamine("Raamatud", self.kasutaja, värv_raamatud,
                                                                    "raamatud.json", "raamatu", "raamatud", "Loetud"))
        self.raamatud.pack(pady=kategooriate_pady)

        self.mängud = tkinter.Button(self, text="Mängud", bg=värv_mängud,
                                     command=lambda: self.avamine("Mängud", self.kasutaja, värv_mängud, "mängud.json",
                                                                  "mängu", "mängud", "Mängitud"))
        self.mängud.pack(pady=kategooriate_pady)

        self.riigid = tkinter.Button(self, text="Riigid", bg=värv_riigid,
                                     command=lambda: self.avamine("Riigid", self.kasutaja, värv_riigid, "riigid.json",
                                                                  "riigi", "riigid", "Käidud"))
        self.riigid.pack(pady=kategooriate_pady)

        self.väljumisnupp = tkinter.Button(self, text="Välju", bg=värv_väljumise_nupp, fg="white",
                                           command=lambda: quit(2))
        self.väljumisnupp.pack(pady=40)

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
        geomeetria_keskele(self, 900, 600)

        self.pealkiri = pealkiri
        self.kasutaja = kasutaja
        self.fail = fail
        self.osastav_k = osastav_k
        self.mitmuses = mitmuses
        self.teine_pealkiri = teine_pealkiri

        self.valikuriba_värv = valikuriba_värv
        self.värv_lisamise_raam = värv_lisamise_raam

        self.põhikuva = tkinter.Frame(self, bg=värv_põhikuva)
        self.valikuriba = tkinter.Frame(self, bg=self.valikuriba_värv)

        self.soovikiri_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.vaadatud_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri1_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)
        self.nimekiri2_indikaator = tkinter.Label(self.valikuriba, bg=self.valikuriba_värv)

        print(kasutaja + "'i " + self.mitmuses)

        self.valikuriba.pack_propagate(False)
        self.valikuriba.pack(side="top", fill="x")
        self.valikuriba.configure(width=1000, height=150)

        nuppude_vahe = 30

        self.soovikiri_nupp = tkinter.Button(self.valikuriba, text="Soovikiri", bg=värv_nimekirjade_nupud,
                                             command=lambda: self.lehe_avamine(self.soovikiri_indikaator, "Soovikiri"))
        self.soovikiri_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        self.vaadatud_nupp = tkinter.Button(self.valikuriba, text=self.teine_pealkiri, bg=värv_nimekirjade_nupud,
                                            command=lambda: self.lehe_avamine(self.vaadatud_indikaator,
                                                                              self.teine_pealkiri))
        self.vaadatud_nupp.pack(side=tkinter.LEFT, padx=0)

        self.nimekiri1_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 1", bg=värv_nimekirjade_nupud,
                                             command=lambda: self.lehe_avamine(self.nimekiri1_indikaator, "Nimekiri 1"))
        self.nimekiri1_nupp.pack(side=tkinter.LEFT, padx=nuppude_vahe)

        self.nimekiri2_nupp = tkinter.Button(self.valikuriba, text="Nimekiri 2", bg=värv_nimekirjade_nupud,
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

        self.väljumisnupp = tkinter.Button(self.valikuriba, text="Välju", bg=värv_väljumise_nupp, fg="white",
                                           command=lambda: quit(1))  # 1 nupust väljumine
        self.väljumisnupp.pack(side=tkinter.RIGHT, padx=nuppude_vahe)

        self.tagasinupp = tkinter.Button(self.valikuriba, text="Tagasi", bg=värv_tagasi_nupp,
                                         command=self.tagasi)
        self.tagasinupp.pack(side=tkinter.RIGHT)

        kasutaja_sildi_tekst = "Kasutaja: " + kasutaja
        self.kasutaja_silt = tkinter.Label(self.valikuriba, text=kasutaja_sildi_tekst, font=("Bold", 12),
                                           bg=valikuriba_värv)
        self.kasutaja_silt.pack(side=tkinter.RIGHT, padx=nuppude_vahe)

        self.põhikuva.pack(side="top", fill="both")
        self.põhikuva.pack_propagate(False)
        self.põhikuva.configure(width=1000, height=550)

        self.põhikuva_silt = tkinter.Label(self.põhikuva, text="Palun valige ülevalt nimekiri.",
                                           font=("Bold", 12), bg=värv_põhikuva)
        self.põhikuva_silt.pack(fill="none", expand=True)

    def lehe_avamine(self, indikaator, nimekiri):
        self.peida_indikaatorid()
        indikaator.configure(bg="blue")
        self.tühjenda_põhikuva()
        self.lehe_loomine(nimekiri)

    def lehe_loomine(self, nimekiri):
        leht = tkinter.Frame(self.põhikuva, bg="blue")

        lisamise_raam = tkinter.Frame(leht, bg=self.värv_lisamise_raam)

        lisamise_silt = tkinter.Label(lisamise_raam, text="Uue kirje sisestamine:",
                                      font=("calibre", 14), bg=self.värv_lisamise_raam)

        lisamise_kast = tkinter.Entry(lisamise_raam, font=("calibre", 14))
        lisamise_kast.focus()
        lisamise_nupp = tkinter.Button(lisamise_raam, text="Lisa",
                                       command=lambda: self.kirje_lisamine(lisamise_kast.get(), nimekiri))
        lisamise_kast.bind("<Return>", lambda event: self.kirje_lisamine(lisamise_kast.get(), nimekiri))

        lisamise_raam.pack(side=tkinter.BOTTOM, fill="x")

        lisamise_silt.pack(side=tkinter.LEFT)
        lisamise_kast.pack(side=tkinter.LEFT, pady=5)
        lisamise_kast.pack_propagate(False)
        lisamise_kast.configure(width=30)
        lisamise_nupp.pack(side=tkinter.LEFT, padx=10)

        kustutamise_silt = tkinter.Label(lisamise_raam, text="Kustutatava kirje nr:",
                                         font=("calibre", 14), bg=self.värv_lisamise_raam)
        kustutamise_kast = tkinter.Entry(lisamise_raam, font=("calibre", 14))
        kustutamise_nupp = tkinter.Button(lisamise_raam, text="Kustuta",
                                          command=lambda: self.kirje_kustutamine(kustutamise_kast.get(), nimekiri))
        kustutamise_kast.bind("<Return>", lambda event: self.kirje_kustutamine(kustutamise_kast.get(), nimekiri))

        kustutamise_nupp.pack(side=tkinter.RIGHT, padx=10)
        kustutamise_kast.pack(side=tkinter.RIGHT)
        kustutamise_kast.pack_propagate(False)
        kustutamise_kast.configure(width=7)
        kustutamise_silt.pack(side=tkinter.RIGHT)

        nimekirja_kast = scrolledtext.ScrolledText(leht, font=("Bold", 16), bg=värv_nimekiri)

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


if __name__ == "__main__":
    logimine = KasutajaSisestamine()
    logimine.mainloop()
