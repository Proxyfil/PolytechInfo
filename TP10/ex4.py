import math

class Arbre(object):
    listeDesArbresOk = []
    def __init__(self, ref, haut = 10, ray = 0.5, etatOk = True):
        self.ref = ref
        self.haut = haut
        self.ray = ray
        self.etatOk = etatOk
        if self.etatOk:
            Arbre.listeDesArbresOk.append(self.ref)
    @staticmethod
    def volTronc(r,h):
        return round(math.pi*(r**2)*h, 2)
    def affiche(self):
        ref = self.ref.split(" ")
        print(f"Essence: {ref[0]} ; position: ( {ref[1]} ; {ref[2]} )")
        print(f"Hauteur: {self.haut} ; rayon: {self.ray} ; volume: {self.volTronc(self.ray,self.haut)} cm3")
        if self.etatOk:
            print("Etat: bon")
        else:
            print("Etat: mauvais")
    def destruction(self):
        Arbre.listeDesArbresOk.remove(self.ref)
        object.__del__(self)
    def __del__(self):
        if self.etatOk:
            Arbre.listeDesArbresOk.remove(self.ref)
    def nbArbresOk():
        print(f"Nb d'arbres en bon état: {len(Arbre.listeDesArbresOk)}")
    def afficheUneEssence(essence):
        print(f"Coordonnées GPS {essence} en bon état:")
        for arbres in Arbre.listeDesArbresOk:
            if arbres.split(" ")[0] == essence:
                print(f"    {arbres.split(' ')[1]}   {arbres.split(' ')[2]}")

class ArbreTraite(Arbre):
    def __init__(self, ref, traitement, dates, haut = 10, ray = 0.5, etatOk = True):
        super().__init__(ref, haut, ray, etatOk)
        self.dates = dates
        self.traitement = traitement
    def affiche(self):
        super().affiche()
        print(f"traitement: {self.traitement} effectué {len(self.dates)} fois :")
        for date in self.dates:
            print(f" le {date[0]}/{date[1]}/{date[2]}")
    def ajouteDate(self, date):
        self.dates.append(date)
    def traitementAnnee(self, annee):
        nb = 0
        for date in self.dates:
            if date[2] == annee:
                nb += 1
        print(f"Essence: {self.ref.split(' ')[0]}  position: ( {self.ref.split(' ')[1]} ; {self.ref.split(' ')[2]} ) traité {nb} fois en {annee}")
        
        
                

arbre1 = Arbre("Chêne 47.052508 4.383403", 158, 6)
arbre1.affiche()