class Vecteur(object):
    def __init__(self, xy = (0, 0)):
        self.xy = xy
    def affiche(self):
        print("x = ", self.xy[0])
        print("y = ", self.xy[1])
    def prodScal(self, autreVecteur):
        return self.xy[0] * autreVecteur.xy[0] + self.xy[1] * autreVecteur.xy[1]
    def somme(self, autreVecteur):
        return Vecteur((self.xy[0] + autreVecteur.xy[0], self.xy[1] + autreVecteur.xy[1]))

vecteur1 = Vecteur((1, 2))
vecteur2 = Vecteur((3, 4))
vecteur1.affiche()
vecteur2.affiche()
print("Le produit scalaire de", vecteur1.xy, "et", vecteur2.xy, "est", vecteur1.prodScal(vecteur2))
vecteur3 = vecteur1.somme(vecteur2)
vecteur3.affiche()   