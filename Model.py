import random

from labirinti import labirinti

class Labirint:

    #postavimo labirint, zacetni polozaj misi in sire
    
    def __init__(self, labirinti):
        n = random.randint(0, len(labirinti) - 1)
        self.matrika = []
        self.siri = []
        self.nova_igra(n, 3)

    def nova_igra(self, n, stevilo_sirov):
        #n je stevilka labirinta(kasneje)
        self.matrika = labirinti[n]
        #labirintov bo kasneje vec in bomo v []
        #povedali kateri labirint uporabimo;
        #labirinti zamenjamo z labirinti[i]
        self.visina = len(self.matrika)
        self.sirina = len(self.matrika[0])

        self.polozaj_misi = (self.visina - 2, 1)
        #zacetni polozaj misi: levo spodaj
        self.matrika[self.polozaj_misi[0]][self.polozaj_misi[1]] = 1
        
        siri = []
        
        while len(siri) < stevilo_sirov:
            #print(siri)
            #izbiramo nakljucna polja za sire, dokler polje ni veljavno (prazno)
            tr_y = random.randint(0, self.visina - 1)
            tr_x = random.randint(0, self.sirina - 1)
            while self.matrika[tr_y][tr_x] != -1:
                tr_y = random.randint(0, self.visina - 1)
                tr_x = random.randint(0, self.sirina - 1)
                #print(tr_y, tr_x)
            self.matrika[tr_y][tr_x] = 2
            siri.append((tr_y, tr_x))
        self.siri = siri
        #self.narisi()

class Igra:

    def __init__(self):
        self.smer = (0, 0)
        self.tocke = 8
        self.labirint = Labirint(labirinti)
        #self.osnovna_zanka()
    
    def osnovna_zanka(self):
        while True:
            #uporabnik vnese zelen premik
            self.uporabnikov_vnos()
            uspesen_premik = self.premakni_mis()
            #ce je premik uspesen, se odsteje tocka, mis premakne
            if uspesen_premik == True:
                self.tocke -= 1
            #print(self.tocke)
            #konec igre
            koncaj = self.konec_igre()
            if koncaj != 0:
                if koncaj == 1:
                    print('Zmagal si!')
                elif koncaj == -1:
                    print('Izgubil si!')
                break

    def uporabnikov_vnos(self):
        vnos = input()
        if vnos == 'W':
            self.smer = (-1, 0) #gor
        elif vnos == 'S':
            self.smer = (1, 0) #dol
        elif vnos == 'A':
            self.smer = (0, -1) #levo
        elif vnos == 'D':
            self.smer = (0, 1) #desno
            
    def premakni_mis(self):
        y, x = self.labirint.polozaj_misi
        d_y, d_x = self.smer
        premik = False #zastavica
        #premik je mozen, ce novo polje ni zid
        if self.smer != (0, 0) and self.labirint.matrika[y + d_y][x + d_x] != 0:
            if self.labirint.matrika[y + d_y][x + d_x] == 2:
                #poje sir
                self.tocke += 5
                self.labirint.siri.pop(self.labirint.siri.index((y + d_y, x + d_x)))
            #premik uspel: prejsen polozaj -> prazno polje, nastavimo nov polozaj misi
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = -1
            premik = True
            self.labirint.polozaj_misi = (y + d_y, x + d_x)
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = 1
        #self.izrisi_polja()
        self.smer = (0, 0)
        return premik

    def konec_igre(self):
        #zmanjkalo potez
        if self.tocke <= 0:
            return -1
        #pojedel vse sire
        if len(self.labirint.siri) == 0:
            return 1
        return 0
    ##TODO locimo da igralec zmaga ali izgubi

    def izrisi_polja(self):
        for vrstica in self.labirint.matrika:
            print(vrstica)

if __name__ == '__main__':
    pass
    #igra = Igra()
        
