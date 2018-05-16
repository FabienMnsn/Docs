from basiques.cube import Cube
import random

class Mur(Cube):
    """Classe héritant de la classe Cube, caractérisée par:
        -ses coordonnées: x, y, z
        -sa hauteur
        -sa largueur
        -sa longueur"""

    def __init__(self, x, y, z, larg, long, haut):
        """Constructeur de la classe Mur"""
        Cube.__init__(self,x,y,z,larg,long,haut)

    def safficher(self):
        """Methode d'affichage d'un mur au format :
        mur[x= , y= , z= , larg= , long= , haut= ]
        """
        print("Mur(x=%.2f,y=%.2f,z=%.2f, larg=%.2f,long=%.2f,haut=%.2f)"%(self.x, self.y, self.z, self.larg, self.long, self.haut))
			
def Creation_Mur():
    """Création d'un mur avec une hauteur et une epaisseur fixé par les limites de l'Arene"""

    x = random.randint(0, 50)
    y = random.randint(0, 50)
    z = random.randint(0, 50)

    larg = random.randint(10, 50) #largeur arbitraire
    long = 200#un mur va jusq'au plafond
    haut = random.randint(10, 50)  
    
    return Mur(x, y, z, larg, long, haut)



#creation d'u constructeur temporaire pour l'affichage tkinter
def Creation_Mur_xy(x, y):
    """Création d'un mur avec une hauteur et une epaisseur fixé par les limites de l'Arene"""

    x = x
    y = y
    z = 1  # un mur est posé au sol

    larg = 60
    long = 35
    haut = 499  # un mur monte jusqu'au plafond

    return Mur(x, y, z, larg, long, haut)
    
    
