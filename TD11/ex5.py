import tkinter as tk

# fonction appelée quand on presse une touche
def clavier(event):
    global coords
    touche = event.keysym
    if touche == "Up":
        if coords[1]-10 > 0:
            coords = (coords[0], coords[1]-10)
        else:
            coords = (coords[0], 0)
    elif touche == "Down":
        if coords[1]+10 < 275:
            coords = (coords[0], coords[1]+10)
        else:   
            coords = (coords[0], 278)
    elif touche == "Right":
        if coords[0]+10 < 275:
            coords = (coords[0]+10, coords[1])
        else:
            coords = (278, coords[1])
    elif touche == "Left":
        if coords[0]-10 > 0:
            coords = (coords[0]-10, coords[1])
        else:
            coords = (0, coords[1])
    # changement de coordonnées pour le pion:
    canvas.coords(ov, coords[0], coords[1], coords[0]+25, coords[1]+25)
    
fenetre = tk.Tk()
fr = tk.Frame(fenetre)
fr.pack(padx=20, pady=10)
lab1 = tk.Label(fr, text="Cliquer dans la zone verte, puis utiliser les flèches:")
lab1.grid(row=0, column=0, padx=2, pady=2)
canvas = tk.Canvas(fr, width=300, height=300, bg="lightgreen")
coords = (0, 0)
# création du pion:
ov = canvas.create_oval(10,10,35,35,fill="blue")
# ajout du lien aux touches du clavier:
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.grid(row=1, column=0)
fenetre.mainloop()

"""
Ce programme permet de déplacer un pion avec les flèches du clavier.
"""