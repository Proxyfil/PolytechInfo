def afficherLignesEtLongueur(source):
#On affiche chaque ligne du fichier source et sa longueur.
    try:
        f=open(source, 'r')
        for ligne in f:
            print(ligne)
            lineFeed=0
            if ligne[-1]=='\n':
                lineFeed=1
        print("Longueur :", len(ligne)-lineFeed)
        f.close()
    except IOError:
        print("Lecture du fichier ",source," impossible.")

source=input("Saisir le nom du fichier source : ")
afficherLignesEtLongueur(source)

"""
Cette fonction affiche le contenu d'un fichier source et sa longueur.
"""

def nbligne(source):
    """
    Cette fonction calcule le nombre de lignes d'un fichier source.
    """
    try:
        f=open(source, 'r')
        nb_lignes=0
        for ligne in f:
            nb_lignes=nb_lignes+1
        f.close()
        return nb_lignes
    except IOError:
        print("Lecture du fichier ",source," impossible.")

def longueurPlusGrandeLigne(source):
    """
    Cette fonction calcule la longueur de la plus grande ligne d'un fichier source.
    """
    try:
        f=open(source, 'r')
        longueur=0
        for ligne in f:
            if len(ligne)>longueur:
                longueur=len(ligne)
        f.close()
        return longueur
    except IOError:
        print("Lecture du fichier ",source," impossible.")

f=open("monfichier2.txt", 'w')
f.write(" Hello\ndear")
f.close()
f=open("monfichier2.txt", 'r')
#listLig=f.readlines()
listLig=f.read().splitlines()
f.close()
print(listLig)

"""
la différence entre readlines() et read().splitlines() est que readlines() retourne une liste de lignes et read().splitlines() retourne une liste de lignes sans le caractère de fin de ligne.
"""

"""
la méthode splitlines() est une méthode de la classe str qui permet de découper une chaîne de caractères en une liste de lignes.
"""

