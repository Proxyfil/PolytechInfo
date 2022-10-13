from math import log, log10

def nbrDeChiffres(n):
    return int(log10(n))+1

def sommeDesChiffres(n):
    somme = 0
    for i in str(n):
        somme += int(i)
    return somme


print(nbrDeChiffres(1546))