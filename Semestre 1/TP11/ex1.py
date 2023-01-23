import tkinter as tk
from random import randint

class Essai1(object):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)
        
        self.var1 = tk.StringVar()
        self.lab1 = tk.Label(self.frame, textvariable=self.var1)
        self.var1.set("I'm here and I'm")
        self.lab1.grid(row=0, column=0)
        
        self.var2 = tk.StringVar()
        self.lab2 = tk.Label(self.frame, textvariable=self.var2)
        self.lab2.grid(row=0, column=1)
        
        self.button1 = tk.Button(self.frame, text="Try me", width=8, background="green",foreground="white", command=self.mafct)
        self.button1.grid(row=1, column=1, pady=5)

    def mafct(self):
        if randint(0,1) == 0:
            self.var2.set("Happy :-)")
        else:
            self.var2.set("Unhappy :-(")
def main():
    root = tk.Tk()
    app = Essai1(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    
"""
Ce programme permet de tirer au hasard Happy :-) ou Unhappy :-( avec le bouton Try me dans une fenêtre Tkinter.

"""