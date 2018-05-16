#imports

from robot_gopy.robot2I013 import *
from images import traitementimage
from strategie import captureimage

#code

class strategieSuivieBalise:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False

    def update(self, distance):
        #alignement central de la tete du robot
        self.servo_rotate(90)
        #get distance(mm) avec le capteur
        distance = self.moyenne_dist()
        #capture et traitement d'une image
        captureimage()
        coords = traitement_image("capture")
        if (distance < 200):
            #colision imminente
            #arret provisoire
            self.stop = True
        else:
            if (coords[0] < 335 and distance > 200):
                #le centre de la balise detectee est a gauche du champs de vision du robot
                self.servo_rotate(45)
                #strategie rotation avec un angle precis A FAIRE
                
            elif (coords[0] > 385 and distance > 200):
                #balise detectee a droite du champs de vision du robot
                self.servo_rotate(135)
                #strategie rotation avec un angle precis A FAIRE

            elif (coords[0] < 385 and coords[0] > 335 and distance > 200):
                #balise + ou - au centre de l'image
                self.servo-rotate(90)
                self.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,180)

            elif (coords[0] == -1):
                #aucune balise detectee
                #arret provisoire
                self.stop = True
