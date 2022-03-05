#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Listbox, END
#from typing_extensions import IntVar
from tkinter import IntVar, messagebox

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
        self.v = IntVar()

        self.prodej = tk.Radiobutton(self, text="prodej", variable=self.v, value=1, command=self.prodej)
        self.prodej.grid(row=1, column=1)

        self.nakup = tk.Radiobutton(self, text="nákup", variable=self.v, value=2, command=self.nakup)
        self.nakup.grid(row=2, column=1)

        self.vstup = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.vstup.grid(row=3, column=1)

        self.lbl_vysledek =tk.Label(self, text="")
        self.lbl_vysledek.grid(row=4, column=1)

        self.lbl_mena = tk.Label(self, text="CZK")
        self.lbl_mena.grid(row=4, column=2)

        self.lstBx = Listbox(self)
        self.lstBx.grid(row=5, column=1)
        self.lstBx.bind("<ButtonRelease-1>", self.kliknu)
        self.geometry("400x500")

        f = open("listek.txt")
        self.radky = f.readlines()

        self.prodejni_ceny = []
        self.nakupni_ceny = []
       

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


    def prodej(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba","Nezadali jste vstupní hodnotu nebo nevybrali měnu!")
        else:
            self.p = float(self.vstup.get())*float(self.prodejni_ceny[self.index])
            self.lbl_vysledek.config(text=self.p)


    def nakup(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba", "Nezadali jste vstupní hodnotu nebo nevybrali měnu!")
        else:
            self.n = float(self.vstup.get())*float(self.nakupni_ceny[self.index])
            self.lbl_vysledek.config(text=self.n)

    
    
    def desetinne(self):
        try:
            float(self.vstup.get())
        except:
            return False
        return True

        
    def validate(self, value):
        if len(value) == 0 or value.isnumeric() or self.desetinne():
            return True
        else:
            return False


  

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()