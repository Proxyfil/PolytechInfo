class Joueur():
    cases = [['.','.','.'],['.','.','.'],['.','.','.']]
    fin = False
    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    @staticmethod
    def convention():
        output = ""
        for x in range(3):
            for y in range(3):
                output += '('+str(x)+','+str(y)+')'
            output+='\n'
        print(output)

    def afficheCases(self):
        output = ""
        for x in range(3):
            for y in range(3):
                output += self.cases[x][y]
            output+='\n'
        print(output)

    def gagne(self):
        for y in range(3):
            if self.cases[0][y] == self.cases[1][y] == self.cases[2][y] == self.symbole:
                return True
        for x in range(3):
            if self.cases[x][0] == self.cases[x][1] == self.cases[x][2] == self.symbole:
                return True
        if self.cases[0][0] == self.cases[1][1] == self.cases[2][2] == self.symbole:
            return True
        if self.cases[0][2] == self.cases[1][1] == self.cases[2][0] == self.symbole:
            return True
        return False

    def joue(self):
        entree = ""
        while entree not in ['0,0','0,1','0,2','1,0','1,1','1,2','2,0','2,1','2,2'] or self.cases[int(entree[0])][int(entree[2])] != '.':
            entree = input("Entrez une case à jouer (ex: 1,1): ")
        self.cases[int(entree[2])][int(entree[0])] = self.symbole
        self.afficheCases()
        if self.gagne():
            self.fin = True
            print(self.nom, "a gagné !")
            self.afficheCases()

j1, j2 = Joueur("Joueur 1", "X"), Joueur("Joueur 2", "O")

while not j1.fin and not j2.fin:
    j1.joue()
    if not j1.fin:
        j2.joue()