import tkinter


def kinnita():
    print("Kinnita")


aken = tkinter.Tk()
aken.title("Registreerimine")
laius = 300
kõrgus = 300
x = (aken.winfo_screenwidth() / 2) - (laius / 2)
y = (aken.winfo_screenheight() / 2) - (kõrgus / 2)
aken.geometry("%dx%d+%d+%d" % (laius, kõrgus, x, y))

kasutajanimi_sisestus = tkinter.StringVar()
parool_sisestus = tkinter.StringVar()

kasutajanime_silt = tkinter.Label(aken, text="Kasutajanimi:", font=("calibre", 12, "bold"))
parooli_silt = tkinter.Label(aken, text="Parool:", font=("calibre", 12, "bold"))
kasutajanime_kast = tkinter.Entry(aken, textvariable=kasutajanimi_sisestus, font=("calibre", 12))
parooli_kast = tkinter.Entry(aken, textvariable=parool_sisestus, font=("calibre", 12))

väljumisnupp = tkinter.Button(aken, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
kinnitus = tkinter.Button(aken, text="Kinnita", command=kinnita)

kasutajanime_silt.grid(row=0, column=0)
kasutajanime_kast.grid(row=0, column=1)
parooli_silt.grid(row=1, column=0)
parooli_kast.grid(row=1, column=1)

kinnitus.grid(row=2, column=1, pady=5)
väljumisnupp.grid(row=3, column=1, pady=5)

aken.mainloop()
