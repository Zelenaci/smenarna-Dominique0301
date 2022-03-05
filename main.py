#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Listbox, END
#from typing_extensions import IntVar
from tkinter import IntVar, messagebox

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
    name = "Foo"

    def __init__(self):
        self.index = None
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.v = IntVar()

        self.prodej = tk.Radiobutton(self, text="prodej", variable=self.v, value=1, command=self.prodej)
        self.prodej.pack()

        self.nakup = tk.Radiobutton(self, text="nákup", variable=self.v, value=2, command=self.nakup)
        self.nakup.pack()

        self.vstup = tk.Entry(self)
        self.vstup.pack()

        self.lbl_vysledek =tk.Label(self, text="")
        self.lbl_vysledek.pack()

        self.lstBx = Listbox(self)
        self.lstBx.pack()
        self.lstBx.bind("<ButtonRelease-1>", self.kliknu)

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
            messagebox.showwarning("Chyba","Nezadali jste vstupní hodnotu!")
        else:
            self.p = int(self.vstup.get())*float(self.prodejni_ceny[self.index])
            self.lbl_vysledek.config(text=self.p)


    def nakup(self):
        if self.index == None or self.vstup.get() == "":
            messagebox.showwarning("Chyba", "Nezadali jste vstupní hodnotu!")
        else:
            self.n = int(self.vstup.get())*float(self.nakupni_ceny[self.index])
            self.lbl_vysledek.config(text=self.n)


        
        


    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()