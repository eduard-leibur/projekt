import os
import tkinter
import json
from tkinter import messagebox
from funktsioonid.geomeetria import geomeetria_keskele


class KasutajaSisestamine:
    def __init__(self):
        self.aken = tkinter.Tk()
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
                    with open("andmed/kasutaja.txt", "w") as kasutaja_fail:    # sisselogitud kasutajanime salvestamine
                        kasutaja_fail.write(self.kasutajanimi)

                    print("Kasutaja", self.kasutajanimi, "sisse logitud.")  # info konsooli
                    sõnum = "Kasutaja " + self.kasutajanimi + " sisse logitud."
                    tkinter.messagebox.showinfo(title=None, message=sõnum)
                    self.aken.destroy()
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

                    for element in asukohad:
                        täielik_asukoht = asukoht + self.kasutajanimi + element
                        with open(täielik_asukoht, "w") as json_fail:
                            json.dump({"Soovikiri": [], "Vaadatud": [], "Nimekiri 1": [], "Nimekiri 2": []}, json_fail)

                    print("Kasutaja", self.kasutajanimi, "registreeritud.")  # info konsooli
                    sõnum = "Kasutaja " + self.kasutajanimi + " registreeritud."
                    tkinter.messagebox.showinfo(title=None, message=sõnum)
                    self.aken.destroy()
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

    def peameetod(self):
        self.aken.title("Sisse logimine")
        geomeetria_keskele(self.aken, 400, 300)

        kasutajanime_silt = tkinter.Label(self.aken, text="Kasutajanimi:", font=("calibre", 12, "bold"))
        parooli_silt = tkinter.Label(self.aken, text="Parool:", font=("calibre", 12, "bold"))

        kasutajanime_kast = tkinter.Entry(self.aken, font=("calibre", 12))
        parooli_kast = tkinter.Entry(self.aken, font=("calibre", 12))
        kasutajanime_kast.focus()

        väljumisnupp = tkinter.Button(self.aken, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
        kinnita_nupp = tkinter.Button(self.aken, text="Logi sisse",
                                      command=lambda: self.kinnita(kasutajanime_kast, parooli_kast))
        registreerimine = tkinter.Button(self.aken, text="Registreeri",
                                         command=lambda: self.registreeri(kasutajanime_kast, parooli_kast))

        kasutajanime_silt.grid(row=0, column=0)
        kasutajanime_kast.grid(row=0, column=1)
        parooli_silt.grid(row=1, column=0)
        parooli_kast.grid(row=1, column=1)

        kinnita_nupp.grid(row=2, column=1)
        registreerimine.grid(row=2, column=2)
        väljumisnupp.grid(row=3, column=1)

        self.aken.mainloop()
