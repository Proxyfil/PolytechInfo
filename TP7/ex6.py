def nombre(d):
    return len(list(d.keys()))

def stockTotal(d):
    return sum(list(d.values()))

def afficher(d):
    liste = []
    for i in d.keys():
        liste.append([i,d[i]])
    for i in sorted(liste, key=lambda x: x[0]):
        print(i[0],i[1])
    return

def fruitsDeStocksMax(d):
    liste = []
    for i in d.keys():
        liste.append([i,d[i]])
    for i in sorted(liste, key=lambda x: x[1], reverse=True):
        print(i[0],i[1])
    return

def fusion(d1,d2):
    d3 = {}
    for i in list(d1.keys()):
        d3[i] = d1[i]
    for i in list(d2.keys()):
        d3[i] = d2[i]
    return d3

print(fusion({"pomme": 5, "poire": 3, "banane": 2}, {"orange": 3}))