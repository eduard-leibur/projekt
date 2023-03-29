import tkinter
import os


def kasutaja_sisestamine():
    os.chdir("C:\\Users\\eduard.leibur\\Downloads\\projekt\\projekt\\tkinter")
    os.system("python kasutaja_sisestamine.py")
    with open("kasutaja.txt", "r") as fail:
        sisestatud_kasutaja = fail.read()
    kasutaja_silt.config(text=sisestatud_kasutaja)


avakuva = tkinter.Tk()
avakuva.title("Avakuva")
laius = 500
kõrgus = 400
ekraani_laius = avakuva.winfo_screenwidth()
ekraani_kõrgus = avakuva.winfo_screenheight()
x = (ekraani_laius/2) - (laius/2)
y = (ekraani_kõrgus/2) - (kõrgus/2)
avakuva.geometry('%dx%d+%d+%d' % (laius, kõrgus, x, y))


with open("kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
kasutaja_silt = tkinter.Label(avakuva, text=kasutaja)
kasutaja_silt.pack()

testnupp = tkinter.Button(avakuva, text="Sisenemine", command=kasutaja_sisestamine)
testnupp.pack()

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=lambda: quit(1))
väljumisnupp.pack()

avakuva.mainloop()
