import turtle
import random
turtle.speed("fastest")

def rectangle(x, y, h, v):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(v)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(v)
    turtle.left(90)

def cercle(self, x, y, r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)

class Wagon():
    def __init__(self, x, y, passagers):
        self.x = x
        self.y = y
        self.passagers = passagers

        self.rectangle(x, y, 80, 45)
        turtle.penup()
        self.rectangle(x+5,y+10,20,30)
        self.rectangle(x+30,y+10,20,30)
        self.rectangle(x+55,y+10,20,30)

        self.cercle(x+15, y-20, 10)
        self.cercle(x+65, y-20, 10)

    @staticmethod
    def rectangle(x, y, h, v):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(v)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(v)
        turtle.left(90)

    @staticmethod
    def cercle(x, y, r):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(r)

    @staticmethod
    def cerclePlein(x, y, r, color="black"):
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    def NbPassagers(self):
        return len([i for i in self.passagers if i == 1])

class Passager():
    train = [Wagon(-200,0,[0,0,0]),Wagon(-100,0,[0,0,0]),Wagon(0,0,[0,0,0]),Wagon(100,0,[0,0,0])]
    def __init__(self, numWagon=0, numFenetre=0):
        self.numWagon = numWagon
        self.numFenetre = numFenetre
        while self.train[numWagon].passagers[numFenetre] == 1:
            numWagon = random.randint(0,3)
            numFenetre = random.randint(0,2)
        self.train[numWagon].passagers[numFenetre] = 1
        self.train[numWagon].cerclePlein(self.train[numWagon].x+15+self.numFenetre*25, self.train[numWagon].y+10, 7)


    def monte(self, wagon):
        wagon.cerclePlein(self.wagon.x+15+self.place*25, self.wagon.y+10, 7)

    def delete(self, wagon):
        wagon.cerclePein(self.wagon.x+15+self.place*25, self.wagon.y+10, 7, "white")
        self.delete()

Passager()
Passager()
Passager()
Passager()
turtle.mainloop()

input()