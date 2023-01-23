class Livre (object) :
    def __init__( self , auteur , titre , nbPages ) :
        self.auteur = auteur
        self.titre = titre
        self.nbPages = nbPages
    def affiche(self):
        print("Titre : " , self.titre )
        print("Auteur : ", self.auteur , " Pages : " , self.nbPages)

"""
méthodes : __init__ , affiche
attributs : auteur , titre , nbPages
"""

livre1 = Livre ( "Victor Hugo" , "Les Misérables" , 1500 )
livre2 = Livre ( "Jules Verne" , "Vingt mille lieues sous les mers" , 500 )
livre1.affiche()
livre2.affiche()