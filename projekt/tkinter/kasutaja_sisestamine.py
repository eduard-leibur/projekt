import tkinter
import json
from tkinter import messagebox


def kinnita():  # "Kinnita" nuppu vajutades
    kasutajanimi = kasutajanimi_sisestus.get()
    parool = parool_sisestus.get()

    with open("kasutajate andmed.json", "r") as fail:
        andmed = json.load(fail)

    if kasutajanimi == "":
        print("Kasutajanimi puudu")
    if kasutajanimi in andmed:
        if andmed[kasutajanimi] == parool:
            print("Kasutaja sisse logitud.")
            tkinter.messagebox.showinfo(title=None, message="Korras")
        else:
            tkinter.messagebox.showerror(title=None, message="Vale parool!")
    else:
        tkinter.messagebox.showwarning(title=None, message="Sellist kasutajat pole!")


def registreeri():
    kasutajanimi = kasutajanimi_sisestus.get()
    parool = parool_sisestus.get()

    with open("kasutajate andmed.json", "r") as fail_sisse:
        andmed = json.load(fail_sisse)

    andmed[kasutajanimi] = parool

    with open("kasutajate andmed.json", "w") as fail_välja:
        json.dump(andmed, fail_välja)
    print("Kasutaja", kasutajanimi, "registreeritud.")
    sõnum = "Kasutaja " + kasutajanimi + " registreeritud."
    tkinter.messagebox.showinfo(title=None, message=sõnum)


aken = tkinter.Tk()
aken.title("Sisse logimine")
laius = 400
kõrgus = 300
ekraani_laius = aken.winfo_screenwidth()
ekraani_kõrgus = aken.winfo_screenheight()
x = (ekraani_laius/2) - (laius/2)
y = (ekraani_kõrgus/2) - (kõrgus/2)
aken.geometry("%dx%d+%d+%d" % (laius, kõrgus, x, y))

kasutajanimi_sisestus = tkinter.StringVar()
parool_sisestus = tkinter.StringVar()

kasutajanime_silt = tkinter.Label(aken, text="Kasutajanimi:", font=("calibre", 12, "bold"))
parooli_silt = tkinter.Label(aken, text="Parool:", font=("calibre", 12, "bold"))
kasutajanime_kast = tkinter.Entry(aken, textvariable=kasutajanimi_sisestus, font=("calibre", 12))
parooli_kast = tkinter.Entry(aken, textvariable=parool_sisestus, font=("calibre", 12))

väljumisnupp = tkinter.Button(aken, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
sisse_logimine = tkinter.Button(aken, text="Logi sisse", command=kinnita)
registreerimine = tkinter.Button(aken, text="Registreeri", command=registreeri)


kasutajanime_silt.grid(row=0, column=0)
kasutajanime_kast.grid(row=0, column=1)
parooli_silt.grid(row=1, column=0)
parooli_kast.grid(row=1, column=1)

sisse_logimine.grid(row=2, column=1)
registreerimine.grid(row=2, column=2)
väljumisnupp.grid(row=3, column=1)

aken.mainloop()
