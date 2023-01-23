class Pluviometrie(object):
    anneesseche = {}
    def __init__(self,annee,pluis=[],simulation=False):
        self.annee = annee
        self.pluis = pluis
        if self.seche(pluis) and not simulation:
            Pluviometrie.anneesseche[annee] = (self.moyminmax()[0],self.moyminmax()[1],self.moyminmax()[2],sum(self.pluis))
    def moyminmax(self):
        moyenne = 0
        for i in self.pluis:
            moyenne += i
        moyenne = int(round(moyenne/len(self.pluis),0))
        minimum = min(self.pluis)
        maximum = max(self.pluis)
        return (moyenne,minimum,maximum)
    @staticmethod
    def seche(précipitations):
        return sum(précipitations) < 1000
    def __str__(self):
        liste_mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
        chaine = "Pluviométrie - Année : {}\n".format(self.annee)
        for mois in self.pluis:
            chaine += "{} : {} , ".format(liste_mois[self.pluis.index(mois)],mois)
        return chaine[:-3]
    def __del__(self):
        if self.annee in Pluviometrie.anneesseche:
            del Pluviometrie.anneesseche[self.annee]
    def nbAnneesTresTresSeches(self):
        return len([annee for annee in Pluviometrie.anneesseche if Pluviometrie.anneesseche[annee][3] < 500])
    def sevanneesseches(self,nom_fichier):
        with open(nom_fichier,"w") as f:
            f.write("Année;Moyenne;Minimum;Maximum;Total")

annee1 = Pluviometrie(2021,[207,587,554,110,162,189,135,125,132,117,317,411])
print(annee1)
annee2 = Pluviometrie(2019,[107,105,55,110,42,49,35,25,34,57,104,90])
print(Pluviometrie.anneesseche)

class Meteo(Pluviometrie):
    def __init__(self,annee,temp,pluis=[],simulation=False):
        super().__init__(annee,pluis,simulation)
        self.temp = temp
    def affiche(self):
        print("Temprératures moyennes - Année : {}".format(self.annee))
        print("Janvier : {} , Février : {} , Mars : {} , Avril : {} , Mai : {} , Juin : {} , Juillet : {} , Août : {} , Septembre : {} , Octobre : {} , Novembre : {} , Décembre : {}".format(self.temp[0],self.temp[1],self.temp[2],self.temp[3],self.temp[4],self.temp[5],self.temp[6],self.temp[7],self.temp[8],self.temp[9],self.temp[10],self.temp[11]))
        print(self)
    def simulerechauffement(self,degrés):
        news_temps = []
        for temp in self.temp:
            news_temps.append(temp + degrés)
        news_précipi = []
        for précipitation in self.pluis:
            news_précipi.append(précipitation * (- degrés*0.1,2))
        return Meteo(self.annee,news_temps,news_précipi,True)
    def histo(self):
        """Affiche un histogramme des précipitations"""
        print(f"Histogramme Année {self.annee}")
        liste_mois = ["Jan","Fév","Mar","Avr","Mai","Jui","Jui","Aoû","Sep","Oct","Nov","Déc"]
        maxchartemp = 0
        for temp in self.temp:
            if len(str(temp)) > maxchartemp:
                maxchartemp = int(len(str(temp)))
        for i in range(0,12):
            print(f"{liste_mois[i]} : temp= {self.temp[i]}{(maxchartemp-int(len(str(self.temp[i])))+1)*' '}pluis= {self.pluis[i]} {'*'*int(round(self.pluis[i]/10,0))}")

meteo1 = Meteo(2021,[5,4.5,9.7,12.2,18,25.9,31.3,34.2,30.2,23.8,14.2,9.2],[7,5,55,111,162,29,35,25,121,144,321,415])
print("\n")
meteo1.histo()