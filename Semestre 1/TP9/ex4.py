class Livre(object):
    dictISBN = {}
    def __init__(self, isbn, titre, list_auteurs, nbPages, prix):
        """ISBN de la forme 978-3-16-148410-0 soit étagère-zone-editeur-numéro-contrôle"""
        self.isbn = isbn
        self.titre = titre
        self.list_auteurs = list_auteurs
        self.nbPages = nbPages
        self.prix = prix
        self.dictISBN[self.isbn] = self.list_auteurs
    def revientPlusCher(self, autreLivre):
        prixpages1 = self.prix / self.nbPages
        prixpages2 = autreLivre.prix / autreLivre.nbPages
        if self.prix / self.nbPages > autreLivre.prix / autreLivre.nbPages:
            print(f"{self.titre} revient plus cher par page que {autreLivre.titre} de {prixpages1-prixpages2}€ par page")
            return True
        elif self.prix / self.nbPages == autreLivre.prix / autreLivre.nbPages:
            print(f"{self.titre} revient autant cher par page que {autreLivre.titre}")
            return None
        else:
            print(f"{autreLivre.titre} revient plus cher par page que {self.titre} de {prixpages2-prixpages1}€ par page")
            return False
    @staticmethod
    def extraction(liste):
        result = ""
        for i in liste:
            result += i + ", "
        return result[:-2]+"."
    def affiche(self):
        print(f"{self.titre} de : {Livre.extraction(self.list_auteurs)}\n   {self.nbPages} pages   {self.prix}euros    ISBN : {self.isbn}")
    @staticmethod
    def aCommun(liste1, liste2):
        for i in liste1:
            for j in liste2:
                if i == j:
                    return True
        return False
    def AuteurEnCommun(self, autreLivre):
        liste_commun = []
        for i in self.list_auteurs:
            for j in autreLivre.list_auteurs:
                if i == j:
                    liste_commun.append(i)
        if len(liste_commun) == 0:
            print(f"{self.titre} et {autreLivre.titre} n'ont aucun auteur en commun")
            return False
        else:
            print(f"{self.titre} et {autreLivre.titre} ont un ou des auteur(s) en commun: {Livre.extraction(liste_commun)}")
            return True
    def afficheAuteursEditeur(self, zone, editeur):
        list_auteurs = []
        for i in self.dictISBN:
            if i[5:7] == zone and i[8:11] == editeur:
                for j in self.dictISBN[i]:
                    list_auteurs.append(j)
        print(f"Les auteurs de l'éditeur n°{editeur} dans la zone {zone} sont : {self.extraction(list_auteurs)}")