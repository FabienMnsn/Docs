from robot_gopy.robot2I013 import *
import math





class strategieToutDroit70:
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.angle_prec,x = self.robot.get_motor_position()
        #print("angle prec",self.angle_prec)

    def update(self,distance):
        stop=False
        
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,200)
        angle_actuel,y = self.robot.get_motor_position()
        #print("angle actuel",angle_actuel)
        dist = ((angle_actuel - self.angle_prec)/360.0) * math.pi * (self.robot.WHEEL_DIAMETER/2.0) * 2
        #print("diff",(angle_actuel - self.angle_prec)/360.0)
        #print("angles:",self.angle_prec, angle_actuel)
        #print("distance",dist)
        if dist > distance*10:
            self.stop = True
            
