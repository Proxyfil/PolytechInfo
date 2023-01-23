from urllib.request import urlopen
page = urlopen("http://www.pallier.org/extra/liste.de.mots.francais.frgut.txt")
lignes = page.readlines()
page.close()
chaine = "".join(ligne.decode("utf8") for ligne in lignes)
mots_courants = "".join(car for car in chaine if car.isalpha()).lower()
resultat = "".join(car for car in mots_courants if ord("a") <= ord(car) <= ord("z"))

"""
La premiere ligne de ce programme permet de télécharger le fichier texte contenant la liste des mots courants en français. La deuxième ligne permet de lire le contenu de la page web. La troisième ligne permet de fermer la connexion. La quatrième ligne permet de convertir les octets en chaîne de caractères. La cinquième ligne permet de supprimer les caractères non alphabétiques. La sixième ligne permet de convertir la chaîne de caractères en minuscules. La septième ligne permet de supprimer les caractères qui ne sont pas des lettres de l'alphabet.
"""

def createDictFreq(mots):
    """
    Cette fonction crée un dictionnaire de fréquences à partir d'une chaîne de caractères.
    """
    dictFreq={}
    for car in mots:
        if car in dictFreq:
            dictFreq[car]+=1
        else:
            dictFreq[car]=1
    return dictFreq