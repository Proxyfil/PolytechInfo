def affiche(listeChaines1,listeChaines2) :
    if len(listeChaines1) !=len(listeChaines2) :
        print("Pb : nb d’éléments différents")
    else :
        print("Scientifiques :")
    for i in range(0,len(listeChaines1)) :
        s = listeChaines1[i]+" "+listeChaines2[i]
        print(s)

def construction(lis1,lis2):
    output = []
    for i in range(max(len(lis1),len(lis2))):
        output.extend([lis1[i],lis2[i]])
    return output

def eclatement(lis):
    pair = []
    impair = []
    for i in range(0,len(lis),2):
        pair.extend([lis[i]])
    for i in range(1,len(lis),2):
        impair.extend([lis[i]])
    return (pair,impair)

def rassemble(lis):
    pair = lis[0]
    impair = lis[1]

    output = []
    for i in range(len(pair)):
        output.append(pair[i] + " " + impair[i])
    return output

lis1=["Albert", "Marie", "Raymond"]
lis2=["Einstein", "Curie", "Poincaré"]
print(rassemble(eclatement(construction(lis1,lis2))))
