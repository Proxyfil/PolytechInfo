class Chien():
    
    def __init__(self, identification, nom, race, dateNaiss, taille = 0, poids = 0):
        self.identification = identification  
        self.nom = nom
        self.race = race
        self.dateNaiss = dateNaiss
        self.taille = taille
        self.poids = poids
        
    def affiche(self):
        print(f"{self.nom} est un chien de race {self.race}\nIl est né le {self.dateNaiss[0]} / {self.dateNaiss[1]} / {self.dateNaiss[2]}")
        if self.taille != 0:
            print(f"Il mesure {self.taille} cm")
        if self.poids != 0:
            print(f"Il pèse {self.poids} kg")
        print(f"Il est tatoué : {self.identification}")

c1 = Chien("P250263890203125","Tara","Bichon",(2,5,2022),25.5)
c1.affiche()
c2 = Chien("TAG896","Sophia","Berger",(3,6,2021),48,5.6)
c2.affiche()

class Candidat(Chien):
    
    concoursT = []
    
    def __init__(self, identification, nom, race, dateNaiss, taille = 0, poids = 0, concours = []):
        super().__init__(identification,nom, race, dateNaiss, taille, poids)
        self.concours = concours
        for concour in concours:
            if concour not in Candidat.concoursT:
                Candidat.concoursT.append(concour)
                
    def affiche(self):
        super().affiche()
        if len(self.concours) != 0:
            print(f"Il a participé à {len(self.concours)} concours:")
            for concours in self.concours:
                print(f"    {concours}")
        else:
            print("Il n'a participé à aucun concours")
            
    def participe(self, concours):
        self.concours.append(concours)
        if concours not in Candidat.concoursT:
                Candidat.concoursT.append(concours)
    
    def concoursConnus(self):
        print(f"Voici les concours que nous avons répertoriés: {Candidat.concoursT}")

cand1 = Candidat("P250261992073142","Sangdor","Caniche",(12,6,2021),31.5,3.1,["Tours canin 2022","Mon chien 2022"])
cand1.affiche()
cand1.participe("Concours canin Langeais 2022")
cand1.affiche()