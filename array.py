def verifier(tableau):
    """
    -Fonction permettante de vérifier la proportionnalité d'un tableau
    -Prend en entré le tableau sous forme de liste
    """

    coefficient = tableau[1][0] / tableau[0][0]
    proportionnalite = True
    j = 0

    for i in tableau[0]:
        if i * coefficient != tableau[1][j]:
            proportionnalite = False

        j += 1

    return proportionnalite 

def corriger(tableau):
    """
    -Fonction permettante de corriger un tableau non proportionnel
    -Prend en entré le tableau sous forme de liste
    -Renvoie le tableau corrigé
    """

    for i in range(len(tableau[0])):
        tableau[1][i] = tableau[0][i] * tableau[1][0] / tableau[0][0]

    return tableau

def completer(tableau): 
    """
    -Fonction permettante de completer un tableau
    -Prend en entré le tableau à compléter
    -Renvoie le tableau complété 
    """

    coefficient = tableau[1][0] / tableau[0][0]

    for i in range(len(tableau[0])):
        if tableau[0][i] == "x":
            tableau[0][i] = tableau[1][i] / coefficient 
        elif tableau[1][i] == "x":
            tableau[1][i] = tableau[0][i] * coefficient 

    return tableau 

def generer(a, b, n):
    """
    -Fonction permettante de générer un tableau proportionnel
    -Prend en entré a (le premier nombre du haut), b (le premier nombre du bas), n (le nombre de collones à générer)
    -Renvoie le tableau générer
    """

    tableau = [[a], [b]]
    i = tableau[0][0] + 1 

    for j in range(n):
        tableau[0].append(i)
        tableau[1].append(tableau[0][j + 1] * b / a)

        i += 1 

    return tableau
