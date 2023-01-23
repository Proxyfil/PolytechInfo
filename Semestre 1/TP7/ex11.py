import turtle
turtle.color("red")
turtle.speed(10000)

#Courbe du dragon
# on veut un programme qui produise une courbe du dragon de longueur l avec n itérations et c pour la couleur
def dragon(l,n,c):
    turtle.color(c)
    if n == 0:
        turtle.forward(l)
    else:
        turtle.left(90)
        dragon(l/2,n-1,c)
        turtle.right(90)
        dragon(l/2,n-1,c)
        turtle.right(90)
        dragon(l/2,n-1,c)
        turtle.left(90)
        dragon(l/2,n-1,c)

dragon(400,5,"red")
input()
