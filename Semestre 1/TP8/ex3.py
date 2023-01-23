def ecrire(nom,n):
    """
    Cette fonction écrit n lignes dans un fichier nom.
    """
    f=open(nom, 'w')
    for i in range(n):
        f.write(f"Texte de la ligne n°{str(i+1)}\n")
    f.close()
    return

def copierFin(source, destination, n):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i>=n:
                    g.write(texte)

"""
La fonction copierFin copie les n dernières lignes d'un fichier source dans un fichier destination.
"""

def copierEntre(source, destination, n, m):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i>=n and i<=m:
                    g.write(texte)

def copierLignesPaires(source, destination):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i%2==0:
                    g.write(texte)

def copierLignesImpaires(source, destination):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i%2!=0:
                    g.write(texte)