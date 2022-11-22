# several games
import tkinter as tk
from PIL import Image, ImageTk
import Exemple as ex

class Games(object):

    def __init__(self, master):
        self.master = master
        self.fr = tk.Frame(self.master)
        self.fr.pack()

        self.menubar = tk.Menu(self.fr)
        self.menubar.add_command(label="Smileys", command=self.lancementExemple1)
        self.menubar.add_command(label="Devinette", command=self.lancementExemple2)
        self.menubar.add_command(label="Jeux des trois symboles", command=self.lancementExemple3)
        self.menubar.add_command(label="Pendu", command=self.lancementExemple4)
        self.menubar.add_command(label="Quitter", command=self.master.destroy)
        self.master.config(menu=self.menubar)

        self.canvas = tk.Canvas(self.fr, width=500, height=200, background="lightpink")
        image = Image.open("SymbolsPictures/jeux.jpg")
        self.photo = ImageTk.PhotoImage(image.resize((200,200)),master=self.master)
        self.canvas.create_image(250,100,image=self.photo)
        self.canvas.pack()

    def lancementExemple1(self):
        ex.Exemple(self.master)
    def lancementExemple2(self):
        ex.JustePrix(self.master)
    def lancementExemple3(self):
        ex.Jeu_Des_Trois_Symboles(self.master)
    def lancementExemple4(self):
        ex.Pendu(self.master)

def main():
    fenetre = tk.Tk()
    fenetre.title("Games")
    app = Games(fenetre)
    fenetre.mainloop()
 
if __name__ == '__main__':
    main()

def division(a,b):
    if b == 0:
        return 0
    else:
        return division(a,b-1) + a