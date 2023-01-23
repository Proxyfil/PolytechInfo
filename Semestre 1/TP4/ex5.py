import math

def AfficherSommesDeCubes():
    cubes = []
    for i in range(10):
        cubes.append(i**3)

    for i in range(100,1000):
        somme = 0
        for j in range(3):
            somme += cubes[int(str(i)[j])]
        if somme == i:
            print(i)

def Afficher2(n):

    for i in range(100,n):
        somme = 0
        for j in range(len(str(i))):
            somme += int(str(i)[j])**len(str(i))
        if somme == i:
            print(i)

Afficher2(100000)