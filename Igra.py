import tkinter as tk

#from Model import Labirint as lab
from labirinti import labirinti
from Model import Igra as igra


class Grafika:

    def __init__(self, okno):
        self.odmik = 4
        self.igra = igra()
        self.labirint = self.igra.labirint
        self.visina = self.labirint.visina * 40
        self.sirina = self.labirint.sirina * 40
        self.zacetek(okno)
        

    def zacetek(self, okno):
        #prikaz = tk.Frame(okno)
        okno.bind('<Key>', self.uporabnikov_vnos)
        self.plosca = tk.Canvas(okno,
                                width = self.sirina + 2 * self.odmik,
                                height = self.visina + 2 * self.odmik)
        self.plosca.grid(row = 1, column = 0, columnspan = 2)
        #self.plosca.create_line(0, 0, 100, 100, fill = 'red')
        gumb1 = tk.Button(okno, text = 'start', command = None)
        gumb1.grid(row = 0, column = 0, sticky=tk.W+tk.E+tk.N+tk.S)
        gumb2 = tk.Button(okno, text = 'konec', command = None)
        gumb2.grid(row = 0, column = 1, sticky=tk.W+tk.E+tk.N+tk.S)

        #self.plosca = tk.configure(background = 'white')
        self.mreza(okno)
        self.zapolni_polja(okno)
        self.osnovna_zanka(okno)

    def mreza(self, okno):
        #print('mreza')
        for i in range(self.labirint.visina + 1):
            self.plosca.create_line(self.odmik, i * self.visina/ self.labirint.visina + self.odmik,
                                    self.visina + self.odmik, i * self.visina / self.labirint.visina + self.odmik,
                                    fill = 'black')
        for i in range(self.labirint.sirina + 1):
            self.plosca.create_line(i * self.sirina/ self.labirint.sirina + self.odmik, self.odmik,
                                    i * self.sirina / self.labirint.sirina + self.odmik, self.sirina + self.odmik,
                                    fill = 'black')

    def zapolni_polja(self, okno):
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
        #self.uporabnikov_vnos()
        uspesen_premik = self.igra.premakni_mis()
        #ce je premik uspesen, se odsteje tocka, mis premakne
        if uspesen_premik == True:
            self.igra.tocke -= 1
        #print(self.igra.tocke)
        #konec igre
        if self.igra.konec_igre():
            pass
            #print('konec igre')
        self.mreza(okno)
        self.zapolni_polja(okno)
        okno.after(100, lambda: self.osnovna_zanka(okno))

    def uporabnikov_vnos(self, event):
        if event.keysym == 'w':
            self.igra.smer = (-1, 0) #gor
        elif event.keysym == 's':
            self.igra.smer = (1, 0) #dol
        elif event.keysym == 'a':
            self.igra.smer = (0, -1) #levo
        elif event.keysym == 'd':
            self.igra.smer = (0, 1) #desno

okno = tk.Tk()

moj_program = Grafika(okno)
okno.mainloop()
        
        
