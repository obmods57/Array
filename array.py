class Array:

    def __init__(self, tableau, tableau2):
        self.tableau = tableau
        self.tableau2 = tableau2

    def Verif(self):
        self.coefficient = self.tableau[0] / self.tableau2[0]
        self.proportionnel = True

        for self.i in range(0, len(self.tableau)):
            if self.tableau2[self.i] * self.coefficient != self.tableau[self.i]:
                self.proportionnel = False

        if self.proportionnel is True:
            print ("Fin, le tableau est proportionnel.\n")
        else:
            print ("Fin, le tableau n'est pas proportionnel.\n")

    def Correction(self):
        self.coefficient = self.tableau[0] / self.tableau2[0]
        self.tableau_correct = []
        self.nombre_non_proportionnel = []
        self.proportionnel = True

        for self.i in range(0, len(self.tableau)):
            if self.tableau2[self.i] * self.coefficient != self.tableau[self.i]:
                self.tableau_correct.append(self.tableau[self.i] / self.coefficient)
                self.nombre_non_proportionnel.append(self.tableau2[self.i])
                self.proportionnel = False
            else:
                self.tableau_correct.append(self.tableau2[self.i])

        if self.proportionnel is True:
            print ("Ce tableau est proportionnel et n'a donc pas besoin de correction.\n")
        else:
            print ("Nombre du haut :", self.tableau)
            print ("Nombre du bas :", self.tableau_correct)

            print ("Nombre non proportionnels, corriges :", self.nombre_non_proportionnel)


#s = Array([1, 2, 4, 8, 16], [2, 4, 8, 17, 36])
#s.Verif()
#s.correction()
