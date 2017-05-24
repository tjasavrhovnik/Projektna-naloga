import tkinter as tk
import random

okno = tk.Tk()
gumb = tk.Button(okno, text= 'START')
gumb.pack()

labirinti = [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

class Labirint:
    def __init__(self, d):
        self.slika = tk.Canvas(okno, width = d * self.visina + 1,
                                height = d * self.visina + 1)
        self.slika.place(x = 0, y = 0)

    def nova_igra(self, n, stevilo_sirov):
        #n je stevilka labirinta(kasneje)
        self.matrika = labirinti
        #labirintov bo kasneje vec in bomo v []
        #povedali kateri labirint uporabimo;
        #labirinti zamenjamo z labirinti[i]
        self.visina = len(labirinti)
        self.sirina = len(labirinti[0])

        self.polozaj_misi = (1, self.visina - 2)
        
        siri = []
        mozni_polozaji = []
        for i in range(self.visina // 2):
            for j in range(self.visina // 2):
                if (2 * i - 1, 2 * j - 1)!= self.polozaj_misi:
                    mozni_polozaji += [(2 * i - 1, 2 * j - 1)]
        while len(siri) < stevilo_sirov:
            siri += [random.choice[mozni_polozaji]]
        self.siri = siri
        self.tocke = 10
        self.aktivno = True
        self.narisi()

        
    def premakni_mis(smer):
        (x, y) = self.polozaj_misi
        if self.aktivno == True:
            if smer == 'GOR':
                if self.matrika[x][y - 1] == 0:
                    (x, y) = (x, y - 2)
                    self.tocke -= 1
            elif smer == 'DOL':
                if self.matrika[x][y + 1] == 0:
                    (x, y) = (x, y + 2)
                    self.tocke -=1
            elif smer == 'DESNO':
                if self.matrika[x + 1][y] == 0:
                    (x, y) = (x + 2, y)
                    self.tocke -= 1
            elif smer == 'LEVO':
                if self.matrika[x - 1][y] == 0:
                    (x, y) = (x - 2, y)
                    self.tocke -= 1
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


    #def narisi(self)
      
        
