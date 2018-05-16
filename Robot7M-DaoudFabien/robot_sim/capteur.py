
#imports

from basiques.arene import *
from robot_sim.robot2 import *

#code


        

class Capteur: 
        def __init__(self,arene,robot):
                self.robot = robot
                self.arene = arene

        def isCube(x,y,z,cube): # FONCTIONNE
                """fonction qui chercher si un point x,y,z est dans un mur et retourne true dans ce cas. Sinon retourne false"""
                if (x <= cube.x+cube.larg and x >= cube.x) and (y <= cube.y + cube.long and y >= cube.y) and (cube.haut >= z and z >= cube.z):
                        #os.system("cls")
                        #print("VOUS ETES DANS UN MUR !")
                        return True
                return False

        def isCubeList(x,y,z,liste_cube):
                """fonction qui fait la meme chose que celle du dessus mais applique a la liste entiere d'objets de l'arene"""
                i = 0
                while i < len(liste_cube) :
                        objet = liste_cube[i]
                        if(not(isinstance(objet, Sol))):
                                if isCube(x,y,z,objet):
                                        #print("sortie pour objet :",i)
                                        return True
                        i = i + 1
                return False
        
        def detecter_distance(self):
                """donne la distance par rapport a l'obstacle situé devant la tete du robot"""
                distance_max_recherche = 150
                r = self.robot
                x,y,z = r.position
                long, larg, haut = r.dimension
                dirx, diry = r.direction
                (x0,y0), (x1,y1), (x2,y2), (x3,y3) = r.coords
                ex = (x0+x1)/2
                ey = (y0+y1)/2# coordonnées de l'éclaireur : mises à la tete du robot
                cpt = 0

                while cpt < distance_max_recherche:
                        if (isCubeList(ex,ey,haut,self.arene.liste_cube)):
                                return cpt
                        ex = ex + (r.tete.orientation[0]/10)
                        ey = ey + (r.tete.orientation[1]/10)
                        cpt += 1
                return -1

        def detecter_distance2(self,robot):
                """donne la distance par rapport a l'obstacle situé devant la tete du robot"""
                distance_max_recherche = 150
                r = robot
                x,y,z = r.position
                long, larg, haut = r.dimension
                dirx, diry = r.direction
                (x0,y0), (x1,y1), (x2,y2), (x3,y3) = r.coords
                ex = (x0+x1)/2
                ey = (y0+y1)/2# coordonnées de l'éclaireur : mises à la tete du robot
                cpt = 0
                """
                while(isCubeList(ex,ey,haut,self.arene.liste_cube) == False) and cpt < distance_max_recherche:
                        ex = ex + (r.tete.orientation[0]/10)
                        ey = ey + (r.tete.orientation[1]/10)
                        cpt += 1
                return cpt
                """
                while cpt < distance_max_recherche:
                        if (isCubeList(ex,ey,haut,self.arene.liste_cube)):
                                return cpt
                        ex = ex + (r.tete.orientation[0]/10)
                        ey = ey + (r.tete.orientation[1]/10)
                        cpt += 1
                return -1


                

        def detecter(self):
                """chercher si un objet est devant le robot retourne True dans ce cas"""
                zone = 3
                r = self.arene.liste_robot[0]
                x,y,z = r.position
                long, larg, haut = r.dimension
                dirx, diry = r.direction
                (x0,y0), (x1,y1), (x2,y2), (x3,y3) = r.coords
                ex = (x0+x1)/2
                ey = (y0+y1)/2# coordonnées de l'éclaireur : mises à la tete du robot
                

                i = 0
                while i < zone : # balayage de la zone
                        #print("Cpt.detec:",ex, ey)
                        if isCubeList(ex,ey,haut,self.arene.liste_cube):
                                #print("suis dans un bloc")
                                #print("cpt.detec:",ex,ey)
                                return True
                        #print("cpt.detec:",ex,ey)
                        ex = ex + r.tete.orientation[0]
                        ey = ey + r.tete.orientation[1]
                        i  = i + 1
                return False
