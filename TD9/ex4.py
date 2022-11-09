
NbPoints = 0

class Point(object):
    def __init__(self, nom, xy : tuple):
        global NbPoints
        self.nom = nom
        self.xy = xy
        NbPoints += 1
    def affich(self):
        print(self.nom, self.xy)
    def nbDePoints(self):
        global NbPoints
        return NbPoints
    def destructeur(self):
        global NbPoints
        NbPoints -= 1
        del self
    def milieu(self, p2):
        return Point("Milieu", ((self.xy[0]+p2.xy[0])/2, (self.xy[1]+p2.xy[1])/2))

"""
un attribut de classe est un attribut qui appartient à la classe et non à l'instance de classe pour le nombre d'instance créé de cette classe on aurait pu utiliser un attribut de classe pour compter le nombre d'instance créé de cette classe
"""

Points1 = Point("A", (1, 2))
Points2 = Point("B", (3, 4))
Points3 = Point("C", (5, 6))
Points1.affich()
Points2.affich()
Points3.affich()
Points1.destructeur()
print(NbPoints)
