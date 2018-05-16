from robot2I013 import *
from time import strftime
from datetime import datetime

"""
#code
robot = Robot2I013()
img = robot.get_image()
date = str(datetime.now())
#img.save(date+".jpg")
img.save("capture.jpg") #nom fixe pour pouvoir recuperer l'image facilement dans une autre strat


class strategieCamera:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False

    def update(self):
        self.robot.get_image()
        self.stop = True """


def captureimage(robot):
    """capture une image"""
    img = robot.get_image()
    img.save("capture.jpg")
