import os
import tkinter
import json
from tkinter import messagebox
from funktsioonid.geomeetria import geomeetria_keskele


def kinnita(juhtum):  # "Kinnita" nuppu vajutades
    kasutajanimi = kasutajanimi_sisestus.get()
    parool = parool_sisestus.get()

    with open("andmed/kasutajate andmed.json", "r") as fail:
        andmed = json.load(fail)

    if kasutajanimi == "":
        print("Kasutajanimi puudu")             # info konsooli
        tkinter.messagebox.showwarning(title=None, message="Sisestage kasutajanimi")
    elif parool == "":
        print("Parool puudu")                   # info konsooli
        tkinter.messagebox.showwarning(title=None, message="Sisestage parool")
    else:
        if kasutajanimi in andmed:
            if andmed[kasutajanimi] == parool:
                with open("andmed/kasutaja.txt", "w") as kasutaja_fail:    # sisselogitud kasutajanime salvestamine
                    kasutaja_fail.write(kasutajanimi)

                print("Kasutaja", kasutajanimi, "sisse logitud.")  # info konsooli
                sõnum = "Kasutaja " + kasutajanimi + " sisse logitud."
                tkinter.messagebox.showinfo(title=None, message=sõnum)
                quit(2)     # 2- kasutaja sisse logitud
            else:
                tkinter.messagebox.showerror(title=None, message="Vale parool!")
        else:
            tkinter.messagebox.showwarning(title=None, message="Sellist kasutajat pole!")


def registreeri():  # "Registreeri" nuppu vajutades
    kasutajanimi = kasutajanimi_sisestus.get()
    parool = parool_sisestus.get()

    if kasutajanimi.isascii():
        if kasutajanimi.islower():
            if len(parool) >= 3:
                with open("andmed/kasutajate andmed.json", "r") as fail_sisse:
                    andmed = json.load(fail_sisse)  # olemasolevate kasutajate lugemine
                andmed[kasutajanimi] = parool  # uue kasutaja lisamine
                with open("andmed/kasutajate andmed.json", "w") as fail_välja:
                    json.dump(andmed, fail_välja)  # sõnastiku koos uue kasutajaga salvestamine

                käsklus = "mkdir .\\andmed\\kasutajad\\" + kasutajanimi
                os.system(käsklus)      # loob kasutaja nimelise kausta kasutaja andmete jaoks
                print(kasutajanimi, "kaust loodud.")

                print("Kasutaja", kasutajanimi, "registreeritud.")  # info konsooli
                sõnum = "Kasutaja " + kasutajanimi + " registreeritud."
                tkinter.messagebox.showinfo(title=None, message=sõnum)
            else:
                tkinter.messagebox.showerror(title="Viga paroolis",
                                             message="Parool peab koosnema vähemalt kolmest tähemärgist või numbrist!")
        else:
            tkinter.messagebox.showerror(title="Viga kasutajanimes",
                                         message="Kasutajanimi peab olema ainult väiketähtedes!")
    else:
        tkinter.messagebox.showerror(title="Viga kasutajanimes",
                                     message="Kasutajanimi ei tohi sisaldada täpitähti!")


aken = tkinter.Tk()
aken.title("Sisse logimine")
geomeetria_keskele(aken, 400, 300)


kasutajanimi_sisestus = tkinter.StringVar()
parool_sisestus = tkinter.StringVar()

kasutajanime_silt = tkinter.Label(aken, text="Kasutajanimi:", font=("calibre", 12, "bold"))
parooli_silt = tkinter.Label(aken, text="Parool:", font=("calibre", 12, "bold"))
kasutajanime_kast = tkinter.Entry(aken, textvariable=kasutajanimi_sisestus, font=("calibre", 12))
parooli_kast = tkinter.Entry(aken, textvariable=parool_sisestus, font=("calibre", 12))
parooli_kast.bind("<Return>", kinnita)

väljumisnupp = tkinter.Button(aken, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
sisse_logimine = tkinter.Button(aken, text="Logi sisse", command=lambda: kinnita("nupp"))
registreerimine = tkinter.Button(aken, text="Registreeri", command=registreeri)


kasutajanime_silt.grid(row=0, column=0)
kasutajanime_kast.grid(row=0, column=1)
parooli_silt.grid(row=1, column=0)
parooli_kast.grid(row=1, column=1)

sisse_logimine.grid(row=2, column=1)
registreerimine.grid(row=2, column=2)
väljumisnupp.grid(row=3, column=1)

aken.mainloop()
