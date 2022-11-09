import pickle
def creeFicDic():
    d={(True,True) : 1, (True,False) : 0, (False,True) : 0, (False,False) : 0}
    with open("dic.txt", 'wb') as f:
        pickle.dump(d,f)

creeFicDic()

"""
somme=0
for i in range(100):
    somme=somme+d[(i%2==0,i%3==0)]

Cet algorythme sert à compter le nombre de fois où les nombres de 0 à 99 sont divisibles par 2 et par 3."""

def calcul():
    """Calculer et afficher le combre d'entier entre 1 et 10e6 qui sont divisibles seulement par 3 ou seulement par 5"""
    somme=0
    d={(True,True) : 1, (True,False) : 0, (False,True) : 0, (False,False) : 0}
    for i in range(1000000):
        somme=somme+d[(i%3==0,i%5==0)]
    print(somme)