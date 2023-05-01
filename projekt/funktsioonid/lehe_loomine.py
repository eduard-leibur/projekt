import tkinter


def lehe_loomine(põhikuva, pealkiri):
    leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(leht, text=pealkiri, font=("Bold", 12), pady=20)
    pealkiri.pack()

    leht.pack()
    leht.pack_propagate(False)
    leht.configure(width=1000, height=550)
