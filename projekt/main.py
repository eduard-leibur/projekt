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

testnupp = tkinter.Button(avakuva, text="Sisenemine", command=kasutaja_sisestamine)
testnupp.pack()

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=väljumine)
väljumisnupp.pack()

avakuva.mainloop()
