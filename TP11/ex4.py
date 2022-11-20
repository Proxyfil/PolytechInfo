import tkinter as tk
import random
from sympy import *

class Integrales(object):
    def __init__(self, master):
        self.lancer = -1
        self.nbde1 = False
        self.nbde2 = False
        self.nbde3 = False
        self.master = master
        self.master = tk.Frame(self.master)
        self.master.pack(padx=20, pady=10)
        
        self.lab1 = tk.Label(self.master, text="Vous souhaitez calculer une intégrale?",font=("Arial24",10))
        self.lab1.grid(row=0, column=0, columnspan=2)
        
        self.lab2 = tk.Label(self.master, text="Entrez la fonction, en fonction de x:",font=("Arial24",10))
        self.lab2.grid(row=1, column=0, sticky=tk.E)
        
        self.var1 = tk.StringVar()
        
        self.entry1 = tk.Entry(self.master, width=50, textvariable=self.var1)
        self.entry1.grid(row=1, column=1, sticky=tk.W)
        
        self.lab3 = tk.Label(self.master, text="Entrez la borne inférieure:",font=("Arial24",10))
        self.lab3.grid(row=2, column=0, sticky=tk.E)
        
        self.var2 = tk.StringVar()
        
        self.entry2 = tk.Entry(self.master, width=10, textvariable=self.var2)
        self.entry2.grid(row=2, column=1, sticky=tk.W)
        
        self.lab4 = tk.Label(self.master, text="Entrez la borne supérieure:",font=("Arial24",10))
        self.lab4.grid(row=3, column=0, sticky=tk.E)
        
        self.var3 = tk.StringVar()
        
        self.entry3 = tk.Entry(self.master, width=10, textvariable=self.var3)
        self.entry3.grid(row=3, column=1, sticky=tk.W)
        
        self.valider = tk.Button(self.master, text="calculer", background="pink", command=lambda : self.integrale(self.var1.get(), self.var2.get(), self.var3.get()))
        self.valider.grid(row=4, column=1)
        
        self.lab5 = tk.Label(self.master, text="",font=("Arial24",10), background="purple", width=25, foreground="white")
        self.lab5.grid(row=5, column=0, columnspan=2, pady=15)
        
    def integrale(self, function, bornea, borneb):
        x = Symbol('x')
        integrale = integrate(function, (x, bornea, borneb))
        self.lab5["text"] = integrale
        

def main():
    root = tk.Tk()
    root.title("Intégrales")
    app = Integrales(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
