def factoriel(n):
    resu = 1
    for i in range(1,n+1):
        resu = resu * i
    return resu

def somme(n):
    resu = 0
    for i in range(0,n+1):
        resu = resu + 1/factoriel(i)
    return resu

print(somme(5))