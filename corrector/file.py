class File:

    def __init__(self):
        with open("slovnik.txt", "r", encoding="utf-8") as soubor:
            self._slovnik = []
            for radek in soubor.readlines():
                self._slovnik.append(radek.strip())

    def seradPodleVelikosti(self):
        nejvyssi = 0
        self.slovnik = []
        for radek in self._slovnik:
            if len(radek) > nejvyssi:
                for x in range(len(radek) - nejvyssi):
                    self.slovnik.append(list())
                nejvyssi = len(radek)
            self.slovnik[len(radek)-1].append(radek)

    def ziskejSlovnik(self):
        return self.slovnik
