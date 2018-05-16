#import

import random

#code

class Balise:
    """Classe Balise, caractérisée par:
        -ses coordonnées: x, y, z (coords du centre)
        -sa hauteur
        -sa largueur"""

    def __init__(self, x, y, z, haut):
        """Constructeur de la classe Balise"""
        self.x = x
        self.y = y
        self.z = z
        self.haut = haut
        
    def safficher(self):
        """Methode d'affichage d'une Balise au format :
        mur[x= , y= , z= , larg= , haut= ]
        """
        return "Balise(x=%.2f,y=%.2f,z=%.2f, haut=%.2f)"%(self.x, self.y, self.z, self.haut)

def Creation_Balise():
    """creation d'une balise de coords et taille aleatoire"""

    x = random.randint(25, 75)
    y = random.randint(25, 75)
    z = random.randint(25, 75)

    haut = random.randint(50, 80)

    return Balise(x, y, z, haut)
