from robot2I013 import *

class strategieObstacle:
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.angle_prec,x = self.robot.get_motor_position()


    def update(self):
        stop = False
		
        dist_obst = self.robot.moyenne_dist()
        if dist > 1000 or dist == 8190 : # on continue si la distance est assez grande
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,150)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,150)
            angle_actuel,y = self.robot.get_motor_position()

        else : # obstacle trouve
            """ sinon on n'avance pas, on tourne a 90 degres on avance
                de 30 ou 40cm, puis on tourne le robot a sa position initiale
                """
		strat90 = strategieRot90(self.robot)
		statDroit = strategieToutDroit(self.robot)
		
		strat90.update('D') # tourner a droite
		stratDroit.update(30) # avancer 
		strat90.update('G')  # tourner a gauche
		stratDroit.update(30) # avancer
		strat90.update('G') # tourner a gauche 
		stratDroit.update(30) # avancer
		strat90.update('D') # tourner a droite
		
        # Quand l'obstacle a ete evite on continue d'avancer

        #self.robot.set_motor_dps(self.robot.MOTOR_LEFT,150)
        #self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,150)
                
            
        


        
        

        
        
