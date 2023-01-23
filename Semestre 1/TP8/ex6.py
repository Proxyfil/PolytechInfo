def lireCoordonnees(source):
    """
    Cette fonction lit un fichier source et renvoie une liste de coordonnées sous forme de tuples.
    """
    try:
        f=open(source, 'r')
        listCoord=[]
        for ligne in f:
            listCoord.append((int(ligne.split(',')[0][1:]), int(ligne.split(',')[1][:-2])))
        f.close()
        return listCoord
    except IOError:
        print("Lecture du fichier ",source," impossible.")

import math

def distance(coord1, coord2):
    """
    Cette fonction calcule la distance euclidienne entre deux points.
    """
    return math.sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)

def distanceTotale(listCoord):
    """
    Cette fonction calcule la distance totale d'une liste de coordonnées.
    """
    dist=0
    for i in range(len(listCoord)-1):
        dist+=distance(listCoord[i], listCoord[i+1])
    return dist*(10**-2)

print(lireCoordonnees("points.txt"))
print(distanceTotale(lireCoordonnees("points.txt")))