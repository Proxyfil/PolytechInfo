class Personnage():
    nbPerso = 0
    def __init__(self, nom, position : tuple, pointsVie, pointsAttaque, pointsDefense):
        global nbPerso
        self.nom = nom
        self.position = position
        self.pointsVie = pointsVie
        self.pointsAttaque = pointsAttaque
        self.pointsDefense = pointsDefense
        self.nbClone = 0
        Personnage.nbPerso += 1
    def __del__(self):
        del self
        Personnage.nbPerso -= 1
    def destructeur(self):
        Personnage.nbPerso -= 1
        del self
    def affiche(self):
        print(self.nom, self.position, self.pointsVie, self.pointsAttaque, self.pointsDefense)
    def attaque(self, p2):
        if (p2.position[0] - self.position[0])**2 + (p2.position[1] - self.position[1])**2 > 10:
            print("Trop loin")
        else:
            p2.pointsVie -= self.pointsAttaque - p2.pointsDefense
            if p2.pointsVie <= 0:
                p2.pointsVie = 0
    def deplace(self, position):
        self.position = position
    def clone(self):
        self.nbClone += 1
        return Personnage(self.nom+str(self.nbClone), self.position, self.pointsVie, self.pointsAttaque, self.pointsDefense)
    @staticmethod
    def NbPerso():
        return Personnage.nbPerso
    @staticmethod
    def regle_attaque():
        return "La distance entre les deux personnages doit être inférieure ou égale à 10."

Marc = Personnage("Marc", (1, 2), 1, 10, 5)
Marc.affiche()
Antoine = Personnage("Antoine", (3, 4), 1, 10, 5)
Antoine.affiche()
Jean = Personnage("Jean", (5, 6), 1, 10, 5)
Jean.affiche()
Paul = Personnage("Paul", (17, 18), 1, 10, 5)
Paul.affiche()
Marc.attaque(Antoine)
Marc.affiche()
Antoine.affiche()
Jean.attaque(Paul)
Jean.affiche()
Paul.affiche()
Marc.deplace((3, 4))
Marc.affiche()
Antoine.affiche()
Jean.deplace((17, 18))
Jean.affiche()
Paul.affiche()
print(Personnage.regle_attaque())
print(Personnage.NbPerso())
Marc.destructeur()
print(Personnage.NbPerso())
