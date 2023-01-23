#Exercice 1

import math

class Legume():
    def __init__(self,nom,stock,prix):
        self.nom = nom
        self.stock = stock
        self.prix = prix
    def __str__(self):
        return "{} : stock {} kg, prix {} euros par kg".format(self.nom,self.stock,self.prix)
    def metAJour(self,quantité):
        self.stock += quantité
        if self.stock < 0:
            self.stock = 0
        if quantité > 0:
            print("{} kg de {} en plus, valeur du stock : {} euros, il reste {} kg en stock".format(quantité,self.nom,self.prix*self.stock,self.stock))
        elif quantité < 0:
            print("{} kg de {} en moins, valeur du stock : {} euros, il reste {} kg en stock".format(-quantité,self.nom,self.prix*self.stock,self.stock))

tomate = Legume("tomate",10,1.5)
print(tomate)
tomate.metAJour(5)
print(tomate)
tomate.metAJour(-15)
print(tomate)

class Courge(Legume):
    def __init__(self,nom,stock,prix,rayon):
        super().__init__(nom,stock,prix)
        self.rayon = rayon
    def volume(self):
        print("Le volume moyen d'une courge {} est {} cm3".format(self.nom,4/3*math.pi*self.rayon**3))

courge = Courge("courge",10,1.5,10)
print(courge)
courge.volume()

#Exercice 2

class Controle():
    defaut = {}
    nbControles = 0
    def __init__(self,date:str,poids:list,diametres:list,hauteurs:list):
        self.date = date
        self.poids = poids
        self.diametres = diametres
        self.hauteurs = hauteurs
        Controle.defaut[date] = [tuple(self.poids),tuple(self.diametres),tuple(self.hauteurs)]
        Controle.nbControles += 1
    def moyenne(self):
        return (sum(self.poids)/len(self.poids),sum(self.diametres)/len(self.diametres),sum(self.hauteurs)/len(self.hauteurs))
    @staticmethod
    def parfait(poids,diametre,hauteur):
        return poids < 3 and diametre > 3.8 and diametre < 4.2 and hauteur >= 23
    def __str__(self):
        string = "Controle du {}\n".format(self.date)
        for i in range(0,len(self.poids)):
            string += "Mesure {} : Poids = {} kg, diametre = {} cm, hauteur = {} cm\n".format(i+1,self.poids[i],self.diametres[i],self.hauteurs[i])
        return string
    def __del__(self):
        del Controle.defaut[self.date]
        Controle.nbControles -= 1
    @staticmethod
    def nbMesuresDefauts():
        total_defauts = 0
        for control in Controle.defaut:
            for i in range(0,len(Controle.defaut[control][0])):
                if Controle.parfait(Controle.defaut[control][0][i],Controle.defaut[control][1][i],Controle.defaut[control][2][i]) == False:
                    total_defauts += 1
        return total_defauts
    def savdefauts(self,nom_fichier):
        with open(nom_fichier,"w") as fichier:
            for control in Controle.defaut:
                fichier.write("Mesures défaillantes controle {}\n".format(control))
                for i in range(0,len(Controle.defaut[control][0])):
                    if Controle.parfait(Controle.defaut[control][0][i],Controle.defaut[control][1][i],Controle.defaut[control][2][i]) == False:
                        fichier.write("Poids = {} kg, diametre = {} cm, hauteur = {} cm\n".format(Controle.defaut[control][0][i],Controle.defaut[control][1][i],Controle.defaut[control][2][i]))

control1 = Controle("01/01/2020",[2.8,3.5,2.9,3.2,3],[3.9,4,3.6,4.2,4],[23,24,22,23.5,23.9])
print(control1.moyenne())
print(control1.parfait(3,4,23))
print(control1)
control2 = Controle("02/01/2020",[3.1,3.2,3.3,3.4,3.5],[3.9,4,3.6,4.2,4],[23,24,22,23.5,23.9])
print(control2.moyenne())
print(control2.parfait(3,4,23))
print(control2)
print(Controle.defaut)
print(Controle.nbControles)
print(Controle.nbMesuresDefauts())

class ControleMachine(Controle):
    def __init__(self,date:str,poids:list,diametres:list,hauteurs:list,machine:str):
        super().__init__(date,poids,diametres,hauteurs)
        self.machine = machine
    def affiche(self):
        print("Machine : {}".format(self.machine))
        print(super().__str__())

control3 = ControleMachine("03/01/2020",[3.1,3.2,3.3,3.4,3.5],[3.9,4,3.6,4.2,4],[23,24,22,23.5,23.9],"machine1")
control3.affiche()
control3.savdefauts("defauts.txt")