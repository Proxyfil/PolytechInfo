class Maliste(list):
    def __str__(self):
        chaine="["
        for i in self:
            chaine += str(i)
            chaine += (";")
        return chaine[:-1]+"]"
    def __add__(self,other):
        liste3 = []
        for i in self:
            liste3.append(i)
        for i in other:
            liste3.append(i)
        return Maliste(liste3)

L1 = Maliste([1,2,3])
L2 = Maliste([4,5])
print(L1+L2)