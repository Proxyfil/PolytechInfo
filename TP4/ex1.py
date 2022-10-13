def saisie():
    entier = 0
    while entier <= 0:
        entier = int(input("Saisir un entier positif : "))
    return entier

def afficherTerme(entier):
    somme = 0
    for i in range(1, entier+1):
        somme = somme + 1/i**2
    print("La somme des termes est : ", somme, "et la valeur bizarre est : ", 3.1415926535898**2/6)

def main():
    entier = saisie()
    afficherTerme(entier)

main()