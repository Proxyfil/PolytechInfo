class Inventaire(dict):
    def __str__(self):
        chaine = ""
        trié = sorted(self.items())
        for i in trié:
            chaine += "{} : {}\n".format(i[0],i[1])
        return chaine
    def __add__(self,other):
        dictionnaire = {}
        for i in other:
            if i in self:
                dictionnaire[i] = self[i] + other[i]
            else:
                dictionnaire[i] = other[i]
        return Inventaire(dictionnaire)

inv1 = Inventaire({'pâtes' : 2, 'farine' : 1, 'lessive' : 2})
print(inv1)
inv2 = Inventaire({'pâtes' : 1, 'sucre' : 2, 'lessive' : 1})
print(inv2)
print(inv1 + inv2)
print(inv1)

class Inventaire():
    def __init__(self,nom,inventaire):
        self.nom = nom
        self.inventaire = inventaire
    def __str__(self):
        print(f"Inventaire {self.nom}")
        print(self.inventaire)
    def __add__(self,other):
        name = ""
        if self.nom == other.nom:
            name = self.nom
        elif self.nom == "":
            name = other.nom
        elif other.nom == "":
            name= self.nom
        elif len(self.inventaire) > len(other.inventaire):
            name = self.nom
        else:
            name = other.nom
        new = Inventaire(name,self.inventaire+other.inventaire)
        return new
        