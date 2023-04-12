def geomeetria_keskele(aken, laius, kõrgus):
    ekraani_laius = aken.winfo_screenwidth()
    ekraani_kõrgus = aken.winfo_screenheight()
    x = (ekraani_laius / 2) - (laius / 2)
    y = (ekraani_kõrgus / 2) - (kõrgus / 2)
    aken.geometry('%dx%d+%d+%d' % (laius, kõrgus, x, y))
