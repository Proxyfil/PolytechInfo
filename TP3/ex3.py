import random

def fct(n):
    m = 2*n
    return (n,m)

def division_euclidienne(a,b):
    q = 0
    r = a
    while r >= b:
        r = r - b
        q = q + 1
    return (q,r)

def verif():
    for i in range(0,100):
        a = random.randint(0,10000)
        b = random.randint(0,10000)
        (q,r) = division_euclidienne(a,b)
        if q != a//b or r != a%b:
            print("Erreur: division_euclidienne(",a,",",b,") = (",q,",",r,")")
            return False
    return True

print(verif())