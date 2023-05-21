import tkinter
from tkinter import messagebox
from projekt.funktsioonid.geomeetria import geomeetria_keskele
from projekt.kategooria import Kategooria
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
                                                                                       "filmi", "filmid"))
        self.filmid.pack(pady=kategooriate_pady)

        self.raamatud = tkinter.Button(self, text="Raamatud", command=lambda: self.avamine("Raamatud", self.kasutaja,
                                                                                           värv_raamatud,
                                                                                           "raamatud.json",
                                                                                           "raamatu", "raamatud"))
        self.raamatud.pack(pady=kategooriate_pady)

        self.mängud = tkinter.Button(self, text="Mängud", command=lambda: self.avamine("Mängud", self.kasutaja,
                                                                                       värv_mängud, "mängud.json",
                                                                                       "mängu", "mängud"))
        self.mängud.pack(pady=kategooriate_pady)

        self.riigid = tkinter.Button(self, text="Riigid", command=lambda: self.avamine("Riigid", self.kasutaja,
                                                                                       värv_riigid, "riigid.json",
                                                                                       "riigi", "riigid"))
        self.riigid.pack(pady=kategooriate_pady)

        self.väljumisnupp = tkinter.Button(self, text="Välju", command=lambda: quit(2))
        self.väljumisnupp.pack(pady=20)

    @staticmethod
    def avamine(pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses):
        if aktiivne_kasutaja == "":
            print("Pole kasutajat!")
            tkinter.messagebox.showwarning(title="Puudub kastuaja", message="Palun logige esmalt sisse kasutajana.")
        else:
            kategooria = Kategooria(pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses)
            kategooria.mainloop()
