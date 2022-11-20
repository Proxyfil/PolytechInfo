class Ruche():
    def __init__(self,lieu,poids,humidité):
        self.lieu = lieu
        self.poids = poids
        self.humidité = humidité
    def moyenne(self):
        tot = 0
        for poid in self.poids:
            tot += poid[0]
        return tot/len(self.poids)
    def alerte(self):
        alerte = False
        for n in self.humidité[-3:]:
            if n >= 0.8:
                alerte = True
        if alerte == True:
            print("Attention à l'humidité")
        else:
            print("Pas de problème d'humidité")
    @staticmethod
    def difference(liste):
        liste_final = []
        for tuple in liste:
            liste_final.append(tuple[0]-tuple[1])
        return liste_final
    def picActivite(self):
        """ affiche le maximum et le ou les jours correspondant à l'activité
maximale (différence maximale de poids entre 7h du matin et 11h du matin). """
        liste = []
        for tuple in self.poids:
            liste.append(round(tuple[0]-tuple[1],1))
        print("Le maximum d'activité est de {} kg et il a eu lieu le(s) jour:".format(round(max(liste),1)),end="")
        for i in range(0,len(liste)):
            if liste[i] == max(liste):
                print(" {} ;".format(i+1),end="")
    def affiche(self):
        print(f"Ruche: {self.lieu}  ; poids moyen: {self.moyenne()} kg")
        self.alerte()
        self.picActivite()
            

arbre1 = Ruche("Bois de Houx a3",[(32.6,31.9),(32.7,31.6),(32.8,31.8),(32.9,31.6),(33.1,32.9),(33.1,32.7),(33.2,31.9),(33.4,33.1)],[30,80,80,80,0,80,80,80,0,20])
arbre1.alerte()
arbre1.affiche()

class RucheParrainee(Ruche):
    parrainages = {}
    def __init__(self,lieu,poids,humidité,nomParrain,montantVerse):
        super().__init__(lieu,poids,humidité)
        self.nomParrain = nomParrain
        self.montantVerse = montantVerse
        RucheParrainee.parrainages[lieu] = (nomParrain,montantVerse)
    def __del__(self):
        del RucheParrainee.parrainages[self.lieu]
    def afficheToutes(self,nom):
        liste_ruches_parrainees = [lieu for lieu in RucheParrainee.parrainages if RucheParrainee.parrainages[lieu][0] == nom]
        chaine = f"{len(liste_ruches_parrainees)} ruche(s) parrainée(s) par {nom} : "
        for lieu in liste_ruches_parrainees:
            chaine += f"{lieu} ; "
        somme_tot = 0
        for lieu in liste_ruches_parrainees:
            somme_tot += RucheParrainee.parrainages[lieu][1]
        print(chaine)
        print(f"Somme totale: {somme_tot} euros")
        
ruche1 = RucheParrainee("Bois de Houx a2",[(32.6,31.9),(32.7,31.6),(32.8,31.8),(32.9,31.6),(33.1,32.9),(33.1,32.7),(33.2,31.9),(33.4,33.1)],[50,80,60,50,80,80,0,80,20,10],"Alfred",3500)
ruche2 = RucheParrainee("Bois de Houx a3",[(32.6,31.9),(32.7,31.6),(32.8,31.8),(32.9,31.6),(33.1,32.9),(33.1,32.7),(33.2,31.9),(33.4,33.1)],[30,80,80,80,0,80,80,80,0,20],"Alfred",4100)

ruche1.afficheToutes("Alfred")
del ruche2
ruche1.afficheToutes("Alfred")