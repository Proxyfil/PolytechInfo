import random
presentateur = {(1, 1): (2, 3), (1, 2): (3, 3), (1, 3): (2, 2), (2, 1): (3, 3), (2, 2): (1, 3), (2, 3): (1, 1), (3, 1): (2, 2), (3, 2): (1, 1), (3, 3): (1, 2)}

alea = {1: (2,3), 2:(1,3), 3:(1,2)}
change = {(1,2):3, (1,3):2, (2,1):3, (2,3):1, (3,1):2, (3,2):1}

def choix_presentateur(porte_gagnante,porte_joueur):
    return random.choice(presentateur[(porte_gagnante,porte_joueur)])

def strategie_alea(porte_debut,porte_ouverte):
    return random.choice(alea[porte_debut])

def strategie_change(porte_debut,porte_ouverte):
    return change[(porte_debut,porte_ouverte)]

def strategie_garde(porte_debut,porte_ouverte):
    return porte_debut

def experience(n):
    a = 0
    g = 0
    c = 0

    for i in range(n):

        porte_gagnante = random.randint(1,3)
        porte_joueur = random.randint(1,3)
        porte_ouverte = choix_presentateur(porte_gagnante,porte_joueur)
        if strategie_alea(porte_joueur,porte_ouverte) == porte_gagnante:
            a += 1
        if strategie_change(porte_joueur,porte_ouverte) == porte_gagnante:
            c += 1
        if strategie_garde(porte_joueur,porte_ouverte) == porte_gagnante:
            g += 1
    print("Gagne avec alea : ", a/n)
    print("Gagne avec change : ", c/n)
    print("Gagne avec garde : ", g/n)

experience(100000)
