#Exercice 1

import tkinter as tk
root = tk.Tk()
root.title("Exemple")
root.mainloop()

"""
La variable root permet de créer une fenêtre graphique.
root.mainloop() permet de lancer la fenêtre graphique.
"""

import tkinter as tk
root = tk.Tk()
root.title("Exemple")
frame1 = tk.Frame(root, background='lightblue')
frame1.pack(padx=20, pady=20, fill=tk.BOTH)
root.mainloop()

"""
On met juste une ligne mince car on ne veut pas que la fenêtre soit trop grande.
si on met root.mainloop() avant frame1.pack(), la fenêtre ne s'affiche pas.
"""

import tkinter as tk
root = tk.Tk()
root.title("Exemple")
frame1 = tk.Frame(root, background="lightblue")
frame1.pack(padx=20, pady=20, fill=tk.BOTH)
lab1 = tk.Label(frame1, text="Hello 1",background="purple",font="Arial24",foreground="white")
lab2 = tk.Label(frame1, text="Hello 2",background="pink",font=("Arial24",25),foreground="black")
lab1.grid(row=0, column=1, padx=10, pady=10)
lab2.grid(row=1, column=0, padx=10, pady=10)

b1 = tk.Button(frame1, text="fermer", width=8, background="darkblue",
foreground="white",command=root.destroy)
b1.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

root.mainloop()

"""
lab1 permet de créer un label.
grid permet de placer le label dans la fenêtre.
on obtient un texte centré car on a mis padx et pady.
root.destroy permet de fermer la fenêtre.
Le bouton est centré car on a mis columnspan=2.
"""

#Exercice 2

#exo debut saisie nom
import tkinter as tk
def viderText(event):
 entree.delete(0,tk.END)

def mafct():
 v2.set("Bien le bonjour",entree.get())

fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)
lab1 = tk.Label(maFrame, text="Nom ?")
lab1.grid(row=0, column=0, padx=2, pady=2)
v1 = tk.StringVar()
v1.set("Taper votre nom ici")
entree = tk.Entry(maFrame, textvariable=v1, width=30)
entree.grid(row=0, column=1, padx=2, pady=2)
entree.bind("<ButtonRelease>",viderText)
v2 = tk.StringVar()
lab2 = tk.Label(maFrame, textvariable=v2)
lab2.grid(row=1, column=0, columnspan=2, padx=2, pady=5)
b1 = tk.Button(maFrame, text="cliquer", width=8, background="pink", command=mafct)
b1.grid(row=2, column=0, columnspan=2, padx=2, pady=2)
fen.mainloop()

"""
La ligne 1 permet de créer une fenêtre.
La ligne 2 permet de créer une frame.
La ligne 3 permet de placer la frame dans la fenêtre.
La ligne 4 permet de créer un label.
La ligne 5 permet de placer le label dans la frame.
La ligne 6 permet de créer une variable de type StringVar.
La ligne 7 permet de mettre une valeur par défaut dans la variable.
La ligne 8 permet de créer une zone de saisie.
La ligne 9 permet de placer la zone de saisie dans la frame.
La ligne 10 permet de vider la zone de saisie quand on clique dessus.
La ligne 11 permet de créer une variable de type StringVar.
La ligne 12 permet de créer un label.
La ligne 13 permet de placer le label dans la frame.
La ligne 14 permet de créer un bouton.
La ligne 15 permet de placer le bouton dans la frame.
La ligne 16 permet de lancer la fenêtre.
"""

#Exercice 3

import tkinter as tk
import random

fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)
lab1 = tk.Label(maFrame, text="Un chiffre noir ou rouge va sortir...\nCliquer ce que vous pensez obtenir")
lab1.grid(row=0, column=1)
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(maFrame, text='chiffre pair',variable=var1, onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(maFrame, text='rouge',variable=var2, onvalue=1, offvalue=0)
c2.pack()
rectangle_bleu = tk.Canvas(maFrame, width=100, height=200, background='blue')
c1.grid(row=1, column=0)
c2.grid(row=1, column=2)
rectangle_bleu.grid(row=2, column=1)

rectangle_bleu.create_text(50, 100, text="0", font="Arial 24", fill="white")
fen.mainloop()