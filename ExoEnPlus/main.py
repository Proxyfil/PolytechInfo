import tkinter
import jeu

jeuNim = jeu.jeu(1)

board = [[0,0,0],[0,0,0],[0,0,0]]


def leftClick(event):
    global jeuNim
    validate = jeuNim.jouer_case((event.x//100, event.y//100), 1)
    if(not validate):
        return
    if(str(event.widget) != '.!canvas'):
        return
    global board
    global canvas
    if(event.x < 100 and event.y < 100 and event.x > 0 and event.y > 0):
        if(board[0][0] == 0):
            canvas.create_rectangle(0, 0, 100, 100, fill="red")
            board[0][0] = 1
    elif(event.x < 200 and event.y < 100 and event.x > 100 and event.y > 0):
        if(board[0][1] == 0):
            canvas.create_rectangle(100, 0, 200, 100, fill="red")
            board[0][1] = 1
    elif(event.x < 300 and event.y < 100 and event.x > 200 and event.y > 0):
        if(board[0][2] == 0):
            canvas.create_rectangle(200, 0, 300, 100, fill="red")
            board[0][2] = 1
    elif(event.x < 100 and event.y < 200 and event.x > 0 and event.y > 100):
        if(board[1][0] == 0):
            canvas.create_rectangle(0, 100, 100, 200, fill="red")
            board[1][0] = 1
    elif(event.x < 200 and event.y < 200 and event.x > 100 and event.y > 100):
        if(board[1][1] == 0):
            canvas.create_rectangle(100, 100, 200, 200, fill="red")
            board[1][1] = 1
    elif(event.x < 300 and event.y < 200 and event.x > 200 and event.y > 100):
        if(board[1][2] == 0):
            canvas.create_rectangle(200, 100, 300, 200, fill="red")
            board[1][2] = 1
    elif(event.x < 100 and event.y < 300 and event.x > 0 and event.y > 200):
        if(board[2][0] == 0):
            canvas.create_rectangle(0, 200, 100, 300, fill="red")
            board[2][0] = 1
    elif(event.x < 200 and event.y < 300 and event.x > 100 and event.y > 200):
        if(board[2][1] == 0):
            canvas.create_rectangle(100, 200, 200, 300, fill="red")
            board[2][1] = 1
    elif(event.x < 300 and event.y < 300 and event.x > 200 and event.y > 200):
        if(board[2][2] == 0):
            canvas.create_rectangle(200, 200, 300, 300, fill="red")
            board[2][2] = 1

    if(type(validate) == str and "gagné" in validate):
        print("gagné")

def rightClick(event):
    global jeuNim
    validate = jeuNim.jouer_case((event.x//100, event.y//100), 2)
    if(not validate):
        return
    if(str(event.widget) != '.!canvas'):
        return
    global board
    global canvas
    if(event.x < 100 and event.y < 100 and event.x > 0 and event.y > 0):
        if(board[0][0] == 0):
            canvas.create_rectangle(0, 0, 100, 100, fill="yellow")
            board[0][0] = 1
    elif(event.x < 200 and event.y < 100 and event.x > 100 and event.y > 0):
        if(board[0][1] == 0):
            canvas.create_rectangle(100, 0, 200, 100, fill="yellow")
            board[0][1] = 1
    elif(event.x < 300 and event.y < 100 and event.x > 200 and event.y > 0):
        if(board[0][2] == 0):
            canvas.create_rectangle(200, 0, 300, 100, fill="yellow")
            board[0][2] = 1
    elif(event.x < 100 and event.y < 200 and event.x > 0 and event.y > 100):
        if(board[1][0] == 0):
            canvas.create_rectangle(0, 100, 100, 200, fill="yellow")
            board[1][0] = 1
    elif(event.x < 200 and event.y < 200 and event.x > 100 and event.y > 100):
        if(board[1][1] == 0):
            canvas.create_rectangle(100, 100, 200, 200, fill="yellow")
            board[1][1] = 1
    elif(event.x < 300 and event.y < 200 and event.x > 200 and event.y > 100):
        if(board[1][2] == 0):
            canvas.create_rectangle(200, 100, 300, 200, fill="yellow")
            board[1][2] = 1
    elif(event.x < 100 and event.y < 300 and event.x > 0 and event.y > 200):
        if(board[2][0] == 0):
            canvas.create_rectangle(0, 200, 100, 300, fill="yellow")
            board[2][0] = 1
    elif(event.x < 200 and event.y < 300 and event.x > 100 and event.y > 200):
        if(board[2][1] == 0):
            canvas.create_rectangle(100, 200, 200, 300, fill="yellow")
            board[2][1] = 1
    elif(event.x < 300 and event.y < 300 and event.x > 200 and event.y > 200):
        if(board[2][2] == 0):
            canvas.create_rectangle(200, 200, 300, 300, fill="yellow")
            board[2][2] = 1

    if(type(validate) == str and "gagné" in validate):
        print("gagné")

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

    global canvas
    canvas = tkinter.Canvas(width=300, height=300, bg='#41B77F', bd=0, highlightthickness=0)
    canvas.create_line(0, 100, 500, 100)
    canvas.create_line(0, 200, 500, 200)
    canvas.create_line(100, 0, 100, 500)
    canvas.create_line(200, 0, 200, 500)
    canvas.pack()

    #Créer un bouton
    button_start = tkinter.Button(window, text="Robot (jaune)", font=("Courrier", 25), bg='#41B77F', fg='white')
    button_start.pack()

    window.bind("<Button-1>", leftClick)
    window.bind("<Button-3>", rightClick)
    window.mainloop()

main()
