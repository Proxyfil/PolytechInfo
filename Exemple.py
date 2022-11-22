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
            img = Image.open(random.choice(["SymbolsPictures/banane.jpg","SymbolsPictures/kiwi.jpg","SymbolsPictures/orange.jpg"]))
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

class Pendu(object):
    def __init__(self, master):
        self.motpendu = random.choice(["python","java","c","c++","c#","javascript","php","ruby","swift","kotlin","go","rust","scala","perl","haskell","fortran","cobol","pascal","ada","lisp","prolog","erlang","clojure","d","dart","groovy","lua","r","matlab","delphi","visualbasic","assembly","html","css","sql","bash","powershell","typescript","actionscript","apl","awk","basic","brainfuck","caml","cobol","dylan","erlang","fortran","haskell","icon","j","julia","lisp","logo","ml","modula2","nemerle","oberon","ocaml","pascal","perl","prolog","python","r","ruby","sml","scheme","smalltalk","tcl","verilog","vhdl","xml"])
        self.nbfautes = 0
        self.motpenducache = "_"*len(self.motpendu)
        self.lettre = []
        self.alllettres = []
        self.master = master
        self.nvfenetre=tk.Toplevel(self.master)
        self.nvfenetre.title("Pendu")
        self.fr = tk.Frame(self.nvfenetre)
        self.fr.pack(padx=20, pady=10)

        self.lab1 = tk.Label(self.fr, text="Jeu gratuit")
        self.lab1.grid(row=0, column=0, columnspan= 3,padx=2, pady=2)

        self.lab2 = tk.Label(self.fr, text="Entrez le mot a trouver (5 lettres mini, 20 maxi, minuscules sans accents) ou random:")
        self.lab2.grid(row=1, column=0, columnspan= 2,padx=2, pady=2)

        self.cvar1 = tk.StringVar()
        self.cvar2 = tk.StringVar()

        self.entry = tk.Entry(self.fr, width=20, textvariable=self.cvar1)
        self.entry.grid(row=1, column=2, padx=2, pady=2)

        self.valider = tk.Button(self.fr, text="Valider", width=8, background="blue", command=self.valider)
        self.valider.grid(row=2, column=2)

        self.lab3 = tk.Label(self.fr, text='Entrer une lettre minuscule non accentuée:', background="lightyellow")
        self.lab3.grid(row=3, column=1, columnspan=3)

        self.entry2 = tk.Entry(self.fr, width=20, textvariable=self.cvar2)
        self.entry2.grid(row=4, column=1, columnspan=2)

        self.pendu = tk.Canvas(self.fr, width=300, height=300, background="green")
        self.pendu.grid(row=5, column=0, columnspan=3, pady=10)

        self.lab4 = tk.Label(self.fr, text='', width=20, background="skyblue")
        self.lab4.grid(row=6, column=0, columnspan=3, pady=10)

        self.jouer = tk.Button(self.fr, text="jouer", background="red", command=self.jouer, width=8)
        self.jouer.grid(row=7, column=0, columnspan=2, pady=10)

        self.quitter = tk.Button(self.fr, text="quitter", background="red", command=self.nvfenetre.destroy, width=8)
        self.quitter.grid(row=7, column=2, pady=10)

    def valider(self):
        self.last = self.cvar2.get()
        if self.cvar2.get() in self.alllettres:
            self.lab4["text"] = "Vous avez déjà entré cette lettre"
            return None
        elif self.cvar1.get() == self.motpendu:
            self.lab4["text"] = "Bravo! Vous avez gagné!"
        elif self.nbfautes == 10:
            self.lab4["text"] = "Perdu! Vous avez fait trop de fautes"
        elif self.motpenducache == self.motpendu:
            self.lab4["text"] = "Bravo! Vous avez gagné!"
        else:
           if self.cvar2.get() in self.motpendu:
               self.lettre.append(self.cvar2.get())
               self.motpenducache = ""
               for i in self.motpendu:
                   if i in self.lettre:
                       self.motpenducache += i
                   else:
                       self.motpenducache += "_"
               self.lab4["text"] = self.motpenducache
           elif self.cvar2.get() not in self.motpendu:
               self.lab4["text"] = self.motpenducache
               self.nbfautes += 1
               self.ajoutbaton()
        self.alllettres.append(self.cvar2.get())


    def ajoutbaton(self):
        if self.nbfautes == 1:
            self.pendu.create_line(50, 250, 250, 250)
        elif self.nbfautes == 2:
            self.pendu.create_line(150, 250, 150, 50)
        elif self.nbfautes == 3:
            self.pendu.create_line(150, 50, 250, 50)
        elif self.nbfautes == 4:
            self.pendu.create_line(250, 50, 250, 100)
        elif self.nbfautes == 5:
            self.pendu.create_oval(240, 100, 260, 120)
        elif self.nbfautes == 6:
            self.pendu.create_line(250, 120, 250, 200)
        elif self.nbfautes == 7:
            self.pendu.create_line(250, 140, 220, 180)
        elif self.nbfautes == 8:
            self.pendu.create_line(250, 140, 280, 180)
        elif self.nbfautes == 9:
            self.pendu.create_line(250, 200, 220, 240)
        elif self.nbfautes == 10:
            self.pendu.create_line(250, 200, 280, 240)

    def jouer(self):
        self.motpendu = random.choice(["python","java","c","c++","c#","javascript","php","ruby","swift","kotlin","go","rust","scala","perl","haskell","fortran","cobol","pascal","ada","lisp","prolog","erlang","clojure","d","dart","groovy","lua","r","matlab","delphi","visualbasic","assembly","html","css","sql","bash","powershell","typescript","actionscript","apl","awk","basic","brainfuck","caml","cobol","dylan","erlang","fortran","haskell","icon","j","julia","lisp","logo","ml","modula2","nemerle","oberon","ocaml","pascal","perl","prolog","python","r","ruby","sml","scheme","smalltalk","tcl","verilog","vhdl","xml"])
        self.lettre = []
        self.nbfautes = 0
        self.motpenducache = "_" * len(self.motpendu)
        self.lab4["text"] = self.motpenducache
        self.pendu.delete("all")
