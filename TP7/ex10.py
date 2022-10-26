def nombreApparitionsCaractère(texte):
    liste = {}
    for etype in ['é','è','ê','ë']:
        texte = texte.replace(etype,'e')
    for otype in ['ô','ö','ò','ó']:
        texte = texte.replace(otype,'o')
    for atype in ['à','â','ä','á','ã','å']:
        texte = texte.replace(atype,'a')
    for utype in ['ù','û','ü','ú']:
        texte = texte.replace(utype,'u')

    for i in texte.lower():
        if i in liste:
            liste[i] += 1
        else:
            liste[i] = 1
    return liste

def afficher(d):
    liste = []
    for i in d.keys():
        if(i in ['é','è','ê','ë']):
            liste.append(['e',d[i]])
        liste.append((i,d[i]))
    return sorted(liste, key=lambda x: x[0])

print(afficher(nombreApparitionsCaractère("Bonjour, je m'appelle Pierre.")))