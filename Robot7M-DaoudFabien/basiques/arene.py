from math import acos
from math import sqrt
from ast import literal_eval
from basiques.cube import *
from basiques.mur import *
from basiques.sol import *

class Arene :
    """ Classe Arene caracterisée par les attributs:
    - lx : sa limite (double) sur l'axe des x
    - ly : sa limite (double) sur l'axe des y
    - lz : sa limite (double) sur l'axe des z
    - liste_cube : une liste contenant des "cubes"(sol,mur,obstacle) avec leurs coordonnées dans l'arene
    """

    def __init__(self,lx,ly,lz,liste_cube,liste_strat):
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.liste_cube = liste_cube
        self.liste_strat=liste_strat

    def ajouter_cube(self,cube) :
        """Si c'est possible on ajoute un cube dans l'arene
            et on return True, et False sinon"""
        bx = -self.lx/2<=cube.x and cube.x <= self.lx/2
        by = -self.ly/2<=cube.y and cube.y <= self.ly/2
        bz = -self.lz/2<=cube.z and cube.z <= self.lz/2

        L = 0<=cube.x + cube.larg and cube.x + cube.larg <= self.lx
        l = 0<=cube.y + cube.long and cube.y + cube.long <= self.ly
        h = 0<=cube.z + cube.haut and cube.z + cube.haut <= self.lx
        
        if bx and by and bz :#and L and l and h:
            self.liste_cube.append(cube)
            return True
        return False

    def generateur_arene(self):

        if (len(self.liste_cube) == 0):
            s1 = Sol(0,0,0, self.lx, 0, self.lz)
            #self.ajouter_cube(s1)
            self.liste_cube.append(s1)
            taillex = self.lx  # taille de l'arene
            taillez = self.lz  # taille de l'arene
            larg_mur = 20  # largeur des murs de contour
            hauteur_max = self.ly # hauteur du mur (CST)

            m1 = Mur(0,0,-taillez/2, taillex+larg_mur,hauteur_max,larg_mur)
            m2 = Mur(taillex/2,0,0, larg_mur,hauteur_max,taillez+larg_mur)
            m3 = Mur(0,0,taillez/2, taillex+larg_mur,hauteur_max,larg_mur)
            m4 = Mur(-taillex/2,0,0, larg_mur,hauteur_max,taillez+larg_mur)

            self.ajouter_cube(m1)
            self.ajouter_cube(m2)
            self.ajouter_cube(m3)
            self.ajouter_cube(m4)
            #self.liste_cube.append(m1)
            #self.liste_cube.append(m2)
            #self.liste_cube.append(m3)
            #self.liste_cube.append(m4)
            #generation de cubes aleatoires
            """nb_obstacles = 5
            i = 0
            long_max = 90
            while i < nb_obstacles:
                x = random.randint(-taillex+long_max, taillex-long_max)
                z = random.randint(-taillez+long_max, taillez-long_max)
                long = random.randint(int(taillex/8), int(taillex/4))

                m = Cube(x, 0, z, long, self.ly/2, long)
                #self.ajouter_cube(m)
                self.liste_cube.append(m)
                i = i + 1
            """
    def safficher(self):

        """Methode d'affichage d'une arene au format :
        Arene(limiteX= , limiteY= , limiteZ= )
        Liste d'objet [    ,    ,    ]
        """
        print("-------------------------------------------------\nArene(limiteX=%.2f,limiteY=%.2f,limiteZ=%.2f)"
              %(self.lx, self.ly, self.lz))
        print("LISTE OBJET\n[")
        for i in self.liste_cube:
            print(i.safficher())
        print("]")
        

    def retirer_cube(self,x,y,z) :
        """Si il y'a un cube à la position (x,y,z) dans l'arene
            on le retire et on return True, sinon on return False """
        i = 0
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if c.x == x and c.y == y and c.z == z :
                del self.liste_cube[i]
                return True
            else :
                i= i+1
        return False

		

    def retourne_angle(self,x,y,xx,yy) :
        """ retourne un angle teta en radian selon une direction initale d'un
            vecteur u(x,y) et une les coordonées du vecteur de la prochaine
            direction d'un vecteur v(xx,yy) en paramètres """

        sgn = (x*yy)+(xx*y)
        u = sqrt((x*x)+(y*y)) #norme de u
        v = sqrt((xx*xx)+(yy*yy)) #norme de v
        
        tmp = ((x*xx)+(y*yy))/(u+v)
        teta = acos(tmp)

        if(sgn < 0):
            return -1*teta
        return teta

    def possede_sol(self):
        """Cherche si l'arene possède un sol ou non"""
        if len(self.liste_cube) == 0:
            return False
        else:
            for i in self.liste_cube:
                if isinstance(i, Sol):
                    return True
            return False
    
    
    def toSaveF(self, f):
        """Ecrit les coordonnees de l'arene dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Arene;' + str(self.lx) + ';' + str(self.ly) + ';' + str(self.lz) + ';\n')
        for cube in self.liste_cube:
            cube.toSaveF(f)
        for rob in self.liste_robot:
            rob.toSaveF(f)
    
def Creation_Arene() :
    """ Test d'une creation d'Arene vide"""
    liste_cube = [] #liste vide pour créer une arène vide
    lx = 500
    ly = 500
    lz = 500 # valeurs limites de l'arène

    arene = Arene(lx,ly,lz,liste_cube,[])

    return arene

def sauvegardeEnv(arene,nomfichier):
    with open(nomfichier,'w') as f:
        arene.toSaveF(f)
        print("Arene sauvegardée.")
        
	       
def chargerEnv(nomfichier):
    """Fonction de chargement, ouverture du fichier en mode lecture"""
    with open(nomfichier,'r') as f:
        liste_cube = list()
        """deux listes vides pour contenir les objets charges"""
        for line in f:
            ligne=line.split(";")
            if ligne[0] == 'Arene':
                """On cree une nouvelle arene avec les parametres trouves sur la ligne, separes par des ';' """
                arene = Arene(int(ligne[1]),int(ligne[2]),int(ligne[3]),liste_cube)
            elif ligne[0] == 'Cube':
                """On ajoute le cube a la liste de cube de l'arene, avec parametres trouves sur la ligne"""
                arene.liste_cube.append(Cube(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5]),int(ligne[6])))
            elif ligne[0] == 'Mur':
                arene.liste_cube.append(Mur(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5]),int(ligne[6])))
            elif ligne[0] == 'Sol':
                arene.liste_cube.append(Sol(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5])))
            elif ligne[0] == 'Robot':
                (x,y,z)=literal_eval(ligne[1])
                (a,b,c)=literal_eval(ligne[2])
                (lo,la,ha)=literal_eval(ligne[3])
                arene.liste_robot.append(Robot((x,y,z),(a,b,c),(lo,la,ha)))
        print("Arene chargée.")
        return arene
