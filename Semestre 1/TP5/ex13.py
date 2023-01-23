import turtle
turtle.speed(1000)
def uneEtoile(nbr,size,color):
    turtle.color(color)
    for i in range(nbr):
        turtle.forward(size)
        turtle.left(180)
        turtle.forward(size)
        turtle.left(360/(nbr*2))

def etoileComplete(lnbr,lsize,lcolor):
    for i in range(len(lnbr)):
        uneEtoile(lnbr[i],lsize[i],lcolor[i])
    turtle.hideturtle()
    input()

def etoileComplete2(nsc):
    for i in range(len(nsc)):
        uneEtoile(nsc[i][0],nsc[i][1],nsc[i][2])
    turtle.hideturtle()
    input()
    

etoileComplete2([(6,100,"green"),(11,80,"purple"),(13,90,"red"),(21,50,"orange")])