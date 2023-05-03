import tkinter
import os
from funktsioonid.geomeetria import geomeetria_keskele
from kategooria import Kategooria


def kasutaja_sisestamine():
    os.system("python kasutaja_sisestamine.py")
    with open("andmed/kasutaja.txt", "r") as fail:
        sisestatud_kasutaja = fail.read()
    silt_kasutajaga = "Kasutaja: " + sisestatud_kasutaja
    kasutaja_silt.config(text=silt_kasutajaga)
    global kasutaja
    kasutaja = sisestatud_kasutaja


def avamine(pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses):
    kategooria = Kategooria(pealkiri, aktiivne_kasutaja, valikuriba_värv, fail, osastav_k, mitmuses)
    kategooria.peameetod()


def väljumine():
    with open("andmed/kasutaja.txt", "w") as fail:
        fail.write("")
    quit(1)     # 1 - väljumine meetodiga sulgemine


avakuva = tkinter.Tk()
avakuva.title("Avakuva")
geomeetria_keskele(avakuva, 500, 400)


kasutaja = ""
silt = "Kasutaja: " + kasutaja
kasutaja_silt = tkinter.Label(avakuva, text=silt)
kasutaja_silt.pack()

sisenemine = tkinter.Button(avakuva, text="Sisenemine", command=kasutaja_sisestamine)
sisenemine.pack(pady=20)

kategooriate_pady = 5
filmid = tkinter.Button(avakuva, text="Filmid",
                        command=lambda: avamine("Filmid", kasutaja, "lightblue", "filmid.json", "filmi", "filmid"))
filmid.pack(pady=kategooriate_pady)
raamatud = tkinter.Button(avakuva, text="Raamatud",
                          command=lambda: avamine("Raamatud", kasutaja, "yellow",
                                                  "raamatud.json", "raamatu", "raamatud"))
raamatud.pack(pady=kategooriate_pady)
mängud = tkinter.Button(avakuva, text="Mängud",
                        command=lambda: avamine("Mängud", kasutaja, "lightgreen", "mängud.json", "mängu", "mängud"))
mängud.pack(pady=kategooriate_pady)
riigid = tkinter.Button(avakuva, text="Riigid",
                        command=lambda: avamine("Riigid", kasutaja, "lightred", "riigid.json", "riigi", "riigid"))
riigid.pack(pady=kategooriate_pady)

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=väljumine)
väljumisnupp.pack(pady=20)


avakuva.mainloop()
