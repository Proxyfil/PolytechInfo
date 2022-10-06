def impaires(n):
    return [i for i in range(1, n, 2)]

def somme_puissance_impaires(n,p):
    sum = 0
    for i in impaires(n):
        sum += i**p
    return sum