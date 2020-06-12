class Corrector:
    def __init__(self, slovnik):
        self.slovnik = slovnik

    def ziskejOpravy(self, text_na_opravu):
        text_na_opravu = text_na_opravu.lower()
        self.opravy = list()

        if len(text_na_opravu) > 1:
            mozne_opravy = self.slovnik[len(text_na_opravu)-2:len(text_na_opravu)+1]
        else:
            mozne_opravy = self.slovnik[len(text_na_opravu) - 1:len(text_na_opravu) + 1]

        for slovo in mozne_opravy[0]:
            for y in range(len(text_na_opravu)):
                text_na_opravu_upraven = list(text_na_opravu)
                del text_na_opravu_upraven[y]
                if(self.zkontrolujSlovo(slovo, text_na_opravu_upraven, 2) == 0):
                    self.opravy.append(slovo)

        for slovo in mozne_opravy[1]:
            if(self.zkontrolujSlovo(slovo, text_na_opravu, 2) == 1):
                self.opravy.append(slovo)

        for slovo in mozne_opravy[2]:
            for y in range(len(slovo)):
                slovo_upravene = list(slovo)
                del slovo_upravene[y]
                if(self.zkontrolujSlovo(slovo_upravene, text_na_opravu, 2) == 0):
                    self.opravy.append(slovo)


        return self.opravy

    def zkontrolujSlovo(self, slovo, slovo_k_oprave, chyby):
        procet_nespravnych = 0

        for x in range(len(slovo)):
            if (not (slovo[x] == slovo_k_oprave[x])):
                if (procet_nespravnych < chyby):
                    procet_nespravnych += 1
                else:
                    break
        return procet_nespravnych


