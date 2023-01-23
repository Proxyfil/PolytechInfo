import random

def estPremier(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def criblagesimple(n):
    """Renvoie la liste des nombres premiers inférieurs ou égaux à n"""
    premiers = [0,2]
    for i in range(3, n + 1):
        for p in premiers:
            if i % p == 0:
                premiers.append(0)
                break
        else:
            premiers.append(i)
    return premiers

def criblage(n):
    """Renvoie la liste des nombres premiers inférieurs ou égaux à n"""
    premiers = [2]
    for i in range(3, n + 1):
        for p in premiers:
            if i % p == 0:
                break
        else:
            premiers.append(i)
    return premiers

def verif():
    q = criblage(10000)
    for i in range(0,100):
        b = random.randint(0,1000)
        if(estPremier(b) != (b in q)):
            return False
    return True

print(verif())