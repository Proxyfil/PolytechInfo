import tkinter as tk
from tkinter import messagebox
def kungs():
    test = messagebox.askyesno(title="Kungs", message="Hey you win a ticket concert, don't you know?")
    if test == True:
        messagebox.showinfo(title="Kungs", message="You're welcome")
    else:
        messagebox.showinfo(title="Kungs", message="Now you know!")

def synapson():
    test = messagebox.askyesno(title="Synapson", message="Hi, come visit us, maybe you'll see a fireball under the moonlight!")
    if test == True:
        messagebox.showinfo(title="Synapson", message="You know")
    else:
        messagebox.showinfo(title="Synapson", message="Ok, ok, as you feel...")

def beto():
    messagebox.showinfo(title="Bigflo et Oli",message="Nous aussi, on t'invite dans la cour des grands...")
def twopac():
    messagebox.showinfo(title="2pac",message="Make your life be like ;-)")
fen = tk.Tk()
fen.title("Musique :-)")
fr = tk.Frame(fen)
fr.config(width=200, height=200,background="lightgreen")
fr.pack()

menubar = tk.Menu(fr)
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Electro", menu=menu1)
menu1.add_command(label="Kungs", command=kungs)
menu1.add_command(label="Synapson", command=synapson)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Rap", menu=menu2)
menu2.add_command(label="Bigflo et Oli", command=beto)
menu2.add_command(label="2Pac", command=twopac)
fen.config(menu=menubar)
fen.mainloop()

"""
Ce programme permet de créer un menu déroulant avec des sous-menus et d'afficher des messages d'information.
"""