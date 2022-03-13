#!/usr/bin/env python3

from cProfile import label
from os.path import basename, splitext
import tkinter as tk
from tkinter import Listbox, END
#from typing_extensions import IntVar
from tkinter import IntVar, messagebox, StringVar

from numpy import True_

# from tkinter import ttk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        self.index = None
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.v = StringVar()

        self.prodavani = tk.Radiobutton(self, text="Prodej", variable=self.v, value=1, command=self.sel)
        self.prodavani.grid(row=1, column=1)

        self.nakupovani = tk.Radiobutton(self, text="Nákup", variable=self.v, value=2, command=self.sel)
        self.nakupovani.grid(row=2, column=1)

        self.vstup = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.vstup.grid(row=3, column=1)

        self.lbl_vysledek =tk.Label(self, text="", foreground="red")
        self.lbl_vysledek.grid(row=4, column=1)

        self.lbl_mena = tk.Label(self, text="CZK")
        self.lbl_mena.grid(row=4, column=2)

        self.lbl_cena = tk.Label(self, text="")
        self.lbl_cena.grid(row=5, column=3)

        self.lbl_final = tk.Label(self,text="")
        self.lbl_final.grid(row=5, column=6)

        self.tl = tk.Button(self, text = "Přepočet", command=self.final)
        self.tl.grid(row=7, column=1)

        self.lstBx = Listbox(self)
        self.lstBx.grid(row=5, column=1)
        self.lstBx.bind("<ButtonRelease-1>", self.kliknu)
        self.geometry("400x400")

        f = open("listek.txt")
        self.radky = f.readlines()

        self.prodejni_ceny = []
        self.nakupni_ceny = []

        self.carka = self.vstup.get().replace(",",".")

       

        for radek in self.radky:
            radek = radek.split()
            radek[3] = radek[3].replace(",", ".")
            radek[2] = radek[2].replace(",", ".")
            self.lstBx.insert(END, radek[0])
            self.prodejni_ceny.append(radek[3])
            self.nakupni_ceny.append(radek[2])

    def kliknu(self, event):
        self.index = self.lstBx.curselection()[0]
        print(self.radky[self.index])


    def nakup(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba","Nezadali jste vstupní hodnotu nebo nevybrali měnu!")
        else:
            self.p = float(self.vstup.get())*float(self.prodejni_ceny[self.index])
            self.lbl_vysledek.config(text=self.p)
            self.lbl_cena.config(text="Zaplatíte {} Kč.".format(round(self.p)))


    def prodej(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba", "Nezadali jste vstupní hodnotu nebo nevybrali měnu!")
        else:
            self.n = float(self.vstup.get())*float(self.nakupni_ceny[self.index])
            self.lbl_vysledek.config(text=self.n)
            self.lbl_cena.config(text="Dostanete {} Kč.".format(round(self.n)))

    
    
    def desetinne(self, value):
        try:
            float(value)
        except:
            return False
        return True

        
    def validate(self, value):
        if len(value) == 0 or value.isnumeric() or self.desetinne(value):
            return True
        else:
            return False

    


    def pocet(self):
        if self.v.get() == "1":
            self.prodej()
        elif self.v.get() == "2":
            self.nakup()
        else:
            messagebox.showwarning("Chyba", "Nezadali jste vstupní hodnotu nebo nevybrali měnu!")


    def sel(self):
        print(type(self.v.get()))


    def final(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba", "Nezadali jste vstupní hodnotu nebo nevybrali měnu!")
        else:
            self.pocet()





  

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()