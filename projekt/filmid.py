import tkinter
from funktsioonid.geomeetria import geomeetria_keskele

kuva = tkinter.Tk()
kuva.title("Filmid")
geomeetria_keskele(kuva, 1000, 700)

with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
print(kasutaja + "'i filmid.")


valikuriba = tkinter.Frame(kuva, width=1000, height=150, bg="lightblue")
valikuriba.pack(side="top", fill="x")

põhikuva = tkinter.Frame(kuva, width=1000, height=550, bg="lightgreen")
põhikuva.pack(side="top", fill="both")

"""
väljumisnupp = tkinter.Button(põhikuva, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack()"""

kuva.mainloop()
