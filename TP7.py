#Exercice 1:

def f(n):
    if 0<=n and n<=7:
        return n-1
    else:
        return f(n+3)

def g(n):
    if (n>=6):
        return n-1
    else :
        return g(n-8)

def h(n):
    if (n<=10):
        return 3
    else:
        return h(n-8)

"""
Les fonctions f,g et h sont récursives.
En effet, elles ont toutes un cas de base et un cas récursif.

La fonction f a pour cas de base 0<=n<=7 et pour cas récursif n>7.
La fonction g a pour cas de base n>=6 et pour cas récursif n<6.
La fonction h a pour cas de base n<=10 et pour cas récursif n>10.
"""

#Exercice 2:

def binome(n, p):
    if p == n:
        return 1
    elif p == 0:
        return 1
    elif 0<=p<=n:
        return binome(n-1, p-1) + binome(n-1, p)

#Exercice 3:

def listeSansDoublons(l):
    lresult = []
    lset = set(l)
    for element in lset:
        lresult.append(int(element))
    return sorted(lresult)

def valeursCommunes(l1,l2):
    lresult = []
    l1set = set(l1)
    l2set = set(l2)
    for element in l1set:
        if element in l2set:
            lresult.append(int(element))
    return lresult

#Exercice 4:

maliste = list("Un Texte")
print(maliste)
monEnsemble = set("Un Texte")
print(monEnsemble)

"""
La premiere variable contient une liste avec tout les caractères du texte. (contenu entre deux crochets)
La seconde variable contient un ensemble avec tout les caractères du texte. (pas en double) (contenu entre deux accolades)
"""

def memesLettres(s1,s2):
    return set(s1) == set(s2)

#Exercice 5:

dico = {25:4, 8:1, 12:2, 3:5}
print(dico)
print("5 dans dico ? ", (5 in dico))
print("25 dans dico ? ", (25 in dico))
dico[9]=1
dico[8]=2
print(dico)
del dico[25]
print(dico)

inventaire = {'orange':378, 'pomme':545, 'banane':422, 'poire':269}

def stock():
    fruit = input("Quel fruit voulez-vous ? ")
    if fruit in inventaire:
        print("Il y a",inventaire[fruit],"fruits",fruit,"en stock.")
    else:
        print("Il n'y a pas de",fruit,"en stock.")
    return None

def ajout(stock: int):
    fruit = input("Quel fruit voulez-vous ? ")
    stock = int(input("Quel est le stock ? "))
    if fruit in inventaire:
        if inventaire[fruit] != stock:
            inventaire[fruit] = stock
            print("Le stock a été mis à jour.")
        else:
            print("Le stock est déjà à jour.")
    else:
        inventaire[fruit] = stock
        print("Le fruit a été ajouté au stock.")
    return None

def suppression():
    fruit = input("Quel fruit voulez-vous ? ")
    if fruit in inventaire:
        del inventaire[fruit]
        print("Le fruit a été supprimé du stock.")
    else:
        print("Ce fruit n'est pas dans le stock.")
    return None

#Exercice 6:

def nombre(d):
    return len(d)

def sotckTotal(d):
    total = 0
    for fruit in d:
        total += d[fruit]
    return total

def affiche(d):
    for fruit in d:
        print(f"Fruit : {fruit}, stock : {d[fruit]}")
    return None

def fruitsDeStockMax(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)

def fusion(d1,d2):
    return {**d1, **d2}

#Exercice 7:

def moyenne(l):
    if "ABI" not in l:
        if "ABJ" in l:
            for i in range(len(l)):
                if l[i] == "ABJ":
                    l[i] = 0
                else:
                    l[i] = int(l[i])
        return round(sum(l)/len(l),2)
    else:
        return "défaillant"

def moyennesEtudiants(d):
    return sorted([(etudiant,moyenne(d[etudiant])) for etudiant in d])

#Exercice 8:
import random

presentateur = {(1, 1): (2, 3), (1, 2): (3, 3), (1, 3): (2, 2),(2, 1): (3, 3), (2, 2): (1, 3), (2, 3): (1, 1),(3, 1): (2, 2), (3, 2): (1, 1), (3, 3): (1, 2)}
"""
Clé = (porte gagnante, porte choisie par le joueur au début) : Valeur = (porte_à_ouvrir_1,
porte_à_ouvrir_2)
"""

alea = {1: (2, 3), 2: (1, 3), 3: (1, 2)}

change = {(1,2):3,(1,3):2,(2,1):3,(2,3):1,(3,1):2,(3,2):1}

def choix_presentateur(porte_gagnante,porte_joueur):
    return presentateur[(porte_gagnante,porte_joueur)][0]

def strategie_aleatoire(porte_debut,porte_ouverte):
    return random.choice(alea[porte_ouverte])

def strategie_change(porte_debut,porte_ouverte):
    return change[(porte_debut,porte_ouverte)]

def strategie_ne_change_pas(porte_debut,porte_ouverte):
    return porte_debut

def experience(n):
    resultat = {"aleatoire": 0, "change": 0, "ne_change_pas": 0}
    for i in range(n):
        porte_gagnante = random.randint(1,3)
        porte_debut = random.randint(1,3)
        porte_ouverte = choix_presentateur(porte_gagnante,porte_debut)
        if strategie_aleatoire(porte_debut,porte_ouverte) == porte_gagnante:
            resultat["aleatoire"] += 1
        if strategie_change(porte_debut,porte_ouverte) == porte_gagnante:
            resultat["change"] += 1
        if strategie_ne_change_pas(porte_debut,porte_ouverte) == porte_gagnante:
            resultat["ne_change_pas"] += 1
    resultat["aleatoire"] = resultat["aleatoire"]/n
    resultat["change"] = resultat["change"]/n
    resultat["ne_change_pas"] = resultat["ne_change_pas"]/n
    return resultat

"""
La meilleure stratégie est de changer de porte.
"""

#Exercice 9:

def cal_min():
    a_min = 1
    b_min = 2
    c_min = 3
    d_min = 4
    resultat_min = (10 * a_min + b_min - c_min) * d_min
    a = 1
    while a <= 4:
        b = 1
        while b <= 4:
            c = 1
            while c <= 4:
                d = 1
                while d <= 4:
                    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                        resultat = (10 * a + b - c) * d
                        if resultat < resultat_min:
                            resultat_min = resultat
                            a_min = a
                            b_min = b
                            c_min = c
                            d_min = d
                            print('(', a_min, b_min, ' - ', c_min, ') x ', d_min)
                            print('=', resultat_min)
                    d += 1
                c += 1
            b += 1
        a += 1
    return None

def permutations(start, end=[]):
    # Si la liste start est vide, on renvoie la liste end
    if len(start) == 0:
        print(end)
    # Sinon on parcourt la liste start
    # On ajoute le premier élément de start à la fin de end
    # On appelle récursivement permutations avec start[1:] et end
    # On ajoute à end la liste start sans le premier élément
    else:
        for i in range(len(start)):
            permutations(start[:i]+start[i+1:],end+start[i:i+1])

permutations([4,5,6])

def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
def permutationsV2(start, end=[],res=[]):
    if len(start) == 0:
        res.append(end)
    else:
        for i in range(len(start)):
            permutationsV2(start[:i]+start[i+1:],end+start[i:i+1],res)
    if len(res)>0 and len(res)==fact(len(res[0])): #res contient le nbtotal de permutations
        return res

print(permutationsV2([4,5,6]))

"""
Nous avons introduit la fonction fac qui calcule la factorielle d'un nombre car nous avons besoin de connaître le nombre total de permutations possibles pour une liste donnée. Nous avons donc utilisé cette fonction dans la fonction permutationsV2 pour vérifier que nous avons bien trouvé toutes les permutations possibles.
permutationsV2 retourne une liste de listes. Chaque liste est une permutation possible de la liste start.
"""

def permutationsV3(start, end=[],res=[]):
    if len(start) == 0:
        res.append(end)
    else:
        for i in range(len(start)):
            permutationsV3(start[:i]+start[i+1:],end+start[i:i+1],res)
    return res

#Exercice 10:

def nombreApparitionsCaracteres(texte):
    texte = accents(texte).lower()
    app = {}
    for lettre in texte:
        if lettre in app:
            app[lettre] += 1
        else:
            app[lettre] = 1
    return app

def afficher(d):
    result = []
    for lettre in d:
        result.append((lettre,d[lettre]))
    print(result)
    return None

def accents(texte):
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
 
    for i in range(len(texte)):
        chaine = chaine.replace(accent[i], sans_accent[i])
    return texte

#Exercice 11:

#ONLY SECOND VARIANT

from turtle import color,right, left, forward, speed, exitonclick, hideturtle

def dragon(level=4, size=200, direction=45,couleur='red'):
    color(couleur)
    if level:
        right(direction)
        dragon(level-1, size/1.41421356237, direction, couleur)
        left(direction * 2)
        dragon(level-1, size/1.41421356237, -direction, couleur)
        right(direction)
    else:
        forward(size)

speed(1000)
hideturtle()
#dragon(10,400,45)
exitonclick()

#Exercice 12

def ajouter(index,entree,numero):
    if entree in index:
        if numero not in index[entree]:
            index[entree].append(numero)
    else:
        index[entree] = [numero]
    return None

def listeNumerosDePages(l):
    result = ""
    for element in l:
        result += str(element)+' '
    return result

def afficherIndex(index):
    index2 = sorted(index)
    for entree in index2:
        print(entree,':',listeNumerosDePages(sorted(index[entree])))
    return None

def creationIndexPages(index):
    indexpages = {}
    for element in index:
        for element2 in index[element]:
            if element2 not in indexpages:
                indexpages[element2] = [element]
            else:
                indexpages[element2].append(element)
    return indexpages

def listeEntrees(l):
    result = ""
    for element in l:
        result += str(element)+' '
    return result

def afficherIndexPages(index):
    index2 = sorted(index)
    for entree in index2:
        print(entree,':',listeEntrees(sorted(index[entree])))
    return None

#Exercice 13

R = {"a": ["a","b","c","d"],"b": ["a","b","c","d"],"c":["c","d"],"d":["c","d","e"]}

def ensemble(R):
    return set(R)

def identite(E):
    "une relation pour laquelle chaque élément de E est en relation avec lui-même."
    return [(x,x) for x in E]

def est_reflexive(R):
    E = ensemble(R)
    I = identite(E)
    return set(I).issubset(set(R))

def est_symetrique(R):
    return set([(y,x) for (x,y) in R]).issubset(set(R))

def est_antisymetrique(R):
    return set([(x,y) for (x,y) in R if x!=y]).issubset(set(R))

def est_transitive(R):
    return set([(x,z) for (x,y) in R for (y2,z) in R if y==y2]).issubset(set(R))

def composee(R,S):
    return set([(x,z) for (x,y) in R for (y2,z) in S if y==y2])

def est_ordre(R):
    return est_reflexive(R) and est_antisymetrique(R) and est_transitive(R)

def est_equivalence(R):
    return est_reflexive(R) and est_symetrique(R) and est_transitive(R)