class TuristiklassiReisija:
    def __init__(self, nimi):
        self.nimi = str(nimi)
        self.lennuinfo = ""

    def arvutaHind(self, alghind):
        return alghind

    def salvestaLennuinfo(self, lennuinfo):
        self.lennuinfo = lennuinfo

    def __str__(self):
        tekst = self.nimi + " - viimane lend: " + self.lennuinfo
        print(tekst)


class EsimeseKlassiReisija:
    def __init__(self, kliendinr):
        self.kliendinr = int(kliendinr)
        self.lennud = []

    def arvutaHind(self, alghind):
        return 1.5 * alghind

    def salvestaLennuinfo(self, lennuinfo):
        self.lennud.append(lennuinfo)

    def __str__(self):
        tekst = str(self.kliendinr) + " - lende: " + str(len(self.lennud))
        print(tekst)
