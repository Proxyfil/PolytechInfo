#exo debut saisie nom
import tkinter as tk
def viderText(event):
 entree.delete(0,tk.END)

def mafct():
 v2.set(f"Bien le bonjour {entree.get()}")

fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)
lab1 = tk.Label(maFrame, text="Nom ?")
lab1.grid(row=0, column=0, padx=2, pady=2)
v1 = tk.StringVar()
v1.set("Taper votre nom ici")
v3 = tk.IntVar()
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