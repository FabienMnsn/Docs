#from robot_gopy.robot2I013 import *
from strategieRot90 import *
import math
#from robot_sim import *


class strategieCarre:
    #ceci est une strategie qui realise un carre de 70cm de cote
    #A TESTER EN VRAI !
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.cpt_exec=0
        self.angle_prec,x = self.robot.get_motor_position()
        self.en_train_de_tourner = False
        
    def update(self):
        angle_actuel,y = self.robot.get_motor_position()
        dist = ((angle_actuel - self.angle_prec)/360.0) * math.pi * (self.robot.WHEEL_DIAMETER/2.0) * 2
        #print(dist)

        
        self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE, 0, 255, 0)
        self.stop = False
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,200)
        angle_actuel,y = self.robot.get_motor_position()
        dist = ((angle_actuel - self.angle_prec)/360.0) * math.pi * (self.robot.WHEEL_DIAMETER/2.0) * 2
           
        
        if dist > 600 and dist < 700 : ### cas ou le robot doit ralentir
            self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE, 255, 128, 0)
            #test pour ralentir sur les 10 derniers centimetres/unite de mesure
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT + self.robot.MOTOR_LEFT,60)

        elif dist >= 700 : ### cas ou le robot doit s arreter pour tourner 
            self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE, 255, 0, 0)
            self.en_train_de_tourner == True

        elif self.en_train_de_tourner == True: ### cas ou le robot doit tourner a 90 degres
            #reset des valeurs des moteurs(angles)
            #self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            #self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1]) 
            #calcul de la distance a parcourir pour faire un tour de 90deg
            
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,0)
            strat = strategieRot90(self.robot)	###pas sur que ca marche comme ca a tester

            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,200)
            #self.stop = True
            #maj cpt de cote
            self.cpt_exec += 1
            
            #on passe (en_train_de_tourner) a false pour parcourir 70cm (un nouveau cote)
            #puis on reset les angles des moteurs ? ~> yaura surement un pb lors du retour dans le premier if
            #car les distances sont reset mais la lecture de (angle_prec) se fait a l'initialisation de la strat...
            #A TESTER SUR LE ROBOT
            self.en_train_de_tourner = False
            #self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            #self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])

        elif self.cpt_exec == 4: ### cas ou le carre est complete
            self.stop = True

        elif self.cpt_exec > 4:
            print ("le compteur de cote a depasse la valeur max 4 : pb?")
            self.stop = True
        

