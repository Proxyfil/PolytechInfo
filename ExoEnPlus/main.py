import tkinter


def main():
    #Créer un fenetre
    window = tkinter.Tk()
    window.title("Nim")
    window.geometry("720x480")
    window.minsize(480, 360)
    window.config(background='#41B77F')

    #Créer un titre
    label_title = tkinter.Label(window, text="Jeu de Nim", font=("Courrier", 40), bg='#41B77F', fg='white')
    label_title.pack()

    window.mainloop()

main()
