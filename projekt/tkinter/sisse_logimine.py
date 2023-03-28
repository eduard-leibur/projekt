import tkinter

aken = tkinter.Tk()
aken.title("Sisse logimine")
aken.geometry("400x300")

kasutajanimi = tkinter.StringVar()
parool = tkinter.StringVar()

kasutajanime_silt = tkinter.Label(aken, text="Kasutajanimi:", font=("calibre", 12, "bold"))
parooli_silt = tkinter.Label(aken, text="Parool:", font=("calibre", 12, "bold"))
kasutajanime_kast = tkinter.Entry(aken, textvariable=kasutajanimi, font=("calibre", 12))
parooli_kast = tkinter.Entry(aken, textvariable=parool, font=("calibre", 12))

väljumisnupp = tkinter.Button(aken, text="Välju", command=lambda: quit(1))     # 1 - nupust väljumine
kinnitus = tkinter.Button(aken, text="Kinnita")

kasutajanime_silt.grid(row=0, column=0)
kasutajanime_kast.grid(row=0, column=1)
parooli_silt.grid(row=1, column=0)
parooli_kast.grid(row=1, column=1)
kinnitus.grid(row=2, column=1)
väljumisnupp.grid(row=3, column=1)

aken.mainloop()
