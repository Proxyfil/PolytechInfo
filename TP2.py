#Exercice 1:

import math
from re import U

def factoriel(n):
    resu = 1
    for i in range(1, n+1):
        resu *= i
    return resu

"""
Pour n = 0, la fonction factoriel(n) retourne 1
"""

def somme(n):
    resu = 0
    for i in range(0, n+1):
        resu += 1/factoriel(i)
    return resu

def estimation(n):
    return math.e - somme(n)

#Exercice 2:

def termesuite1(m,n):
    u = m
    print(u)
    for i in range(1, n+1):
        u = u**2 -5
        print(u)
    return u

"""
Pour termesuite1, m correspond à la valeur de départ de la suite, et n à la valeur de l'indice du terme de la suite que l'on veut calculer.
"""

"""
Pour termesuite1 où m = 5 et n = 2, la fonction termesuite1 calcul les termes de la suite de départ 5 jusqu'au terme d'indice 2.
"""

def sommeTermes(x,n):
    resu = x
    u = x
    for i in range(1, n+1):
        resu += 3/u
        u = 3/u
    return resu

#Exercice 3:

def fct(n):
    m = 2*n
    return(n,m)

"""
La fonction fct retourne un tuple de deux éléments, le premier étant n, et le second étant 2*n.
"""

def division_euclidienne(dividende, diviseur):
    quotient = 0
    reste = dividende
    while reste >= diviseur:
        reste -= diviseur
        quotient += 1
    return (quotient, reste)

#Exercice 4:

def estPremier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def criblage(n):
    """Crible d'Erathostene"""
    liste = list(range(1, n+1))
    liste[0] = 0
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if j % i == 0:
                try:
                    m = liste.index(j)
                    liste[m] = 0
                except ValueError:
                    pass
    return liste

def criblage2(n):
    """Crible d'Erathostene"""
    liste = list(range(2, n+1))
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if j % i == 0:
                try:
                    liste.remove(j)
                except ValueError:
                    pass
    return liste

def verifListe(n):
    liste = criblage2(n)
    for i in liste:
        if not estPremier(i):
            return False
    return True

#Exercice 5:

def euclide(a, b):
    if b == 0:
        return a
    else:
        return euclide(b, a % b)

def verif_pgcd(a, b, pgcd):
    if pgcd == euclide(a, b):
        return True
    else:
        return False

from random import choice
def t():
    maListe = [14,25,8,-2,9,3]
    for i in range(0,10):
        print(choice(maListe))

"""
La fonction choice permet de choisir un élément aléatoire dans une liste.
"""

def verification_automatique_use_criblage2(n):
    liste = criblage2(16)
    for i in range(0,n):
        a = choice(liste)
        b = choice(liste)
        pgcd = euclide(a,b)
        if not verif_pgcd(a,b,pgcd):
            return False
    return True

#Exercice 6:

def cube(x):
    return (x*3, x**3)

(a, b) = cube(2)

"""
La fonction cube retourne un tuple de deux éléments
"""

"""
La ligne 149 permet de décomposer le tuple retourné par la fonction cube en deux variables a et b.
"""

def bezout(a, b):
    if b == 0:
        return (1, 0)
    else:
        (u, v) = bezout(b, a % b)
        return (v, u - a // b * v)

from random import randint

def verification_bezout(n):
    for i in range(0,n):
        a = randint(1,100)
        b = randint(1,100)
        (u, v) = bezout(a, b)
        if not (a*u + b*v == euclide(a, b)):
            return False
    return True

#Exercice 7:

def verification_base(chaine_nb: str,base: int):
    for i in chaine_nb:
        if int(i) >= base:
            return False
    return True

"""
La fonction pop() sur une liste permet de retirer le dernier élément de la liste et de le retourner.
"""

def str_to_int(chaine_nb: str, base: int):
    if verification_base(chaine_nb, base):
        liste = list(chaine_nb)
        resu = 0
        for i in range(0, len(liste)):
            resu += int(liste.pop()) * base**i
        return resu
    else:
        return "Erreur"

def conversion(chaine_nb: str, base_depart: int, base_arrivee: int):
    if verification_base(chaine_nb, base_depart):
        return str(str_to_int(chaine_nb, base_depart), base_arrivee)
    else:
        return "Erreur"

"""
On utilisera les fonctions python hex, bin et oct pour effectuer une vérification aléatoire des 2 fonctions précédentes.
"""

def verification_aléatoire():
    for i in range(0, 100):
        a = randint(0, 10000)
        b = randint(2, 16)
        c = randint(2, 16)
        if conversion(str(a), b, c) != str(bin(a), b, c):
            return False
    for i in range(0, 100):
        a = randint(0, 10000)
        b = randint(2, 16)
        c = randint(2, 16)
        if conversion(str(a), b, c) != str(oct(a), b, c):
            return False
    return True

#Exercice 8:

def traduction_ch_to_code_cara(chaine: str):
    resu = ""
    for i in chaine:
        resu += str(ord(i)) + " "
    return resu

def correspondance_affiche_tableau_correspondace_encodage():
    print("lettre","encodage")
    for i in range(0, 256):
        print(i, chr(i))

#Exercice 9:

def reduction_chaine(chaine: str):
    resu = ""
    for i in chaine:
        if i.isalpha():
            resu += i.lower()
    return resu

def verification_reduction_chaine():
    for i in range(0, 100):
        a = randint(0, 10000)
        if reduction_chaine(str(a)) != str(a):
            return False
    return True

def ceasar(chaine: str, decalage: int):
    resu = ""
    for i in chaine:
        resu += chr(ord(i) + decalage)
    return resu

#Exercice 10:

def affiche_triangle(n):
    triangle = []
    for i in range(n-2, n+1):
        triangle.append(" "*(n-i) + "X"*(2*i-1))
    return triangle

def affiche_sapin(n):
    sapin = []
    for i in range(0, n):
        sapin.append(affiche_triangle(3+i))
        for i in range(0,len(sapin[:-1])):
            for j in range(0,len(sapin[i])):
                sapin[i][j] = " "*(1) + sapin[i][j]
    for i in sapin:
        for j in i:
            print(j)
    if n 
    for i in range(1, n+1):
        print(" "*(int(n)-1) + "I"*(n))

affiche_sapin(5)