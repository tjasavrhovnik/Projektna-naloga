import tkinter as tk
import sys
import os

from labirinti import labirinti
from Model import Igra as igra

class Grafika:

    def __init__(self, okno):
        #kje na zaslonu se odpre okno
        pozicija = '330x360+100+100'
        okno.geometry(pozicija)
        #nastavimo rob
        self.odmik = 4
        self.zacetek(okno)

    def zacetek(self, okno):
        #odpremo igro: narisemo labirint, polja, pozenemo igro
        self.igra_tece = True
        self.igra = igra()
        self.labirint = self.igra.labirint
        self.visina = self.labirint.visina * 40
        self.sirina = self.labirint.sirina * 40
        okno.bind('<Key>', self.uporabnikov_vnos)
        self.plosca = tk.Canvas(okno,
                                width = self.sirina + 2 * self.odmik,
                                height = self.visina + 2 * self.odmik)
        self.plosca.grid(row = 1, column = 0, columnspan = 3)

        #ta gumb kliknemo, ce zelimo zaceti novo igro
        gumb1 = tk.Button(okno, text = 'NOVA IGRA', command = lambda: self.resetiraj_igro(okno))
        gumb1.grid(row = 0, column = 0, sticky=tk.W+tk.E+tk.N+tk.S)

        #tu se izpise rezultat (izgubljena igra/zmaga)
        self.text1_variable = tk.StringVar()
        text1 = tk.Label(okno, textvariable = self.text1_variable, height = 1, width = 10)
        text1.grid(row = 0, column = 1, sticky=tk.W+tk.E+tk.N+tk.S)

        #tu stejemo tocke
        self.text2_variable = tk.StringVar()
        text2 = tk.Label(okno, textvariable = self.text2_variable, height = 1, width = 10, relief = tk.FLAT)
        text2.grid(row = 0, column = 2, sticky=tk.W+tk.E+tk.N+tk.S)

        self.igra.izrisi_polja()
        self.mreza(okno)
        self.zapolni_polja(okno)
        self.osnovna_zanka(okno)

    def mreza(self, okno):
        #narisemo podlago labirinta (vodoravne in navpicne crte)
        for i in range(self.labirint.visina + 1):
            self.plosca.create_line(self.odmik, i * self.visina / self.labirint.visina + self.odmik,
                                    self.sirina + self.odmik, i * self.visina / self.labirint.visina + self.odmik,
                                    fill = 'black') 
        for i in range(self.labirint.sirina + 1):
            self.plosca.create_line(i * self.sirina / self.labirint.sirina + self.odmik, self.odmik,
                                    i * self.sirina / self.labirint.sirina + self.odmik, self.visina + self.odmik,
                                    fill = 'black')
          
    def zapolni_polja(self, okno):
        #polja ustrezno zapolnimo glede na vrednosti
        for y in range(len(self.labirint.matrika)):
            for x in range(len(self.labirint.matrika[0])):
                if self.labirint.matrika[y][x] == 0:
                    self.narisi_zid(okno, x, y)
                elif self.labirint.matrika[y][x] == -1:
                    self.narisi_prazno(okno, x, y)
                elif self.labirint.matrika[y][x] == 1:
                    self.narisi_mis(okno, x, y)
                elif self.labirint.matrika[y][x] == 2:
                    self.narisi_sir(okno, x, y)

    def narisi_zid(self, okno, x, y):
        self.plosca.create_rectangle(self.odmik + x * 40, self.odmik + y * 40,
                                     self.odmik + (x + 1) * 40, self.odmik + (y + 1) * 40,
                                     fill = 'grey')

    def narisi_prazno(self, okno, x, y):
        self.plosca.create_rectangle(self.odmik + x * 40, self.odmik + y * 40,
                                     self.odmik + (x + 1) * 40, self.odmik + (y + 1) * 40,
                                     fill = 'white')

    def narisi_sir(self, okno, x, y):
        self.narisi_prazno(okno, x, y)
        self.plosca.create_polygon(self.odmik + x * 40 + 20, self.odmik + y * 40 + 10,
                                   self.odmik + x * 40 + 10, self.odmik + y * 40 + 30,
                                   self.odmik + x * 40 + 30, self.odmik + y * 40 + 30,
                                   fill = 'yellow')

    def narisi_mis(self, okno, x, y):
        self.narisi_prazno(okno, x, y)
        self.plosca.create_arc(self.odmik + x * 40 + 10, self.odmik + y * 40 + 10,
                               self.odmik + x * 40 + 30, self.odmik + y * 40 + 30,
                               start = 0, extent = 359,
                               fill = 'blue')

    def osnovna_zanka(self, okno):
        #uporabnik vnese zelen premik
        uspesen_premik = self.igra.premakni_mis()
        #po uspesnem premiku osvezimo tocke
        if uspesen_premik == True:
            self.igra.tocke -= 1
        self.text2_variable.set('TOČKE: ' + str(self.igra.tocke))
        #konec igre in izpis rezultata
        koncaj = self.igra.konec_igre()
        if koncaj != 0:
            if koncaj == 1:
                self.text1_variable.set('Zmagal si!')
            elif koncaj == -1:
                self.text1_variable.set('Izgubil si!')
            self.igra_tece = False
        #osvezimo prikaz
        self.zapolni_polja(okno)

        if self.igra_tece == True:
            okno.after(100, lambda: self.osnovna_zanka(okno))
        else:
            print('konec')

    def uporabnikov_vnos(self, event):
        #nastavimo tipke za premikanje
        if event.keysym == 'w':
            self.igra.smer = (-1, 0) #gor
        elif event.keysym == 's':
            self.igra.smer = (1, 0) #dol
        elif event.keysym == 'a':
            self.igra.smer = (0, -1) #levo
        elif event.keysym == 'd':
            self.igra.smer = (0, 1) #desno

    def resetiraj_igro(self, okno):
        python = sys.executable
        os.execl(python, python, * sys.argv)

okno = tk.Tk()

moj_program = Grafika(okno)
okno.mainloop()
        
