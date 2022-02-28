#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Listbox, END
#from typing_extensions import IntVar
from tkinter import IntVar

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
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()
        self.v = IntVar()

        self.prodej = tk.Radiobutton(self, text="prodej", variable=self.v, value=1, command=self.nakupuji)
        self.prodej.pack()

        self.nakup = tk.Radiobutton(self, text="nákup", variable=self.v, value=2)
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

        for radek in self.radky:
            radek = radek.split()
            self.lstBx.insert(END, radek[0])

    def kliknu(self, event):
        index = self.lstBx.curselection()[0]
        print(self.radky[index])


    def nakupuji(self):
        self.n = int(self.vstup.get())*int(self.radek[0])
        self.lbl_vysledek.config(text=self.n)
        
        


    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()