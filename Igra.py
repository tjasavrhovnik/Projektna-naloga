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
    def __init__(self, n, stevilo_sirov, d):
        #n je stevilka labirinta(kasneje)
        self.matrika = labirinti
        #labirintov bo kasneje vec in bomo v []
        #povedali kateri labirint uporabimo;
        #labirinti zamenjamo z labirinti[i]
        self.visina = len(labirinti) // 2
        self.sirina = len(labirinti) // 2

        polozaj_misi = (self.visina, 1)
        
        self.sir = sir
        siri = []
        mozni_polozaji = []
        for i in range(self.visina):
            for j in range(self.visina):
                if (i, j)!= (self.visina, 1):
                    mozni_polozaji += [(i, j)]
        while len(siri) < stevilo_sirov:
            siri += [mozni_polozaji.pop]

        slika = tk.Canvas(okno, width = d * self.visina + 1,
                          height = d * self.visina + 1).place(x = 0, y = 0)

    def narisi(self):
        
        
