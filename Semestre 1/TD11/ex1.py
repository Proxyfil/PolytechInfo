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