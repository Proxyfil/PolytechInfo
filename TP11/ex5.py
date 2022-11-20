import tkinter as tk
import random
from PIL import ImageTk, Image

class portes(object):
    def __init__(self, master):
        self.liste_cadeau = ["images/argent.jpg","images/barcelone.jpg","images/theatre.jpg","images/perdu.png"]
        self.lancer = -1
        self.nbde1 = False
        self.nbde2 = False
        self.nbde3 = False
        self.master = master
        self.master = tk.Frame(self.master)
        self.master.pack(padx=20, pady=10)
        
        self.lab1 = tk.Label(self.master, text="4 niveaux de lots, lorsque vous gagnez un lot, vous pouvez de nouveau ouvrir une porte,\nmais si vous perdez avec cette nouvelle porte, vous perdez tout...")
        self.lab1.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.rectangle = tk.Canvas(self.master, width=400, height=100)
        self.rectangle.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.porte1 = tk.Canvas(self.master, width=80, height=240, background="pink")
        self.porte1.create_oval(50,115,75,120, fill="black")
        self.porte2 = tk.Canvas(self.master, width=80, height=240, background="lightgreen")
        self.porte2.create_oval(50,115,75,120, fill="black")
        self.porte3 = tk.Canvas(self.master, width=80, height=240, background="lightblue")
        self.porte3.create_oval(50,115,75,120, fill="black")
        
        self.var1 = tk.StringVar()
        self.var1.set("relancer")
        
        self.cvar = tk.IntVar()
        self.cvar.set(1)
        
        self.c1 = tk.Radiobutton(self.master, text="", variable=self.cvar, value=1)
        self.c1.grid(row=2, column=0)
        
        self.c2 = tk.Radiobutton(self.master, text="", variable=self.cvar, value=2)
        self.c2.grid(row=2, column=1)
        
        self.c3 = tk.Radiobutton(self.master, text="", variable=self.cvar, value=3)
        self.c3.grid(row=2, column=2)
        
        self.porte1.grid(row=1, column=0)
        self.porte2.grid(row=1, column=1)
        self.porte3.grid(row=1, column=2)
        
        self.valider = tk.Button(self.master, text="jouer", background="yellow", width=8, command=lambda: self.tirage())
        self.valider.grid(row=3, column=1, pady=20)   
    
        self.lab2 = tk.Label(self.master, text="", width=25, background="lightyellow")
        self.lab2.grid(row=4, column=1, pady=10)
    
    def tirage(self):
        if self.cvar.get() == 1 or self.cvar.get() == 2 or self.cvar.get() == 3:
            self.porte1.delete("all")
            self.porte2.delete("all")
            self.porte3.delete("all")
            self.porte1.create_oval(50,115,75,120, fill="black")
            self.porte2.create_oval(50,115,75,120, fill="black")
            self.porte3.create_oval(50,115,75,120, fill="black")
            self.lab2.config(text="")
            if self.cvar.get() == 1:
                porte = self.porte1
                porte.delete("all")
                image = random.choice(self.liste_cadeau)
                self.img1 = ImageTk.PhotoImage(Image.open(image))
                porte.create_image(41,100, image=self.img1)
            elif self.cvar.get() == 2:
                porte = self.porte2
                porte.delete("all")
                image = random.choice(self.liste_cadeau)
                self.img2 = ImageTk.PhotoImage(Image.open(image))
                porte.create_image(41,100, image=self.img2)
            elif self.cvar.get() == 3:
                porte = self.porte3
                porte.delete("all")
                image = random.choice(self.liste_cadeau)
                self.img3 = ImageTk.PhotoImage(Image.open(image))
                porte.create_image(41,100, image=self.img3)
            if image == "images/perdu.png":
                self.lab2.config(text="Perdu!")
                self.cvar.set(0)
                self.c1.config(state="disabled")
                self.c2.config(state="disabled")
                self.c3.config(state="disabled")
            elif image == "images/argent.jpg":
                self.lab2.config(text="1000€")
            elif image == "images/barcelone.jpg":
                self.lab2.config(text="1 we à Barcelone")
            elif image == "images/theatre.jpg":
                self.lab2.config(text="2 places de théâtre")
        
        

def main():
    root = tk.Tk()
    root.title("Portes")
    app = portes(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
