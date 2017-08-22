import random

labirinti = [[0, 0, 0, 0, 0],
             [0, -1, -1, -1, 0],
             [0, 0, 0, -1, 0],
             [0, -1, -1, -1, 0],
             [0, 0, 0, 0, 0]]
#0:zid, -1:prazno polje, 1:trenutni polozaj, 2:sir

class Labirint:

    #postavimo labirint, zacetni polozaj misi in sire
    
    def __init__(self, labirinti):
        self.nova_igra(0, 1)

    def nova_igra(self, n, stevilo_sirov):
        #n je stevilka labirinta(kasneje)
        self.matrika = labirinti
        #labirintov bo kasneje vec in bomo v []
        #povedali kateri labirint uporabimo;
        #labirinti zamenjamo z labirinti[i]
        self.visina = len(labirinti)
        self.sirina = len(labirinti[0])

        self.polozaj_misi = (self.visina - 2, 1)
        #zacetni polozaj misi: levo spodaj
        self.matrika[self.polozaj_misi[0]][self.polozaj_misi[1]] = 1
        
        siri = []
        mozni_polozaji = [] ##TODO nepotrebno
        
        while len(siri) < stevilo_sirov:
            #izbiramo nakljucna polja za sire, dokler polje ni veljavno (prazno)
            tr_y = random.randint(0, self.visina - 1)
            tr_x = random.randint(0, self.sirina - 1)
            while self.matrika[tr_y][tr_x] != -1:
                tr_y = random.randint(0, self.visina - 1)
                tr_x = random.randint(0, self.sirina - 1)
            self.matrika[tr_y][tr_x] = 2
            siri.append((tr_y, tr_x))
        self.siri = siri
        #self.narisi()

class Igra:

    def __init__(self):
        self.smer = None
        self.tocke = 10
        self.labirint = Labirint(labirinti)
        self.osnovna_zanka()
    
    def osnovna_zanka(self):
        while True:
            #uporabnik vnese zelen premik
            self.uporabnikov_vnos()
            uspesen_premik = self.premakni_mis()
            #ce je premik uspesen, se odsteje tocka, mis premakne
            if uspesen_premik == True:
                self.tocke -= 1
            print(self.tocke)
            #konec igre
            if self.konec_igre():
                print('konec igre')
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
        if self.labirint.matrika[y + d_y][x + d_x] != 0:
            if self.labirint.matrika[y + d_y][x + d_x] == 2:
                #poje sir
                self.tocke += 5
                self.labirint.siri.pop(self.labirint.siri.index((y + d_y, x + d_x)))
            #premik uspel: prejsen polozaj -> prazno polje, nastavimo nov polozaj misi
            ##TODO vrstni red
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = -1
            premik = True
            self.labirint.polozaj_misi = (y + d_y, x + d_x)
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = 1
        self.izrisi_polja() 
        return premik

    def konec_igre(self):
        #zmanjkalo potez
        if self.tocke <= 0:
            return True
        #pojedel vse sire
        if len(self.labirint.siri) == 0:
            return True
        return False
    ##TODO locimo da igralec zmaga ali izgubi

    def izrisi_polja(self):
        for vrstica in self.labirint.matrika:
            print(vrstica)
            
        """"
            if (x, y) in self.siri:
                #Ko pridemo na mesto s sirom, sir izbrisemo, mis ostane.
                self.siri -= (x, y)
                self.tocke += 10
                if self.siri == []:
                    print('Konec igre')
                    self.aktivno = False
            if self.tocke == 0:
                print('Izgubil si.')
                self.aktivno = False
                
"""

igra = Igra()
        
