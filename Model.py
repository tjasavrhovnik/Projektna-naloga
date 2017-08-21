import tkinter as tk
import random


labirinti = [[0, 0, 0, 0, 0],
             [0, -1, -1, -1, 0],
             [0, 0, 0, -1, 0],
             [0, -1, -1, -1, 0],
             [0, 0, 0, 0, 0]]

class Labirint:
    
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
        self.matrika[self.polozaj_misi[0]][self.polozaj_misi[1]] = 1
        
        siri = []
        mozni_polozaji = []
        
        while len(siri) < stevilo_sirov:
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
            self.uporabnikov_vnos()
            uspesen_premik = self.premakni_mis()
            if uspesen_premik == True:
                self.tocke -= 1
            print(self.tocke)
            if self.konec_igre():
                print('konec igre')
                break

    def uporabnikov_vnos(self):
        vnos = input()
        if vnos == 'W':
            self.smer = (-1, 0)
        elif vnos == 'S':
            self.smer = (1, 0)
        elif vnos == 'A':
            self.smer = (0, -1)
        elif vnos == 'D':
            self.smer = (0, 1)
            
            
    def premakni_mis(self):
        y, x = self.labirint.polozaj_misi
        d_y, d_x = self.smer
        premik = False
        if self.labirint.matrika[y + d_y][x + d_x] != 0:
            if self.labirint.matrika[y + d_y][x + d_x] == 2:
                self.tocke += 5
                self.labirint.siri.pop(self.labirint.siri.index((y + d_y, x + d_x)))
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = -1
            premik = True
            self.labirint.polozaj_misi = (y + d_y, x + d_x)
            self.labirint.matrika[self.labirint.polozaj_misi[0]][self.labirint.polozaj_misi[1]] = 1
        self.izrisi_polja()
        
        return premik

    def konec_igre(self):
        if self.tocke <= 0:
            return True
        if len(self.labirint.siri) == 0:
            return True
        return False

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
        
