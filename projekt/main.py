import tkinter
import os


def kasutaja_sisestamine():
    os.system("python kasutaja_sisestamine.py")
    with open("kasutaja.txt", "r") as fail:
        sisestatud_kasutaja = fail.read()
    silt_kasutajaga = "Kasutaja: " + sisestatud_kasutaja
    kasutaja_silt.config(text=silt_kasutajaga)


def väljumine():
    with open("kasutaja.txt", "w") as fail:
        fail.write("")
    quit(1)     # 1 - väljumine meetodiga sulgemine


avakuva = tkinter.Tk()
avakuva.title("Avakuva")
laius = 500
kõrgus = 400
ekraani_laius = avakuva.winfo_screenwidth()
ekraani_kõrgus = avakuva.winfo_screenheight()
x = (ekraani_laius/2) - (laius/2)
y = (ekraani_kõrgus/2) - (kõrgus/2)
avakuva.geometry('%dx%d+%d+%d' % (laius, kõrgus, x, y))


kasutaja = ""
silt = "Kasutaja: " + kasutaja
kasutaja_silt = tkinter.Label(avakuva, text=silt)
kasutaja_silt.pack()

sisenemine = tkinter.Button(avakuva, text="Sisenemine", command=kasutaja_sisestamine)
sisenemine.pack(pady=20)

kategooriate_pady = 5
filmid = tkinter.Button(avakuva, text="Filmid", command=lambda: print("Tahab saada filme"))
filmid.pack(pady=kategooriate_pady)
raamatud = tkinter.Button(avakuva, text="Raamatud", command=lambda: print("Tahab saada raamatuid"))
raamatud.pack(pady=kategooriate_pady)
mängud = tkinter.Button(avakuva, text="Mängud", command=lambda: print("Tahab saada mänge"))
mängud.pack(pady=kategooriate_pady)
kohad = tkinter.Button(avakuva, text="Kohad", command=lambda: print("Tahab saada kohti"))
kohad.pack(pady=kategooriate_pady)

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=väljumine)
väljumisnupp.pack(pady=20)


avakuva.mainloop()
