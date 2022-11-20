import tkinter as tk
import random

class Jeu_4_2_1(object):
    def __init__(self, master):
        self.lancer = -1
        self.nbde1 = False
        self.nbde2 = False
        self.nbde3 = False
        self.master = master
        self.master = tk.Frame(self.master)
        self.master.pack(padx=20, pady=10)
        
        self.rectangle = tk.Canvas(self.master, width=400, height=100, background="pink")
        self.rectangle.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        self.de1 = tk.Canvas(self.master, width=80, height=80, background="white", highlightbackground="black")
        self.de2 = tk.Canvas(self.master, width=80, height=80, background="white", highlightbackground="black")
        self.de3 = tk.Canvas(self.master, width=80, height=80, background="white", highlightbackground="black")
        
        self.var1 = tk.StringVar()
        self.var1.set("relancer")
        
        self.c1var = tk.IntVar()
        self.c1var.set(1)
        self.c2var = tk.IntVar()
        self.c2var.set(1)
        self.c3var = tk.IntVar()
        self.c3var.set(1)
        
        self.c1 = tk.Checkbutton(self.master, textvariable=self.var1, state=tk.DISABLED, onvalue=1, offvalue=0, variable=self.c1var)
        self.c1.grid(row=1, column=0)
        
        self.c2 = tk.Checkbutton(self.master, textvariable=self.var1, state=tk.DISABLED, onvalue=1, offvalue=0, variable=self.c2var)
        self.c2.grid(row=1, column=1)
        
        self.c3 = tk.Checkbutton(self.master, textvariable=self.var1, state=tk.DISABLED, onvalue=1, offvalue=0, variable=self.c3var)
        self.c3.grid(row=1, column=2)
        
        self.de1.grid(row=0, column=0)
        self.de2.grid(row=0, column=1)
        self.de3.grid(row=0, column=2)
        
        self.lab2 = tk.Label(self.master, text="",background="lightblue",font=("Arial24",10), width=15)
        self.lab2.grid(row=3, column=0, columnspan=3)
        
        self.valider = tk.Button(self.master, text="jouer", background="lightgreen", width=8, command=lambda: self.jouer([self.c1var.get(), self.c2var.get(), self.c3var.get()]))
        self.valider.grid(row=2, column=0, pady=10, sticky=tk.E)   
        
        self.restart_b = tk.Button(self.master, text="restart", background="lightgreen", width=8, command=self.restart, state=tk.DISABLED)
        
        self.quitter = tk.Button(self.master, text="quitter", background="lightgreen", width=8, command=self.master.quit)
        self.quitter.grid(row=2, column=2, pady=10, sticky=tk.W)
    
    def DrawDice(self, liste_des):
        liste_de = []
        if liste_des[0] == 1:
            liste_de.append(self.de1)
            self.de1.delete("all")
        if liste_des[1] == 1:
            liste_de.append(self.de2)
            self.de2.delete("all")
        if liste_des[2] == 1:
            liste_de.append(self.de3)
            self.de3.delete("all")
        print(liste_de)
        for de in liste_de:
            nb_points = random.randint(1,6)
            print(f"de = {de} nb_points = {nb_points}")
            if nb_points == 1 and de == self.de3:
                self.nbde3 = True
                self.c3.configure(state=tk.DISABLED)
            if nb_points == 2 and de == self.de2:
                self.nbde2 = True
                self.c2.configure(state=tk.DISABLED)
            if nb_points == 4 and de == self.de1:
                self.nbde1 = True
                self.c1.configure(state=tk.DISABLED)
            if nb_points == 1:
                de.create_oval(35,35,50,50, fill="black")
            elif nb_points == 2:
                de.create_oval(35,20,50,35, fill="black")
                de.create_oval(35,50,50,65, fill="black")
            elif nb_points == 3:
                de.create_oval(35,10,50,25, fill="black")
                de.create_oval(35,35,50,50, fill="black")
                de.create_oval(35,60,50,75, fill="black")
            elif nb_points == 4:
                de.create_oval(15,15,30,30, fill="black")
                de.create_oval(55,15,70,30, fill="black")
                de.create_oval(15,55,30,70, fill="black")
                de.create_oval(55,55,70,70, fill="black")
            elif nb_points == 5:
                de.create_oval(15,15,30,30, fill="black")
                de.create_oval(55,15,70,30, fill="black")
                de.create_oval(35,35,50,50, fill="black")
                de.create_oval(15,55,30,70, fill="black")
                de.create_oval(55,55,70,70, fill="black")
            elif nb_points == 6:
                de.create_oval(15,15,30,30, fill="black")
                de.create_oval(55,15,70,30, fill="black")
                de.create_oval(15,35,30,50, fill="black")
                de.create_oval(55,35,70,50, fill="black")
                de.create_oval(15,55,30,70, fill="black")
                de.create_oval(55,55,70,70, fill="black")    
            if self.nbde1 == True and self.nbde2 == True and self.nbde3 == True:
                self.lab2["text"] = "Gagné !" 
                self.valider.configure(state=tk.DISABLED)
                self.restart_b.grid(row=2, column=1, pady=10)
                self.restart_b.configure(state=tk.NORMAL)
    def jouer(self,liste):
        if self.lancer == -1:
            self.DrawDice([1,1,1])
            self.lancer = 0
            self.c1.configure(state=tk.NORMAL)
            self.c2.configure(state=tk.NORMAL)
            self.c3.configure(state=tk.NORMAL)
            self.c1var.set(0)
            self.c2var.set(0)
            self.c3var.set(0)
        elif self.lancer < 3:
            self.lancer +=1
            self.DrawDice(liste)
            self.c1var.set(0)
            self.c2var.set(0)
            self.c3var.set(0)
        if self.lancer == 3:
            self.valider.configure(state=tk.DISABLED)
            self.lab2["text"] = "Perdu !"
            self.c1.configure(state=tk.DISABLED)
            self.c2.configure(state=tk.DISABLED)
            self.c3.configure(state=tk.DISABLED)
            self.restart_b.grid(row=2, column=1, pady=10)
            self.restart_b.configure(state=tk.NORMAL)
    def restart(self):
        self.lancer = -1
        self.de1.delete("all")
        self.de2.delete("all")
        self.de3.delete("all")
        self.valider.configure(state=tk.NORMAL)
        self.restart_b.grid_forget()
        self.lab2["text"] = ""
        
        
        

def main():
    root = tk.Tk()
    root.title("Jeu 4, 2, 1")
    app = Jeu_4_2_1(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
