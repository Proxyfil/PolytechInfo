import tkinter as tk
import random

class JeuChoix_radiobutton(object):
    def __init__(self, master):
        self.master = master
        self.master = tk.Frame(self.master)
        self.master.pack(padx=20, pady=10)

        self.lab1 = tk.Label(self.master, text="Choissisez:")
        self.lab1.grid(row=1, column=0, rowspan=2, padx= 10)

        self.v = tk.StringVar()
        self.v.set(" ")
        
        self.r1 = tk.Radiobutton(self.master, text="Saint-Honoré", variable=self.v, value="Saint-Honoré", background="lightblue", width=20, anchor="w")
        self.r2 = tk.Radiobutton(self.master, text="Opéra", variable=self.v, value="Opéra", background="lightblue", width=20, anchor="w")
        self.r3 = tk.Radiobutton(self.master, text="Mille-feuilles", variable=self.v, value="Mille-feuilles", background="lightblue", width=20, anchor="w")
        self.r4 = tk.Radiobutton(self.master, text="Religieuse au café", variable=self.v, value="Religieuse au café", background="lightblue", width=20, anchor="w")
        
        self.r1.grid(row=0, column=1, sticky="w")
        self.r2.grid(row=1, column=1, sticky="w")
        self.r3.grid(row=2, column=1, sticky="w")
        self.r4.grid(row=3, column=1, sticky="w")

        self.valider = tk.Button(self.master, text="alors?", background="green",width=8, command=self.random)
        self.valider.grid(row=4, column=0, columnspan=2, pady=10)

        self.lab2 = tk.Label(self.master, text="", background="orange", font=("Arial24",10), width=40)
        self.lab2.grid(row=5, column=0, columnspan=2, pady=4)
        
    def random(self):
        choice_dessert = random.choice(["Saint-Honoré", "Opéra", "Mille-feuilles", "Religieuse au café"])
        if self.v.get() == choice_dessert:
            self.lab2.configure(text=f"Excellent choix, l'ordi adore {choice_dessert}!")
        else:
            self.lab2.configure(text=f"Tssss… pas bon… l'ordi préfère {choice_dessert}")

class JeuChoix_listbox(object):
    def __init__(self, master):
        self.master = master
        self.master = tk.Frame(self.master)
        self.master.pack(padx=20, pady=10)

        self.lab1 = tk.Label(self.master, text="Choissisez:")
        self.lab1.grid(row=0, column=0, padx= 10)

        self.liste_dessert = tk.Listbox(self.master, selectmode=tk.SINGLE, height=4, width=20)
        self.liste_dessert.insert(1, "Saint-Honoré")
        self.liste_dessert.insert(2, "Opéra")
        self.liste_dessert.insert(3, "Mille-feuilles")
        self.liste_dessert.insert(4, "Religieuse au café")
        self.liste_dessert.grid(row=0, column=1, padx= 20)

        self.valider = tk.Button(self.master, text="alors?", background="green",width=8, command=self.random)
        self.valider.grid(row=1, column=0, columnspan=2, pady=10)

        self.lab2 = tk.Label(self.master, text="", background="orange", font=("Arial24",10), width=40)
        self.lab2.grid(row=2, column=0, columnspan=2, pady=4)

    def random(self):
        choice_dessert = random.choice(["Saint-Honoré", "Opéra", "Mille-feuilles", "Religieuse au café"])
        try:
            if self.liste_dessert.get(self.liste_dessert.curselection()) == choice_dessert:
                self.lab2.configure(text=f"Excellent choix, l'ordi adore {choice_dessert}!")
            else:
                self.lab2.configure(text=f"Tssss… pas bon… l'ordi préfère {choice_dessert}")
        except:
            self.lab2.configure(text="Vous devez choisir un dessert!")

def main():
    root = tk.Tk()
    app = JeuChoix_radiobutton(root)
    root.mainloop()
    root2 = tk.Tk()
    app = JeuChoix_listbox(root2)
    root2.mainloop()
    
if __name__ == '__main__':
    main()