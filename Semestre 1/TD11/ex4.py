import tkinter as tk

def dessert():
    try:
        lab2.configure(text=f"{liste_dessert.get(liste_dessert.curselection())}: excellent choix!")
        fen.update()
    except:
        lab2.configure(text="Vous devez choisir un dessert!")
        fen.update()

fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)

lab1 = tk.Label(maFrame, text="Choissisez:")
lab1.grid(row=0, column=0, padx= 10)

liste_dessert = tk.Listbox(maFrame, selectmode=tk.SINGLE, height=4, width=20)
liste_dessert.insert(1, "Mousse au chocolat")
liste_dessert.insert(2, "Tarte aux pommes")
liste_dessert.insert(3, "Pêche Melba")

liste_dessert.grid(row=0, column=1, padx= 20)

valider = tk.Button(maFrame, text="valider", background="lightgreen",width=8, command=dessert)
valider.grid(row=1, column=0, pady=10)

quitter = tk.Button(maFrame, text="quitter", background="lightgreen",width=8, command=fen.destroy)
quitter.grid(row=1, column=1, pady=10)

lab2 = tk.Label(maFrame, text="", background="lightblue", font=("Arial24",10), width=30)
lab2.grid(row=2, column=0, columnspan=2, pady=4)

fen.mainloop()