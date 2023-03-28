import tkinter

avakuva = tkinter.Tk()
avakuva.title("Avakuva")
avakuva.geometry("400x300")

testnupp = tkinter.Button(avakuva, text="Test", command=lambda: print("Test!"))
testnupp.pack()

väljumisnupp = tkinter.Button(avakuva, text="Välju", command=lambda: quit(1))
väljumisnupp.pack()

avakuva.mainloop()
