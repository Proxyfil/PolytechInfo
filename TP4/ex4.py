from turtle import *
speed(100000)

def polygone(taille,nb_cotes):
    for i in range(nb_cotes):
        forward(taille)
        left(360/nb_cotes)

def rosace(taille,nb_cotes):
    for i in range(36):
        polygone(taille,nb_cotes)
        left(10)

def rosaceColorée(taille,nb_cotes):
    nbr = 90
    couleur = [1,0,0]
    color(1,0,0)
    for i in range(int(nbr/3)):
        polygone(taille,nb_cotes)
        left(360/90)
        couleur[0] -= 1/(nbr/3)
        couleur[1] += 1/(nbr/3)
        color(couleur[0],couleur[1],couleur[2])
    for i in range(int(nbr/3)):
        polygone(taille,nb_cotes)
        left(360/90)
        couleur[1] -= 1/(nbr/3)
        couleur[2] += 1/(nbr/3)
        color(couleur[0],couleur[1],couleur[2])
    for i in range(int(nbr/3)):
        polygone(taille,nb_cotes)
        left(360/90)
        couleur[2] -= 1/(nbr/3)
        couleur[0] += 1/(nbr/3)
        color(couleur[0],couleur[1],couleur[2])
rosaceColorée(100,6)
input()