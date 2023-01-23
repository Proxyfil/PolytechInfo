import tkinter as tk
from tkinter import messagebox
import random

def plat():
    global entry1,lab1, valider
    lab1.grid(row=0, column=0)
    lab1.config(text="Quel est votre plat préféré?")
    entry1.grid(row=1, column=0,pady=5)
    valider.grid(row=2, column=0, pady=5)

def dessert():
    global entry1,lab1, valider
    lab1.grid(row=0, column=0)
    lab1.config(text="Quel est votre dessert préféré?")
    entry1.grid(row=1, column=0,pady=5)
    valider.grid(row=2, column=0, pady=5)
    
def enter(event):
    global entry1,lab1,cvar
    liste_jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    messagebox.showinfo("Bonne nouvelle", f"Nous vous cuisinerons un(e) {cvar.get()} {random.choice(liste_jour)}")

fen = tk.Tk()
fen.title("Miam")
fen.configure(background="#fffce4", padx=10, pady=10)

menubar = tk.Menu(fen)
menubar.add_command(label="Plat", command=plat)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_command(label="Dessert", command=dessert)
lab1 = tk.Label(text="", background="#f8f4f4", width=50)
cvar = tk.StringVar()
entry1 = tk.Entry(textvariable=cvar, width=40)
valider = tk.Button(text="Ok", command=lambda : enter(None), background="#ffc4cc", width=10)
fen.bind("<Return>", enter)
fen.config(menu=menubar)
fen.mainloop()