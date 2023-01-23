class Perchiste():
    sportifs = {}
    def __init__(self, nom, sauts):
        self.nom = nom
        self.sauts = sauts
        self.sportifs[nom] = self.moyenne()

    def afficheSportif(self):
        CleOrdonnee = sorted(self.sportifs.keys())
        for key in CleOrdonnee:
            print(key, self.sportifs[key])

    def moyenne(self):
        self.sportifs[self.nom] = 0
        count = 0
        for i in self.sauts:
            if(i != "X"):
                self.sportifs[self.nom] += i
                count += 1
        return round(self.sportifs[self.nom]/count, 2)

    def affiche(self):
        print(self.nom, self.moyenne())
        print(self.sauts)

    def delete(self):
        del self.sportifs[self.nom]
        del self


class Perchiste2():
    sportifs = {}
    def __init__(self, nom, sauts):
        self.nom = nom
        self.sauts = sauts
        self.sportifs[nom] = self.moyenne()

    def afficheSportif(self):
        CleOrdonnee = sorted(self.sportifs.keys(), reverse=True)
        for key in CleOrdonnee:
            print(key, self.sportifs[key])

    def moyenne(self):
        self.sportifs[self.nom] = 0
        count = 0
        for i in self.sauts:
            for j in i[1]:
                if(j != "X"):
                    self.sportifs[self.nom] += j
                    count += 1

        self.sportifs[self.nom] = round(self.sportifs[self.nom]/count, 2)       
        return self.sportifs[self.nom]

    def affiche(self):
        print(self.nom, self.moyenne())
        for i in self.sauts:
            temp = i[0]+" : "
            for j in i[1]:
                temp += str(j) + ", "
            print(temp)

    def delete(self):
        del self.sportifs[self.nom]
        del self

s1 = Perchiste2("Renaud Lavillenie",[("Rio 2016",[5.75,5.85,5.93,"X",6.03]),("Berlin 2018",[5.80,"X",5.9,"X","X",5.95]),("Shangai 2018",[5.7,5.75,"X",5.81])])
s2 = Perchiste2("Serguei Bubka",[("Rome 1984",[5.85,"X",5.94]),("Paris 1985",[5.7,5.8,5.9,"X","X",6])])
s1.affiche()
print(" ")
s1.afficheSportif()
s1.delete()
s2.afficheSportif()
