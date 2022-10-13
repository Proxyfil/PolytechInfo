import turtle
turtle.speed(5000)

def joue():
    mot = initMot()
    print("\n"*50)
    guess = "*"*len(mot)

    count = 0
    while count < 10:
        print(guess)
        guess, status = guessLetter(mot,guess,input("Entrez une lettre: "))

        if(guess == mot):
            print("Gagné")
            return True
        else:
            if(status):
                print("Bonne lettre")
            else:
                print("Mauvaise lettre")
                count += 1
                dessinerPendu(count)
    print("perdu :", mot)
    input()


def initMot():
    return input("Entrez un mot : ")

def guessLetter(mot,guess,char):
    found = False
    guess = list(guess)
    for i in range(len(mot)):
        if(mot[i] == char):
            guess[i] = char
            found = True
    return ("".join(guess), found)

def dessinerPendu(count):
    if(count == 1):
        turtle.forward(100)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
    elif(count == 2):
        turtle.forward(200)
        turtle.right(90)
    elif(count == 3):
        turtle.forward(100)
        turtle.right(90)
    elif(count == 4):
        turtle.forward(25)
        turtle.right(90)
    elif(count == 5):
        turtle.circle(25)
    elif(count == 6):
        turtle.penup()
        turtle.left(90)
        turtle.forward(50)
        turtle.pendown()
        turtle.forward(100)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(90)
    elif(count == 7):
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
    elif(count == 8):
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(45)
    elif(count == 9):
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(90)
    elif(count == 10):
        turtle.forward(50)

joue()