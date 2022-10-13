import random

def saisieSomme():
    entier = 0
    while entier < 2 or entier > 12:
        entier = int(input("Saisir un entier entre 2 et 12 : "))
    return entier

def somme2des():
    valeurs = (random.randint(1,6),random.randint(1,6))
    print("Valeurs 1 : ", valeurs[0], "Valeurs 2 : ", valeurs[1])
    return valeurs[0]+valeurs[1]

def jouer():
    guess = saisieSomme()
    result = somme2des()
    print("Somme des 2 dés : ", result)
    if(guess == result):
        print("Gagné !")
    else:
        print("Perdu !")

jouer()