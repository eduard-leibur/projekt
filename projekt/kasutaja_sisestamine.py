import os
import tkinter
import json
from tkinter import messagebox
from projekt.funktsioonid.geomeetria import geomeetria_keskele
from valikud_kategooria import Valikud
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
                    sõnum = "Kasutaja " + self.kasutajanimi + " sisse logitud."
                    tkinter.messagebox.showinfo(title=None, message=sõnum)

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
