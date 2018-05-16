from robot_sim.robot2 import *

class stop :
    def __init__(self,robot):
        self.robot = robot
        self.stop = False

    def update(self):
        self.robot.stop()
        self.stop = True
