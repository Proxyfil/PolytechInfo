#Exercice 1:

"""
on appel (v, s) des couples de variables
"""

"""
la ligne (v, s) = cube(c) est une affectation de variables (v, s) à la valeur de retour de la fonction cube(c)
"""

"""
lorsque l'utilisateur entre la valeur 2, la fonction cube(c) retourne la valeur 8, qui est affectée à la variable v et la valeur 24à à la variable s
"""

"""
si on execute print(cube(c)) on obtiendrai (v, s)
"""

"""
la fonction affiche n affiche pour chaque n les valeurs de retour de la fonction cube(n) sous la forme:
cube de côté n: volume v, surface s
"""

"""
si l'utilisateur entre la valeur 3, la fonction affiche(3) affichera:
cube de côté 1: volume 1, surface 6
cube de côté 2: volume 8, surface 24
cube de côté 3: volume 27, surface 54
"""

import math

def sphère(r):
    v = 4/3 * math.pi * r**3
    s = 4 * math.pi * r**2
    return (v, s)

def affiche(n):
    for i in range(1, n+1):
        (v, s) = sphère(i)
        print("sphère de rayon", i, ": volume", v, ", surface", s)

r = int(input("Entrez un rayon : "))
affiche(r)

#r = int(input("rayon de la sphère: "))
#affiche(r)

#Exercice 2:

"""
numeros correspond à une liste
"""

"""
len(numeros) correspond à la longueur de la liste numeros
"""

"""
numeros[1] correspond à 318
"""

"""
les valeurs successives de x pour for x in numeros:
543
318
68
54
597
"""

"""
il existe deux types de boucles for, for x in numeros: et for x in range(0, len(numeros)):
la première boucle parcours la liste numeros, la seconde parcours les indices de la liste numeros
"""

"""
pour rallonger la liste numeros, on peut utiliser la fonction append(745) ou la fonction extend([745])
"""

#Exercice 3:

"""
la fonction reverse() inverse l'ordre des éléments d'une liste
"""

"""
la fonction pop() supprime le dernier élément d'une liste et le retourne
"""

"""
+= est une abréviation de = +, elle permet d'ajouter une valeur à une variable
"""

"""
la fonction extend() permet d'ajouter une liste à une liste
"""

"""
la fonction set() permet de créer un ensemble à partir d'une listea
"""

"""
la différence entre append, + et extend est que append ajoute un élément à la fin d'une liste, + ajoute une liste à la fin d'une liste et extend ajoute une liste à la fin d'une liste
"""

#Exercice 4:

"""
maVar est un tuple
"""

"""
le 'for j in maVar:' parcours les éléments du tuple maVar
"""

"""
la fonction append() sur un tuple ne fonctionne pas
"""

#Exercice 5:

"""
la fonction remove() supprime un élément d'une liste
"""

"""
la fonction remove() ne fonctionne pas sur un tuple
"""

#Exercice 6:

"""
la fonction choice() permet de choisir un élément aléatoire dans une liste
"""

"""
la fonction choice() fonctionne sur un tuple
"""

"""
la fonction choice() fonctionne sur une chaine de caractères
"""

"""
la fonction choice() fonctionne sur une liste de chaine de caractères
"""

#Exercice 7:

import random

def saisie():
    n = input("Entrez un entier compris entre 0 et 9 inclus : ")
    while not n.isdigit() or int(n) < 0 or int(n) > 9:
        n = input("Entrez un entier compris entre 0 et 9 inclus : ")
    return int(n)

def joue():
    n = saisie()
    liste = [random.randint(0, 9) for i in range(5)]
    if n in liste:
        print(f"{n} est dans {liste} : vous avez gagné :-)")
    else:
        print(f"{n} n'est pas dans {liste} : vous avez perdu :-(")
    return None

#Exercice 8:

def afficheMaListe(liste):
    choix = input("taper + pour ordre croissant, - pour ordre décroissant : ")
    if choix == "+":
        for x in sorted(liste):
            print(x)
    elif choix == "-":
        for x in sorted(liste, reverse=True):
            print(x)

liste = [54,21,-9,63]
afficheMaListe(liste)

#Exercice 9:

carres = [nbr**2 for nbr in range(101)]
print(carres)

def somme_puissance(n,p):
    somme = 0
    for i in range(1, n+1):
        somme += i**p
    return somme

#Exercice 11:

import turtle

def trapeze(l1, l2, l3, couleur):
    turtle.speed(100)
    turtle.color(couleur)
    turtle.begin_fill()
    turtle.forward(l1)
    turtle.right(120)
    turtle.forward(l2)
    turtle.right(60)
    turtle.forward(l3)
    turtle.right(60)
    turtle.forward(l2)
    turtle.right(120)
    turtle.end_fill()
    return None

#trapeze(60,20,40,"pink")

def triangle(cote, liste_couleurs=["orange","purple","red"]):
    turtle.left(240)
    for i in range(3):
        cote2 = ((cote/3)*(3-i))
        turtle.color(liste_couleurs[i])
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(cote2)
            turtle.left(120)
        turtle.end_fill()
    return None

#triangle(100,["blue","green","yellow"])

#Fin du TD