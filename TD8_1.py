#Exercice 1:

def affiche(n):
    for i in range(n):
        print("My life is so cool ...")

#Affiche(8) (1)
#affiche() (2)
#affiche(3.5) (3)
#On enleve les ':' apres le for (4)
# affiche(8) (5)

"""
(1) : L'exception NameError est levée car la fonction Affiche n'est pas définie.
(2) : L'exception TypeError est levée car la fonction affiche attend un argument.
(3) : L'exception TypeError est levée car la fonction affiche attend un entier. En effet 3.5 est un flottant et pour la boucle for, il faut un entier.
(4) : L'exception SyntaxError est levée car il manque les : après le for.
(5) : L'exception IndentationError est levée car il y a un espace avant l'appel de la fonction affiche.
"""

#Exercice 2:

def somme_carre(n):
    s=0
    for i in range(n):
        s=s+i*i
    print(s)
    return None

def saisit():
    while True:
        n = input("Entrer un entier supérieur ou égale à 0 : ")
        try:
            n = int(n)
            while n < 0:
                print("Pb de saisie")
                n = input("Entrer un entier supérieur ou égale à 0 : ")
            break
        except ValueError:
            print("Pb de saisie")
        except TypeError:
            print("Pb de saisie")

def estEntierPositif(n : str):
    try:
        n = int(n)
        if n < 0:
            return False
        else:
            return True
    except ValueError:
        return False

def saisit2():
    n = input("Entrer un entier supérieur ou égale à 0 : ")
    test = estEntierPositif(n)
    while not test:
        print("Pb de saisie")
        n = input("Entrer un entier supérieur ou égale à 0 : ")
        test = estEntierPositif(n)
    return int(n)

somme_carre(saisit2())
    
"""
Lorsque l'on saisit autre chose qu'un entier, l'exception ValueError est levée car la fonction int() ne peut pas convertir la chaîne de caractères en entier.

Le type de toute entrée via input est une chaîne de caractères.
"""

#Exercice 3:

def transform(l : str):
    l = l.split(";")
    l_result = [float(i)**0.5 for i in l]
    return l_result

test = "16;9;37.21;64;27.04"
print(transform(test))

def transform2(l : str):
    l = l.split(";")
    l_result = []
    for i in l:
        try:
            l_result.append(float(i)**0.5)
        except ValueError:
            print("Pb de saisie pour la valeur", i)
    return l_result

def estFloatPositif(n : str):
    try:
        n = float(n)
        if n < 0:
            return False
        else:
            return True
    except ValueError:
        return False

def transform3(l : str):
    l = l.split(";")
    l_result = []
    for i in l:
        if estFloatPositif(i):
            l_result.append(float(i)**0.5)
        else:
            print("Pb de saisie pour la valeur", i)
    return l_result
    
    
"""
Avec test = "16;9;37.21;64;27.04 ;", on leve l'exception ValueError car il y a un element vide dans la liste. Celui-ci ne peut pas etre converti en float.
Avec test = "16;9;37.21;-64;27.04", on leve l'exception ValueError car il y a un element negatif dans la liste. Celui-ci ne peut pas avoir de racine carrée.
"""