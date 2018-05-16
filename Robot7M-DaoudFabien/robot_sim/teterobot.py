import random
import math


class TeteRobot:
    """
    Classe caractérisé par:
    son orientation: doublet(orx, ory) la tete ne bouge pas sur l'axe Z donc pas de triplet seulement un doublet
    """

    def __init__(self, orientation, direction_robot):
        """Constructeur de la classe TeteRobot"""
        self.orientation = orientation
        self.direction_robot = direction_robot

    def rotationVecteur(self, vecteur, angle):
        angle = math.radians(angle)
        resultat_x = vecteur[0] * math.cos(angle) - vecteur[1] * math.sin(angle)
        resultat_y = vecteur[0] * math.sin(angle) + vecteur[1] * math.cos(angle)
        
        return (resultat_x, resultat_y)
    
    def rotation(self, angle):
        """Methode de rotation de tete"""

        #print("affiche dir robot:",self.direction_robot)

        dir_robot_tmp = self.direction_robot
        if (angle <= 180 or angle >= 0):
            nouvelle_orientation = self.rotationVecteur(dir_robot_tmp, angle-90)
            #print("nouvelle_orientation",nouvelle_orientation)
            self.setOrientation(nouvelle_orientation)
        else:
            return -1
        #vx = self.orientation[0]
        #vy = self.orientation[1]
        #angle = math.radians(angle)
        #vrx = vx * math.cos(angle) - vy * math.sin(angle)
        #vry = vx * math.sin(angle) + vy * math.cos(angle)
        #self.setOrientation((vrx,vry))

    def toString(self):
        return "ROBOT[Tete] | direction: {0}".format(self.orientation,)

    def safficher(self):
        """Methode d'affichage d'un robot au format :
        Robot[position, orientation, dimension]
        """
        return "[Tete] direction: {0}".format(self.orientation)
#________________________________GETTER_______________________________________

    def getOrientation(self):
        return self.orientation

#________________________________SETTER_____________________________________

    def setOrientation(self, orientation):
        self.orientation = orientation

def Creation_TeteRobot(robot):
    """Creation d'une tete de robot avec un direction fixee"""

    orx= 0
    ory= 25
    direction_robot = robot.direction
    return TeteRobot((orx, ory), (direction_robot))

