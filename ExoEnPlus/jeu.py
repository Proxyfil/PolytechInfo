class jeu():
    def __init__(self, premier_joueur: int, deuxieme_joueur="ordi"):
        self.tableau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.premier_joueur = premier_joueur
        self.deuxieme_joueur = deuxieme_joueur
        self.play = 1
        self.croix = [0,premier_joueur]
        self.liste_coups = []

    def jouer_case(self, cases: tuple, joueur: int):
        self.play = joueur
        if self.croix[1] != joueur:
            self.croix[0] = 0
            self.croix[1] = joueur
            self.liste_coups = []
        if self.croix[0] == 3:
            #print("trop jouer")
            return False
        """Verification que la case est bien dans le tableau"""
        if cases[0] > 2 or cases[1] > 2:
            #print("case pas dans le tableau")
            return False
        """Verification que la case est vide"""
        if self.tableau[cases[1]][cases[0]] != 0:
            #print("case deja prise")
            return False
        """Vérifie que tous les coups jouées sont bien sur la même ligne ou meme colonne mais pas en diagonale"""
        if len(self.liste_coups) > 0:
            for i in self.liste_coups:
                if i[0] != cases[0] and i[1] != cases[1]:
                    #print("coups impossible")
                    return False
        if len(self.liste_coups) == 3:
            return False
        self.croix[0] += 1
        self.liste_coups.append(cases)
        self.tableau[cases[1]][cases[0]] = "X"
        if self.tableau == [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]:
            return f"{self.play} à gagné !"
        return True

    def get_tableau(self):
        return self.tableau

    def ia(tableau,coup):
        poss3 = [[["X","X","X"],["0","0","0"],["0","0","0"]],[["X","0","0"],["X","0","0"],["X",]]]
        nbx = 0
        if(coup == 1):
            for i in tableau:
                for j in i:
                    if(i == "X"):
                        nbx += 1
            
            if(nbx == 3):
                tableauid = poss3.index(tableau)