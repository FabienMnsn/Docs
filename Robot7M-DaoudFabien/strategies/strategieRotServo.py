#imports

#from robot_gopy.robot2I013 import *
from robot_sim.robot2 import *

#code

class strategieRotServo():

    def __init__(self, robot):
        self.robot = robot
        self.stop = False
        self.angle = 0

    def update(self):
        if (self.angle <= 180):
            self.robot.servo_rotate(self.angle)
            self.angle += 9
            #print("angle:",self.angle)
        else:
            self.stop = True
