import random
def jeu1():
    print(random.randint(0,1) == int(input("Entrer un nombre pair ou impaire : "))%2)

def jeu2():
    robot = random.randint(0,2)
    utilisateur = input("Entrez +, - ou = : ")
    if utilisateur == "+" and robot == 0:
        print("Gagné :-)")
    elif utilisateur == "-" and robot == 1:
        print("Gagné :-(")
    elif utilisateur == "=" and robot == 2:
        print("Gagné :-|")
    else:
        print("Perdu :-/")

def jeu():
    entree = 0
    while entree not in [1,2]:
        entree = int(input("Choisir un jeu (1 ou 2): "))
    if(entree == 1):
        jeu1()
    else:
        jeu2()

jeu()
