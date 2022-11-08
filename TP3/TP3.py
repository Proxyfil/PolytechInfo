import math

#Exercice 1

def saisie():
    a = input("Entrez un nombre entier supérieur à 0 : ")
    while not a.isdigit() or int(a) <= 0:
        a = input("Entrez un nombre entier supérieur à 0 : ")
    return int(a)

def afficherTerme(n):
    a = 0
    for i in range(1,n+1):
        a += 1/(i**2)
        print(f"Terme {i} : {a} et pi**2/6 = {math.pi**2/6}")

#Exercice 2

import random

def saisieSomme():
    a = input("Entrez un nombre entier supérieur à 1 et inférieur à 13 : ")
    while not a.isdigit() or int(a) <= 12 or int(a) >= 2:
        a = input("Entrez un nombre entier supérieur à 1 et inférieur à 13 : ")
    return int(a)

def sommeDeuxDés():
    a = random.randint(1,6)
    b = random.randint(1,6)
    print(f"dé 1 : {a}")
    print(f"dé 2 : {b}")
    print(f"somme : {a+b}")
    return a+b

def jouer():
    a = saisieSomme()
    b = sommeDeuxDés()
    if a == b:
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")

#Exercice 3

def factoriel(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

def binome(n,p):
    return factoriel(n)/(factoriel(p)*factoriel(n-p))

def afficher_developpement_identité_remarquable(n):
    for i in range(n+1):
        if i == 0:
            print(f"1.0a^{n} + ", end="")
        if i == n:
            print(f"1.0b^{n}")
        else:
            print(f"{binome(n,i)}a^{i}b^{n-i} + ",end="")
    return None

def trianglepascale(n):
    for i in range(n+1):
        for j in range(i+1):
            print(f"{int(binome(i,j))}",end=" ")
        print("")
    return None

#Exercice 4

import turtle

def polygone(taille,nbCotes):
    for i in range(nbCotes):
        turtle.forward(taille)
        turtle.left(360/nbCotes)

def rosace(taille,nbCotes,nbFois):
    turtle.speed(100)
    for i in range(nbFois):
        polygone(taille,nbCotes)
        turtle.left(10)
    a = input("Appuyez sur une touche pour quitter")

def rosace_coloree(taille,nbCotes,nbFois):
    turtle.speed(100)
    """dégradé rouge vers vert"""
    for i in range(int(nbFois/3)):
        turtle.color(1-i/(nbFois/3),0,i/(nbFois/3))
        polygone(taille,nbCotes)
        turtle.left(360/nbFois)
    """dégradé vert vers bleu"""
    for i in range(int(nbFois/3)):
        turtle.color(0,i/(nbFois/3),1-i/(nbFois/3))
        polygone(taille,nbCotes)
        turtle.left(360/nbFois)
    """dégradé bleu vers rouge"""
    for i in range(int(nbFois/3)+1):
        turtle.color(i/(nbFois/3),1-i/(nbFois/3),0)
        polygone(taille,nbCotes)
        turtle.left(360/nbFois)
    a = input("Appuyez sur une touche pour quitter")

#Exercice 5

def afficher():
    for i in range(100,1000):
        if i == int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3:
            print(i)
    return None

def afficher2(n):
    for i in range(100,n+1):
        for v in range(len(str(i))):
            if v == 0:
                a = int(str(i)[v])**len(str(i))
            else:
                a += int(str(i)[v])**len(str(i))
        if i == a:
            print(i)
    return None

#Exercice 6

def afficherTerme(n, x):
    u0 = x
    v0 = 1
    for i in range(1,n+1):
        u = (u0+v0)/2
        v = (2*u0*v0)/(u0+v0)
        u0 = u
        v0 = v
        print(f"Terme {i} : u = {u} et v = {v}")
    print(f"sqrt({x}) : {math.sqrt(x)}")
    return None

#Exercice 7

def jeu1():
    a = input("Entrez un entier : ")
    b = random.randint(1,2)
    if a.isdigit():
        if b%2 == 0:
            if int(a)%2 == 0:
                print("Gagné on attendait un nombre pair")
            else:
                print("Perdu on attendait un nombre pair")
        else:
            if int(a)%2 == 0:
                print("Perdu on attendait un nombre impair")
            else:
                print("Gagné on attendait un nombre impair")
    else:
        print("Perdu on attendait un entier")
    return None

def jeu2():
    a = input("Entrez soit +, soit - ou = : ")
    b = random.choice([":-)",":-I",":-("])
    dicta = {":-)" : "+", ":-I" : "=", ":-(" : "-"}
    if a == dicta[b]:
        print(f"Gagné")
    else:
        print("Perdu")
    return None

def jeu():
    a = input("Entrez soit 1, soit 2 : ")
    while a == "1":
        jeu1()
        a = input("Entrez soit 1, soit 2 : ")
    while a == "2":
        jeu2()
        a = input("Entrez soit 1, soit 2 : ")
    return None

#Exercice 8

#pseudo-code
"""
fonction addition_2_binaires(a: binaire,b: binaire) -> binaire
var c: binaire
var retenue: entier
debut
    c = ""
    retenue = 0
    pour i allant de 0 à len(a)-1
        si a[i] == 0 et b[i] == 0
            c += str(retenue)
            retenue = 0
        sinon si a[i] == 1 et b[i] == 1
            c += str(retenue)
            retenue = 1
        sinon si a[i] == 1 et b[i] == 0 ou a[i] == 0 et b[i] == 1
            si retenue == 0
                c += "1"
            sinon
                c += "0"
        sinon
            si retenue == 0
                c += "0"
                retenue = 1
            sinon
                c += "1"
                retenue = 1
    fin pour
    si retenue == 1
        c += "1"
    sinon
        c += "0"
    fin si
    retourner c
fin
"""

#python

def addition_2_binaires(a,b):
    c = int(a,2) + int(b,2)
    print(bin(c)[2:])

#Exercice 9

#pseudo-code

"""
fonction multiplication_2_binaires(a: binaire,b: binaire) -> binaire
var c: binaire
debut
    c = 0
    pour i allant de 0 à len(a)-1
        si a[i] == 1
            c += b * 10**(len(a)-1-i)
        fin si
    fin pour
    retourner c
fin
"""

#python

def multiplication_2_binaires(a,b):
    c = int(a,2) * int(b,2)
    print(bin(c)[2:])

#Exercice 10

from math import log, log10

def test_pH_solution_aqueuse(concentration_molaire_ions_hydronium) -> float :
    """Renvoie le pH d'une solution aqueuse en fonction de la concentration molaire des ions hydronium"""
    pH = format(-log10(concentration_molaire_ions_hydronium),".2f")
    if pH <= 6.5:
        print(f"La solution est acide car son pH est de {pH}")
    if pH < 7.5 and pH > 6.5:
        print(f"La solution est neutre car son pH est de {pH}")
    elif pH >= 7.5:
        print(f"La solution est basique car son pH est de {pH}")

#Exercice 11

"""
Log10 permet de connaitre le nombre chiffre d'un nombre car log10(10**n) = n
"""

def nb_chiffre_avec_log10(n):
    return int(format(int(log10(n))+1,".0f"))

def somme_chiffre_avec_log(n):
    result = 0
    for i in range(nb_chiffre_avec_log10(n)):
        result += int(str(n)[i])
    return result

#Exercice 12

def suite(u0,r,n):
    for i in range(n):
        u0 += r
    return u0

def suite(u0,r,n):
    for i in range(n):
        u0 *= r
    return u0

#Exercice 13

import turtle

def motif(r):
    turtle.speed(100)
    turtle.fillcolor("blue")
    for i in range(4):
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()
        turtle.circle(r,140)
        turtle.right(180)
        r = r*2
    r = r/2
    r = r/2
    for i in range(4):
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()
        turtle.circle(r,-140)
        turtle.left(180)
        r = r/2

def repetition(n):
    turtle.speed(100)
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,0)
    turtle.circle(5,180/n)
    turtle.pendown()
    for i in range(n):
        motif(5)
        turtle.penup()
        turtle.goto(0,0)
    a = input("Appuyez sur une touche pour quitter")

repetition(10)