from turtle import *
import random
speed("fastest")

class Toile():
    def __init__(self, posMouches=[]):
        self.posMouches = posMouches
        self.dessineToile()

    @staticmethod
    def dessineToile():
        for i in range(8):
            goto(0,0)
            forward(200)
            left(45)

        up()
        goto(0,0)
        down()

        start = 10
        for i in range(17):
            up()
            goto(5*i,-12*i)
            down()
            for j in range(8):
                left(45)
                forward(10*i)



    @staticmethod
    def mouche(angle, coord):
        setheading(angle)
        up()
        goto(coord)
        down()
        begin_fill()
        circle(10,110)
        left(60)
        circle(10,110)
        up()
        goto(coord)
        down()
        left(25)
        circle(10,110)
        left(60)
        circle(10,110)
        right(115)
        circle(4)
        end_fill()

    def ajouteMouche(self):
        pos = (random.randint(-40,40)*5,random.randint(-40,40)*5)
        while(pos in self.posMouches) or pos[0]+pos[1] > 200 or pos[0]+pos[1] < -200 or pos[0]-pos[1] > 200 or pos[0]-pos[1] < -200:
            pos = (random.randint(-40,40)*5,random.randint(-40,40)*5)

        self.posMouches.append(pos)
        self.mouche(random.randint(0,360),pos)

    def afficheNbMouches(self):
        print(len(self.posMouches))

toile = Toile()
for i in range(45):
    toile.ajouteMouche()

mainloop()