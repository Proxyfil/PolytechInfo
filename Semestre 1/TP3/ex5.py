from ex4 import criblage
import random

def euclide(a,b):
    if b == 0:
        return a
    else:
        return euclide(b, a%b)

def verif():
    liste = [(662,414,2),(100,50,50),(100,25,25),(100,75,25),(100,0,100),(0,100,100),(0,0,0)]
    for i in liste:
        if euclide(i[0],i[1]) != i[2]:
            return False
    return True

def verifeuclide():
    entiers = criblage(1000)
    for i in range(0,100):
        p = random.choice(entiers)
        m1 = random.choice(entiers)
        m2 = random.choice(entiers)
        while m2 == m1:
            m2 = random.choice(entiers)
        if euclide(m1*p,m2*p) != p:
            return False
    return True

print(verifeuclide())