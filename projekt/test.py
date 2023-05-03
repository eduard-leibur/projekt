import tkinter
from kategooria import Kategooria


def avamine(pealkiri, kasutaja, valikuriba_värv, fail, osastav_k, mitmuses):
    kategooria = Kategooria(pealkiri, kasutaja, valikuriba_värv, fail, osastav_k, mitmuses)
    kategooria.peameetod()


kuva = tkinter.Tk()
nupp = tkinter.Button(text="Raamatud", font=("calibri", 12),
                      command=lambda: avamine("Raamatud", "ed", "yellow", "raamatud.json", "raamatu", "raamatud"))
nupp.pack()

kuva.mainloop()
