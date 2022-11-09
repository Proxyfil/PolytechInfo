def copier(source, destination):
    f=open(source, 'r')
    g=open(destination, 'w')
    for texte in f:
        g.write(texte)
        f.close()
        g.close()

"""Ex 1
La fonction "copier" sert à copier le contenu d'un fichier texte dans un autre fichier texte."""

def numeroter(source, destination):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i = 0
            for texte in f:
                i+=1
                g.write(str(i)+" "+texte)


"""Ex 2
La fonction "numeroter" sert à numéroter les lignes d'un fichier texte."""

"""Ex 3"""
def entreCrochet1(file1,file2):
    f = open(file1, 'r')
    g = open(file2, 'w')
    for texte in f:
        g.write("["+texte[:-1]+"]\n")
    f.close()
    g.close()

def entreCrochet2(file1,file2):
    with open(file1, 'r') as f:
        with open(file2, 'w') as g:
            for texte in f:
                g.write("["+texte[:-1]+"]\n")

