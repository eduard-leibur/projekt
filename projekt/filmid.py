import tkinter
from funktsioonid.geomeetria import geomeetria_keskele

kuva = tkinter.Tk()
kuva.title("Filmid")
geomeetria_keskele(kuva, 1000, 700)

with open("andmed/kasutaja.txt", "r") as kasutaja_fail:
    kasutaja = kasutaja_fail.read()
print(kasutaja + "'i filmid.")

väljumisnupp = tkinter.Button(kuva, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
väljumisnupp.pack()

kuva.mainloop()
