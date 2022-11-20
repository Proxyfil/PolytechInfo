# one game
import tkinter as tk
import random
from PIL import Image, ImageTk

class Exemple(object):

    def __init__(self,master):
        self.master = master
        self.nvfenetre=tk.Toplevel(self.master)
        self.nvfenetre.title("Smileys")
        self.fr = tk.Frame(self.nvfenetre)
        self.fr.pack(padx=20, pady=10)

        self.lab1 = tk.Label(self.fr, text='5 euros par jeu, vous gagnez lorsque vous obtenez ":-D"')
        self.lab1.grid(row=0, column=0, columnspan= 3,padx=2, pady=2)
        
        self.lab2 = tk.Label(self.fr, text='', width=15, background="purple")
        self.lab2.grid(row=1, column=1, pady=15)

        self.b1 = tk.Button(self.fr, text="jouer", width=8, background="pink", command=self.jouer)
        self.b1.grid(row=2, column=0, padx=2, pady=(20,10))
        
        self.b2 = tk.Button(self.fr, text="quitter", width=8, background="pink", command=self.nvfenetre.destroy)
        self.b2.grid(row=2, column=2, padx=2, pady=(20,10))

        self.res = tk.StringVar()
        self.lab3 = tk.Label(self.fr,textvariable=self.res,background="pink", width=50)
        self.res.set("")
        self.lab3.grid(row=3,column=0, columnspan=3,pady=20)
        self.euros_gagnes = 0
        self.euros_dep = 0
        

        self.nvfenetre.mainloop()

    def jouer(self):
        self.lab2["text"] = random.choice([":-D",":-)",":-(",";-)"])
        if self.lab2["text"] == ":-D":
            self.euros_gagnes += 5
            self.euros_dep += 5
            self.res.set(f"Gagné! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros")
        else:
            self.euros_dep += 5
            self.res.set(f"Perdu! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros")

class JustePrix(object):
    def __init__(self,master):
        self.master = master
        self.nvfenetre=tk.Toplevel(self.master)
        self.nvfenetre.title("Juste Prix")
        self.fr = tk.Frame(self.nvfenetre)
        self.fr.pack(padx=20, pady=10)

        self.lab1 = tk.Label(self.fr, text="5 euros par jeu, vous gagnez lorsque vous trouvez le nombre aléatoire de l'ordinateur")
        self.lab1.grid(row=0, column=0, columnspan= 2,padx=2, pady=2)
        
        self.lab2 = tk.Label(self.fr, text='Entrez un entier entre 0 et 100 (bornes incluses):', background="lightyellow")
        self.lab2.grid(row=1, column=0, pady=5)
        
        self.cvar = tk.StringVar()
        self.entry = tk.Entry(self.fr, textvariable=self.cvar, width=10)
        self.entry.grid(row=1, column=1, pady=5)
        
        self.lab3 = tk.Label(self.fr, text='', width=15, background="orange")
        self.lab3.grid(row=2, column=0,columnspan=2, pady=5)
        
        self.lab4 = tk.Label(self.fr, text='', width=50, background="pink")
        self.lab4.grid(row=3, column=0, columnspan=2, pady=10)

        self.b1 = tk.Button(self.fr, text="jouer", width=8, background="red", command=self.jouer)
        self.b1.grid(row=4, column=0, padx=2, pady=(20,10))
        
        self.b2 = tk.Button(self.fr, text="quitter", width=8, background="red", command=self.nvfenetre.destroy)
        self.b2.grid(row=4, column=1, padx=2, pady=(20,10))

        self.euros_gagnes = 0
        self.euros_dep = 0
        
        self.nb = random.randint(0,100)

        self.nvfenetre.mainloop()
        
    def jouer(self):
        if self.entry.get().isdigit():
            if int(self.entry.get()) == self.nb:
                self.euros_gagnes += 5
                self.euros_dep += 5
                self.lab4["text"] = f"Bravo! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros"
                self.lab3["text"] = ""
                self.nb = random.randint(0,100)
            else:
                self.euros_dep += 5
                self.lab4["text"] = f"Perdu! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros"
                if int(self.entry.get()) > self.nb:
                    self.lab3["text"] = "Trop grand"
                else:
                    self.lab3["text"] = "Trop petit"

class Jeu_Des_Trois_Symboles(object):
    def __init__(self,master):
        
        self.master = master
        self.nvfenetre=tk.Toplevel(self.master)
        self.nvfenetre.title("Jeux des trois symboles")
        self.fr = tk.Frame(self.nvfenetre)
        self.fr.pack(padx=20, pady=10)
        
        self.lab1 = tk.Label(self.fr, text="5 euros par jeu, pour gagner il faut que les 3 symboles soient identiques")
        self.lab1.grid(row=0, column=0, columnspan= 3,padx=2, pady=2)
        
        self.image1 = tk.Canvas(self.fr, width=100, height=100, highlightbackground="black", highlightthickness=1)
        self.image2 = tk.Canvas(self.fr, width=100, height=100, highlightbackground="black", highlightthickness=1)
        self.image3 = tk.Canvas(self.fr, width=100, height=100, highlightbackground="black", highlightthickness=1)
        
        self.image1.grid(row=1, column=0, pady=20)
        self.image2.grid(row=1, column=1, pady=20)
        self.image3.grid(row=1, column=2, pady=20)
        
        self.play = tk.Button(self.fr, text="jouer", width=8, background="yellow", command=self.jouer)
        self.play.grid(row=2, column=1, pady=(20,10))
        
        self.lab2 = tk.Label(self.fr, text='', width=50, background="lightyellow")
        self.lab2.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.euros_gagnes = 0
        self.euros_dep = 0
    
    def jouer(self):
        self.image1.delete("all")
        self.image2.delete("all")
        self.image3.delete("all")
        self.liste_image_canvas = ["","",""]
        self.liste_image_name = ["","",""]
        for i in range(3):
            img = Image.open(random.choice(["TP11/SymbolsPictures/banane.jpg","TP11/SymbolsPictures/kiwi.jpg","TP11/SymbolsPictures/orange.jpg"]))
            self.photo = ImageTk.PhotoImage(img.resize((100,100)),master=self.fr)
            self.liste_image_canvas[i] = self.photo
            self.liste_image_name[i] = img
        self.image1.create_image(50,50,image=self.liste_image_canvas[0])
        self.fr.update()
        self.image2.create_image(50,50,image=self.liste_image_canvas[1])
        self.fr.update()
        self.image3.create_image(50,50,image=self.liste_image_canvas[2])
        self.fr.update()
        print(self.liste_image_canvas)
        if self.liste_image_name[0] == self.liste_image_name[1] == self.liste_image_name[2]:
            self.euros_gagnes += int(random.choice([20,30,40,50]))
            self.euros_dep += 5
            self.lab2["text"] = f"Bravo! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros"
        else:
            self.euros_dep += 5
            self.lab2["text"] = f"Perdu! Vous avez dépensé {self.euros_dep+self.euros_gagnes} euros et gagner {self.euros_gagnes} euros"