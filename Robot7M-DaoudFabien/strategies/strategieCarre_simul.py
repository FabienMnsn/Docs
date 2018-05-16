#from robot_gopy.robot2I013 import *
from strategies.strategieRot90 import *
from strategies.strategieToutDroit70 import *
import math
from robot_sim import *


class strategieCarre:
    #ceci est une strategie qui realise un carre de 70cm de cote
    #A TESTER EN VRAI !
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.cpt_exec=0
        self.en_train_de_tourner = False
        
    def update(self):
        strat70 = strategieToutDroit70(self.robot)
        strat90 = strategieRot90(self.robot)

        #while self.cpt_exec < 4 :
        strat70.update()
        strat90.update()
        self.cpt_exec = self.cpt_exec + 1

    
