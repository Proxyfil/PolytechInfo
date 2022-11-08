#pseudo-code

"""
fonction saisie(): reel
var x: reel
début
    afficher "Entrer un réel positif : "
    lire x
    tant que x<=0 faire
        afficher "Entrer un réel positif : "
        lire x
    fin tant que   
    retourner x
fin

fonction perimetre(a: reel): reel
var
début
    retourner 2*pi*a
fin

fonction aire(a: reel): reel
début
    retourner pi*(a**2)
fin

fonction rayonpositif(a: reel): reel
var a: reel
début
    écrire("Saisir le rayon du cercle :")
    lire(a)
    tant que a < 0 faire
        écrire("Saisir le rayon du cercle :")
        lire(a)
    fin tant que

    retourner a
fin
"""

"""
fonction p_or_s(): charactère
var a: charactère
début
    écrire("Saisir p ou s")
    lire(a)
    tant que a différent de 'p' ou a différent de 's' faire
        écrire("Saisir p ou s :")
        lire(a)
    fin tant que

    retourner a
fin

fonction totale(): reel
var a: reel
    b: charactère
début
    a <- rayonpositif()
    b <- p_or_s()
    si b = 'p' faire 
        retourner perimetre(a)
    sinon faire
        retourner aire(a)
    fin si

fin

debut
totale()
fin
"""

#python

def saisie() -> int:
    """Renvoie un entier positif"""
    x = int(input("Entrer un entier : "))
    while x<=0:
        x = int(input("Entrer un entier : "))
    return x

def perimetre(a: int) -> float:
    """Renvoie le périmètre d'un cercle de rayon a"""
    return 2*math.pi*a

def aire(a: int) -> float:
    """Renvoie l'aire d'un cercle de rayon a"""
    return math.pi*(a**2)

def rayonpositif() -> int:
    """Renvoie un entier positif"""
    x = int(input("Saisir le rayon du cercle :"))
    while x < 0:
        x = int(input("Saisir le rayon du cercle :"))
    return x

def p_or_s() -> str:
    """Renvoie p ou s"""
    a = input("Saisir p ou s :")
    while a != "p" and a != "s":
        a = input("Saisir p ou s :")
    return a

def totale() -> float:
    """Renvoie le périmètre ou l'aire d'un cercle"""
    x = saisie()
    y = p_or_s()
    if y == "p":
        return perimetre(x)
    else:
        return aire(x)

#pseudo-code

"""
fonction surfaceouvolumecylindre(): reel
var a: reel
    b: reel
    c: charactère
début
    a <- saisie()
    b <- saisie()
    c <- p_or_s()
    si c égale à "p" faire
        retourner aire(a)
    sinon faire
        retourner volume(a,b)
    fin si
fin
"""

#python 

def volume(a: int,b: int) -> float:
    """Renvoie le volume d'un cylindre de rayon a et de hauteur b"""
    return math.pi*(a**2)*b

def surfaceouvolumecylindre() -> float:
    """Renvoie l'aire ou le volume d'un cylindre"""
    a = saisie()
    b = saisie()
    c = p_or_s()
    if c == "p":
        return aire(a)
    else:
        return volume(a,b)

#Exercice 1

def diviseur_impairs(n):
    """Renvoie la liste des diviseurs impairs de n"""
    diviseurs = []
    for i in range(1,n+1):
        if n % i == 0 and i % 2 == 1:
            diviseurs.append(i)
    return diviseurs

#Exercice 2

def sontPairs(x, y):
    """Renvoie True si x et y sont pairs, False sinon"""
    return x % 2 == 0 and y % 2 == 0

x = int(input("Entrer un entier"))
y = int(input("Entrer un autre entier"))

if sontPairs(x,y):
    print("Les deux nombres sont pairs")
else:
    print("Les deux nombres ne sont pas pairs")

def listePairsTrue(liste):
    """Renvoie True si tous les éléments de la liste sont pairs, False sinon"""
    for i in liste:
        if i % 2 == 1:
            return False
    return True

#Exercice 3

def f(x):
    if x>0:
        return 2*x
        return x+2

print(f(8))

"""
Seul le premier return est pris en compte, le second est ignoré, en effet, une fois que la fonction a trouvé un return, elle s'arrête.
"""
def f2(x):
    if x>0:
        return (2*x, x+2)

def f3(x):
    if x>0:
        return 2*x+6
    else:
        return 3*x+2

print(f3(1))
print(f3(-1))

"""
Cette fonction contient deux returns et est correcte car ils sont dans des branches différentes.
"""

#Exercice 4

def g(n):
    for i in range(1,n+1):
        print("rang ",i)

print(g(8))

"""
Si on remplace g(8) par print(g(8)), on obtient None car la fonction g ne renvoie rien.
"""

def volumetetraedre(a):
    return format((a**3)/(6*(2**(1/2))),".3f")

#Exercice 5

def saisie():
    x = float(input("enter x>0 : "))
    while x<=0:
        x = float(input("enter x>0 : "))
    return x

y = saisie()
print(y)

"""
Cette fonction demande à l'utilisateur de saisir un nombre positif, tant que ce n'est pas le cas, elle lui redemande de saisir un nombre positif.
"""
"""
Le return est important car il permet de renvoyer la valeur saisie par l'utilisateur.
"""

def saisiedivisible():
    x = int(input("enter x divisible par 3 et pas 5 : "))
    while x%3 != 0 or x%5 == 0:
        x = int(input("enter x divisible par 3 et pas 5 : "))
    return x

y = saisiedivisible()
print(y)

#Exercice 6

import math

def airedisque():
    x = saisie()
    return format(math.pi*(x**2),".3f")

#Exercice 7

def volumecylindre():
    x = saisie()
    y = saisie()
    return format(math.pi*(x**2)*y,".3f")

#Exercice 9

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def afficheTroisFactorielles():
    x = int(input("Entrer un entier : "))
    y = int(input("Entrer un entier : "))
    z = int(input("Entrer un entier : "))
    print(fact(x))
    print(fact(y))
    print(fact(z))
    return None

#Exercice 10

import turtle
