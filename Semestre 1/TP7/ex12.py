def ajouter(index,entrée,numéro):
    if entrée in index:
        index[entrée].append(numéro)
    else:
        index[entrée] = [numéro]
    return index

def listeNuméroDePage(l):
    out = ""
    for i in sorted(l):
        out += str(i) + " "
    return out[:-1]

def afficherIndex(index):
    for i in sorted(index.keys()):
        print(i,':', listeNuméroDePage(index[i]))
    return

def créationIndexPages(index):
    out = {}
    for i in list(index.keys()):
        for j in index[i]:
            if(j not in out.keys()):
                out[j] = [i]
            else:
                out[j].append(i)
    return out

def listeEntrées(l):
    out = ""
    for i in sorted(l):
        out += i + " "
    return out

def afficherIndexPages(indexPages):
    for i in sorted(indexPages.keys()):
        print(i,':', listeEntrées(indexPages[i]))
    return

index={}
ajouter(index, 'Liste', 32)
ajouter(index, 'Liste', 58)
ajouter(index, 'Liste', 47)
ajouter(index, 'Dictionnaire', 58)
ajouter(index, 'Dictionnaire', 62)
ajouter(index, 'Python', 14)
ajouter(index, 'Python', 32)
ajouter(index, 'Python', 29)
afficherIndexPages(créationIndexPages(index))
print(listeEntrées(['Liste', 'Dictionnaire', 'Python']))

