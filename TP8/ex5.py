def lire(source):
    """
    Cette fonction lit un fichier source et renvoie une liste de lignes.
    """
    try:
        f=open(source, 'r')
        listLig=f.read().splitlines()
        f.close()
        return listLig
    except IOError:
        print("Lecture du fichier ",source," impossible.")

def ecrire(l, destination):
    """
    Cette fonction écrit une liste de lignes l dans un fichier destination.
    """
    try:
        f=open(destination, 'w')
        for ligne in l:
            f.write(ligne)
            f.write('\n')
        f.close()
    except IOError:
        print("Ecriture du fichier ",destination," impossible.")

print(lire("musique.txt"))

def copierEnTriantTitres(source, destination):
    """
    Cette fonction copie le contenu d'un fichier source dans un fichier destination en triant les lignes par ordre alphabétique des titres.
    """
    listLig=lire(source)
    listLig.sort()
    ecrire(listLig, destination)

def copierEnRenversant(source, destination):
    """
    Cette fonction copie le contenu d'un fichier source dans un fichier destination en renversant l'ordre des lignes.
    """
    listLig=lire(source)
    listLig.reverse()
    ecrire(listLig, destination)

def CopierEnTriantArtistes(source, destination):
    """
    Cette fonction copie le contenu d'un fichier source dans un fichier destination en triant les lignes par ordre alphabétique des artistes.
    """
    listLig=lire(source)
    listLig.sort(key=lambda x: x.split(' - ')[0])
    ecrire(listLig, destination)

