class Voiture(object):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.kilometrage = 0
    def roule(self, distance):
        self.kilometrage += distance
    def affiche(self):
        print("Marque : ", self.marque)
        print("Modèle : ", self.modele)
        print("Kilométrage : ", self.kilometrage)

voiture1 = Voiture("Ford", "Fiesta")
voiture2 = Voiture("Ford", "Focus")
voiture1.affiche()
voiture2.affiche()
voiture1.roule(100)
voiture2.roule(200)
voiture1.affiche()
voiture2.affiche()

class Conducteur(object):
    def __init__(self, nom):
        self.nom = nom
    def conduit(self, voiture, distance):
        voiture.roule(distance)
        print(self.nom, "a conduit", voiture.marque, voiture.modele, "pendant", distance, "kilomètres")
        print("Le kilométrage de la voiture est maintenant de", voiture.kilometrage, "kilomètres")

conducteur1 = Conducteur("Bob")
conducteur2 = Conducteur("Alice")
conducteur1.conduit(voiture1, 50)
conducteur2.conduit(voiture2, 100)
voiture1.affiche()
voiture2.affiche()
