import random

def bezout(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = bezout(b % a, a)
        return (g, x - (b // a) * y, y)

def verif():
    for i in range(0,10):
        a = random.randint(0,1000)
        b = random.randint(0,1000)
        res = bezout(a,b)
        if(res[0] != a*res[1]+b*res[2]):
            return False
    return True

print(verif())