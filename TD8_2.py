def lire(source):
    f = open(source, 'r')
    s = f.read()
    f.close()
    return s

print(lire("exo1Marceline.txt"))

"""
Le paramètre source est le nom du fichier à lire.
Le paramètre "r" indique que le fichier est ouvert en lecture.
close() permet de fermer le fichier.
f sert de variable intermédiaire. Elle contient le contenu du fichier. On appel ce type de variable un fichier virtuel.
"""

def lire1(source):
    with open(source, 'r') as f:
        print(f.read())
    return None

def lire2v1(source):
    f = open(source, 'r')
    lignes = f.readlines()
    for ligne in lignes:
        print(ligne, end="")
    return None

def lire2v2(source):
    f = open(source, 'r')
    for ligne in f:
        print(ligne, end="")
    return None

def estLisible(source):
    try:
        f = open(source, 'r')
        f.close()
        return True
    except IOError:
        return False
    
def lire3(source):
    if estLisible(source):
        f = open(source, 'r')
        lignes = f.readlines()
        for ligne in lignes:
            print(ligne, end="")
        return None
    else:
        print("Le fichier n'est pas lisible.")
        return None

def nombreCaracteres(source):
    f = open(source, 'r')
    lignes = f.readlines()
    n = 0
    for ligne in lignes:
        n += len(ligne)
    return n

#Exercice 2:

def ecrire(source, s):
    f = open(source, "w")
    f.write(s)
    f.close()
    return None

ecrire("exo2.txt","j’adore l’informatique")

"""
Le paramètre s est la chaîne de caractères à écrire dans le fichier.
Le paramètre "w" indique que le fichier est ouvert en écriture.
"""

def ecrire1(nom,s,n):
    f = open(nom, "w")
    for i in range(n):
        f.write(s+"\n")
    f.close()
    return None

def ajouter(nom,s,n):
    f = open(nom, "a")
    for i in range(n):
        f.write(s+"\n")
    f.close()
    return None

def ecrire2(nom,s,n):
    if estLisible(nom):
        f = open(nom, 'r')
        for i in range(n):
            f.write(s+"\n")
        f.close()
        return None
    else:
        print("Le fichier n'est pas lisible.")
        return None

#Exercice 3:

import pickle

vote = {"Jo":32,"Seb":15,"Zoé":29}

def sauvegarde(source):
    f = open(source, "wb")
    pickle.dump(vote, f)
    f.close()
    return None

def restaure(source):
    f = open(source, "rb")
    vote = pickle.load(f)
    f.close()
    return vote

def affiche(source):
    vote = restaure(source)
    for i in vote:
        print(f"Candidat: {i}  nb de votes: {vote[i]}")
    return None

def ajouter(source,key,n):
    vote = restaure(source)
    vote[key] = n
    sauvegarde(source)
    return None

def heureuxElu1(source):
    vote = restaure(source)
    max = 0
    for i in vote:
        if vote[i] > max:
            max = vote[i]
            nom = i
    print(f"Le candidat {nom} est l'heureux élu avec {max} votes.")
    return None

def heureuxElu2(source):
    vote = restaure(source)
    max = []
    for i in vote:
        if vote[i] == max(vote.values()):
            max.append(i)
    print(f"Les candidats {max} sont les heureux élus avec {max(vote.values())} votes.")
    return None

#Exercice 4:

def creerListe(nom_pgm):
    f = open(nom_pgm, "r")
    f_lines = f.readlines()
    liste_fonctions = []
    for ligne in f_lines:
        if ligne[0:3] == 'def':
            liste_fonctions.append(ligne[4:-2])
    f.close()
    return liste_fonctions

def sauvegarde(nom_pgm,destination):
    f_save = open(destination, "wb")
    pickle.dump(creerListe(nom_pgm), f_save)
    f_save.close()
    return None

def affiche(destination):
    f = open(destination, "rb")
    liste_fonction = pickle.load(f)
    for i in liste_fonction:
        print(f"Fonction: {i.split('(')[0]}   paramètre(s): {i[i.find('(')+1:i.find(')')]}")
    f.close()
    return None

#Exercice 5:

def concatener(source1,source2,destination):
    f_source1 = open(source1, "r")
    f_source2 = open(source2, "r")
    f_destination = open(destination, "w")
    f_destination.write(f_source1.read())
    f_destination.write(f_source2.read())
    f_source1.close()
    f_source2.close()
    f_destination.close()
    return None

def entrelacer(source1,source2,destination):
    f_source1 = open(source1, "r")
    f_source2 = open(source2, "r")
    f_destination = open(destination, "w")
    while True:
        ligne1 = f_source1.readline()
        ligne2 = f_source2.readline()
        if ligne1 == "" and ligne2 == "":
            break
        if ligne1 != "":
            f_destination.write(ligne1)
        if ligne2 != "":
            f_destination.write(ligne2)
    f_source1.close()
    f_source2.close()
    f_destination.close()
    return None