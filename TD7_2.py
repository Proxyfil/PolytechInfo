#Exercice 1:

mavar = {8,4,5,1,8,-2,4,8}
print(len(mavar))
print(mavar)
print(type(mavar))

"""
Cette variable est un ensemble, car elle est définie par des accolades.
Certains éléments sont en double, mais l'ensemble ne les prend pas en compte.
"""

"""
Cette instruction ne fonctionne pas, car les ensembles ne sont pas ordonnés.
"""

mavar.remove(5)
mavar.add(9)

mavar_10_5 = {i for i in range(-10,5)}

"""
On peut créer un ensemble de chaînes de caractères
"""

#Exercice 2:

e1 = {8,4,5}
e2 = {-1,8,2}
e3 = e1 | e2
e4 = e1 & e2
e5 = e1 - e2
print("e1=",e1," e2=",e2)
print("e1 | e2 = ",e3)
print("e1 & e2 = ",e4)
print("e1 - e2 = ",e5)

"""
| est l'opérateur d'union
& est l'opérateur d'intersection
- est l'opérateur de différence
"""

e6 = {4,4,8,5,8}
print("e1=e6 ? ",e1==e6)
print("e4<=e1 ? ",e4<=e1)

"""
= est l'opérateur d'égalité et permet ici de vérifier si deux ensembles sont identiques
<= est l'opérateur de sous-ensemble et permet ici de vérifier si un ensemble est inclus dans un autre
"""

#Exercice 3:

d = {2:4,5:25,3:9,7:49}
print(d)
print(type(d))
print(len(d))
for c in d :
    print("clé : ",c," valeur : ",d[c])
    
"""
Cette variable est un dictionnaire, car elle est définie par des accolades et contient des couples clé:valeur.
c prend les valeurs des clés du dictionnaire.
d[c] permet d'accéder à la valeur associée à la clé c.
"""

d2 = {7:49,5:25,2:4,3:9}
print(d2)
print(d==d2)

"""
Il n'y a pas d'ordre dans les dictionnaires.
"""

d3 = {c : c*c for c in range(0,10) if c%2==0}

"""
On peut pas avoir de clé en double. Mais on peut avoir des valeurs en double.
"""

#Exercice 4:

d={'Alice':[3,6,5], 'Bob':[7,7,7], 'Eve':[2,3,9], 'Hugo':[4,5,6]}

"""
La valeur de Bob est une liste.
"""

def notes(prenom):
    n = ""
    for notes in d[prenom]:
        n+=str(notes)+", "
    print(f"{prenom} a obtenu les notes : {n[:-2]}")
    return None

def moyenne(prenom):
    m = 0
    for notes in d[prenom]:
        m+=notes
    m/=len(d[prenom])
    print(f"{prenom} a une moyenne de {round(m, 2)}")
    return None

def moyenne_sans_mauvaise(prenom):
    m = 0
    liste_n = []
    n = d[prenom][0]
    for notes in d[prenom][1:]:
        if notes<n:
            liste_n.append(n)
            n = notes
        else:
            liste_n.append(n)
    for notes in liste_n:
        m+=notes
    m/=len(liste_n)
    print(f"{prenom} a une moyenne de {round(m, 2)}")
    return None

#Exercice 5:
    
di = {"léo" :10,"jo" :7, "lana" :9}
print(di)
print(di.get("jo",0))
print(di.get("ilo",0))

"""
get permet de récupérer la valeur associée à une clé.
le deuxieme argument est la valeur par défaut si la clé n'est pas présente.
"""

def suppsymbole(texte):
    textel = texte.lower()
    for symbole in [",",".","!","?",";",":"]:
        textel = textel.replace(symbole,"")
    return textel

def nombreApparitionsMots(texte):
    textel = suppsymbole(texte.lower())
    d = {}
    for mot in textel.split():
        d[mot] = d.get(mot,0)+1
    return d

def afficher(d):
    liste = []
    for c in d:
        liste.append((c,d[c]))
    liste.sort(key=lambda x:x[0])
    print(liste)
    return liste

afficher(nombreApparitionsMots("Dans ce texte, la chaîne texte apparaît deux fois, ainsi que le mot chaîne."))

#Exercice 6:

import turtle

def von_Koch(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        von_Koch(l/3, n-1)
        turtle.left(60)
        von_Koch(l/3, n-1)
        turtle.right(120)
        von_Koch(l/3, n-1)
        turtle.left(60)
        von_Koch(l/3, n-1)

def flocon(l,n):
    turtle.speed("fastest")
    for i in range(3):
        von_Koch(l,n)
        turtle.right(120)

flocon(300,6)
turtle.done()