import random
import turtle
import time

# Définition de la taille de la grille
tailleGrille = {'nx': 7, 'ny': 7, 'largeur': 20}


# Matrice qui affiche ' ' pour chaque cellule morte
def creerGrille(tailleGrille):
    resultat = [['' for _ in range(tailleGrille['ny'])] for _ in range(tailleGrille['nx'])]
    return resultat


def init(grille, tailleGrille):
    pourcentage = 0
    # Pourcentage entre 10% et 50%
    while pourcentage < 0.1 or pourcentage > 0.5:
        pourcentage = int(100 * random.random()) / 100
    # Calcul des cellules vivantes     
    cellulesVivantes = int(round(pourcentage * tailleGrille['nx'] * tailleGrille['ny']))
    print(cellulesVivantes)
    count = 0

    while count != cellulesVivantes:
        x = int(tailleGrille['nx'] * random.random())
        y = int(tailleGrille['ny'] * random.random())
        # Vérification de l'occurrence 
        if grille[y][x] == '':
            grille[y][x] = 'V'
            count += 1
    print(grille)


# Dessin carré pour la grille
def carre(largeur):
    for _ in range(4):
        turtle.forward(largeur)
        turtle.right(90)


def positionner(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Dessin de la grille
def dessinerGrille(tailleGrille, grille):
    turtle.speed(0)
    # Pour que la grille soit positionnée au milieu
    turtle.penup()
    turtle.goto(-tailleGrille['nx'] * tailleGrille['largeur'] / 2, tailleGrille['ny'] * tailleGrille['largeur'] / 2)
    turtle.pendown()
    # On commence par dessiner la grille dans son entiereté
    for y in range(tailleGrille['ny']):
        for x in range(tailleGrille['nx']):
            positionner(-x * tailleGrille['largeur'], -y * tailleGrille['largeur'])
            carre(tailleGrille['largeur'])
            positionner(x * tailleGrille['largeur'], y * tailleGrille['largeur'])

    # Coloration des cases en fonction de la matrice, si grille[y][x]="V"
    # on colorie la case correspondante en rouge
    for y in range(tailleGrille['ny']):
        for x in range(tailleGrille['nx']):
            if grille[x][y] == "V":
                positionner(-y * tailleGrille['largeur'], -x * tailleGrille['largeur'])
                turtle.color("red")
                turtle.begin_fill()
                carre(tailleGrille['largeur'] - 1)
                turtle.end_fill()
                positionner(y * tailleGrille['largeur'], x * tailleGrille['largeur'])


# Fonction qui permet de définir le déroulement du jeu
def conditions(grille, tailleGrille):
    nouvelleGrille = creerGrille(tailleGrille)

    for y in range(tailleGrille['ny']):
        for x in range(tailleGrille['nx']):
            nbVoisins = 0
            # Définition des cellules voisines en prenant compte des cellules
            # qui sont aux extrémités
            for y2 in range(max(0, y - 1), min(tailleGrille['ny'], y + 2)):
                for x2 in range(max(0, x - 1), min(tailleGrille['nx'], x + 2)):
                    # On s'assure que l'on ne prenne pas en compte la
                    # case qu'on examine
                    if y2 == y and x2 == x:
                        continue
                    if grille[y2][x2] == "V":
                        nbVoisins += 1

            if grille[y][x] == "V":
                # Cellule vivante avec moins de 2 ou plus de 3 voisins vivants meurt 
                if nbVoisins < 2 or nbVoisins > 3:
                    nouvelleGrille[y][x] = ''
                # Cellule vivante avec 2 ou 3 voisins vivants vit  
                else:
                    nouvelleGrille[y][x] = 'V'
            else:
                # Cellule morte naît si elle a exactement 3 voisins vivants
                if nbVoisins == 3:
                    nouvelleGrille[y][x] = 'V'
                # Cellule morte qui a exactement 2 voisins vivants 
                # reste dans son état actuel 
                else:
                    nouvelleGrille[y][x] = ''
    return nouvelleGrille


def jouer(tailleGrille):
    grille = creerGrille(tailleGrille)
    init(grille, tailleGrille)
    dessinerGrille(tailleGrille, grille)
    while True:
        turtle.clear()
        dessinerGrille(tailleGrille, grille)
        grille = conditions(grille, tailleGrille)
        time.sleep(0.1)


# Exécution du jeu
jouer(tailleGrille)
