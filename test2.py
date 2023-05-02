def leht_soovikiri():
    soovikiri = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(soovikiri, text="Soovikiri", font=("Bold", 12), pady=20)
    pealkiri.pack()

    soovikiri.pack()
    soovikiri.pack_propagate(False)
    soovikiri.configure(width=1000, height=550)


def leht_vaadatud():
    vaadatud_leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(vaadatud_leht, text="Vaadatud", font=("Bold", 12), pady=20)
    pealkiri.pack()

    vaadatud_leht.pack()
    vaadatud_leht.pack_propagate(False)
    vaadatud_leht.configure(width=1000, height=550)


def leht_nimekiri1():
    vaadatud_leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(vaadatud_leht, text="Nimekiri 1", font=("Bold", 12), pady=20)
    pealkiri.pack()

    vaadatud_leht.pack()
    vaadatud_leht.pack_propagate(False)
    vaadatud_leht.configure(width=1000, height=550)


def leht_nimekiri2():
    vaadatud_leht = tkinter.Frame(põhikuva)

    pealkiri = tkinter.Label(vaadatud_leht, text="Nimekiri 2", font=("Bold", 12), pady=20)
    pealkiri.pack()

    vaadatud_leht.pack()
    vaadatud_leht.pack_propagate(False)
    vaadatud_leht.configure(width=1000, height=550)