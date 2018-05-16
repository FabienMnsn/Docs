#imports

#from robot_gopy.robot2I013 import *
from robot_sim.robot2 import *
from robot_sim.utilitaires_geometrie import *
#code

class strategieRot_90():

    def __init__(self,robot):
        self.stop = False
        self.robot = robot
        self.dir_robot = robot.direction
        #self.dir_depart = robot.direction
        self.dir_arrivee = rotation2D(self.dir_robot,90)
        self.angle = 0


    def update(self):
        
        if self.angle < 30:
            self.angle += 1
            #self.robot.calcul_coords_angle(self.angle)
            self.robot.rotation(-3)
            #print(self.angle)
        else:
            print("fin de la strategie rotation -90")
            self.stop = True
            self.robot.stop()
            

