import tkinter

avakuva = tkinter.Tk()
avakuva.title("Avakuva")
laius = 400
kõrgus = 300
ekraani_laius = avakuva.winfo_screenwidth()
ekraani_kõrgus = avakuva.winfo_screenheight()
x = (ekraani_laius/2) - (laius/2)
y = (ekraani_kõrgus/2) - (kõrgus/2)
avakuva.geometry('%dx%d+%d+%d' % (laius, kõrgus, x, y))

testnupp = tkinter.Button(avakuva, text="Test", command=lambda: print("Test!"))
testnupp.pack()

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=lambda: quit(1))
väljumisnupp.pack()

avakuva.mainloop()
