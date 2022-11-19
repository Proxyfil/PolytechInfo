import tkinter as tk
import random

def est_pair(n):
    return n % 2 == 0

def game():
    random_color = random.choice(["red", "black"])
    print(random_color)
    random_number = random.randint(1, 10)
    if est_pair(random_number) and random_color == "red" and var1.get() == 1 and var2.get() == 1:
        lab2.configure(text=f"{random_number} gagner!", foreground=f"{random_color}")
    elif est_pair(random_number) and random_color == "black" and var1.get() == 1 and var2.get() == 0:
        lab2.configure(text=f"{random_number} gagner!", foreground=f"{random_color}")
    elif not est_pair(random_number) and random_color == "red" and var2.get() == 1 and var1.get() == 0:
        lab2.configure(text=f"{random_number} gagner!", foreground=f"{random_color}")
    elif not est_pair(random_number) and random_color == "black" and var2.get() == 0 and var1.get() == 0:
        lab2.configure(text=f"{random_number} gagner!", foreground=f"{random_color}")
    else:
        lab2.configure(text=f"{random_number} perdu!", foreground=random_color)
    fen.update()

fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)
lab1 = tk.Label(maFrame, text="Un chiffre noir ou rouge va sortir...\nCliquer ce que vous pensez obtenir")
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(maFrame, text='chiffre pair',variable=var1, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(maFrame, text='rouge',variable=var2, onvalue=1, offvalue=0)
lab2 = tk.Label(maFrame, text="",background="lightblue",font=("Arial24",10), width=8)
c1.grid(row=1, column=0)
c2.grid(row=1, column=1)
lab1.grid(row=0, column=0, columnspan=2)
lab2.grid(row=2, column=0, columnspan=2, pady=4)
jouer = tk.Button(maFrame, text='Jouer', command=game, background='lightgreen', width=7, height=1)
jouer.grid(row=4, column=0, columnspan=2)

fen.mainloop()