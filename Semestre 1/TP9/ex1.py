class Chat(object):
    def __init__(self, nom, race, poids, annee_de_naissance):
        self.nom = nom
        self.race = race
        self.poids = poids
        self.annee_de_naissance = annee_de_naissance
    def affiche(self):
        print("Nom : ", self.nom)
        print("Race : ", self.race)
        print("Poids : ", self.poids)
        print("Année de naissance : ", self.annee_de_naissance)
    def estPlusGrosQue(self, autreChat):
        if self.poids > autreChat.poids:
            print(self.nom, "est plus gros que", autreChat.nom)
            return True
        else:
            print(self.nom, "n'est pas plus gros que", autreChat.nom)
            return False
    def estPlusVieuxQue(self, autreChat):
        if self.annee_de_naissance < autreChat.annee_de_naissance:
            print(self.nom, "est plus vieux que", autreChat.nom)
            return True
        else:
            print(self.nom, "n'est pas plus vieux que", autreChat.nom)
            return False
