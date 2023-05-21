import os
import tkinter
import json
from tkinter import messagebox
from projekt.funktsioonid.geomeetria import geomeetria_keskele
from valikud_kategooria import Valikud


class KasutajaSisestamine(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sisse logimine")
        geomeetria_keskele(self, 400, 300)

        self.kasutajanime_silt = tkinter.Label(self, text="Kasutajanimi:", font=("calibre", 12, "bold"))
        self.parooli_silt = tkinter.Label(self, text="Parool:", font=("calibre", 12, "bold"))

        self.kasutajanime_kast = tkinter.Entry(self, font=("calibre", 12))
        self.parooli_kast = tkinter.Entry(self, font=("calibre", 12))
        self.kasutajanime_kast.focus()

        self.väljumisnupp = tkinter.Button(self, text="Välju", command=lambda: quit(1))  # 1 - nupust väljumine
        self.kinnita_nupp = tkinter.Button(self, text="Logi sisse",
                                           command=lambda: self.kinnita(self.kasutajanime_kast, self.parooli_kast))
        self.registreerimine_nupp = tkinter.Button(self, text="Registreeri",
                                                   command=lambda: self.registreeri(self.kasutajanime_kast,
                                                                                    self.parooli_kast))

        self.kasutajanime_silt.grid(row=0, column=0)
        self.kasutajanime_kast.grid(row=0, column=1)
        self.parooli_silt.grid(row=1, column=0)
        self.parooli_kast.grid(row=1, column=1)

        self.kinnita_nupp.grid(row=2, column=1)
        self.registreerimine_nupp.grid(row=2, column=2)
        self.väljumisnupp.grid(row=3, column=1)

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
