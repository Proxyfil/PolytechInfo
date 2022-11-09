class Cylindre():
    def __init__(self, rayon, hauteur, couleur="blanc", matière="inconnue"):
        self.rayon = rayon
        self.hauteur = hauteur
        self.couleur = couleur
        self.matière = matière

    def affich(self):
        print("Cylindre de rayon", self.rayon, "et de hauteur", self.hauteur, "de couleur", self.couleur, "et de matière", self.matière)

    def vol(self):
        return self.rayon**2*3.1415926535898*self.hauteur

    def __dict__(self):
        return {"rayon": self.rayon, "hauteur": self.hauteur, "couleur": self.couleur, "matière": self.matière}

    def __doc__(self):
        return "Cylindre de rayon {} et de hauteur {} de couleur {} et de matière {}".format(self.rayon, self.hauteur, self.couleur, self.matière)

cyl = Cylindre(5, 10, "rouge")
cyl2 = Cylindre(5, 10, matière="acier")

cyl.affich()
cyl2.affich()
cyl.vol()
cyl2.vol()

