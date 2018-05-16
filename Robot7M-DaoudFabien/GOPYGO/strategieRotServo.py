#imports

from robot2I013 import *
#from robot_sim.robot2 import *

#code
# marche pas : tete toutes les directions 
class strategieRotServo():

    def __init__(self, robot):
        self.robot = robot
        self.stop = False
        self.angle = 1
    """
    def update(self):
        pos = False
        if (pos == False):
            self.robot.servo_rotate(1)
            pos = True
        if (self.angle < 180):
            self.robot.servo_rotate(self.angle)
            self.angle += 1
            #print("angle:",self.angle)
        elif (self.angle == 0 or self.angle == 180):
            self.stop = True   
    """
    def update(self):
        pos = False
        if (pos == False):
            pos = True
            self.robot.servo_rotate(0)
            

        pos2 = False
        if (pos2 == False):
            pos2 = True
            self.robot.servo_rotate(180)
            
        else:
            self.stop = True
