from robot_sim.robot2 import *
from basiques.arene import *

class Strategy():
    def __init__(self):
        True
    def dessine_carre(self,taille):
        avancer=0
        #(nb_pas) = avancer de nb_pas
        #(-1) = tourner de 90 degres dans le sens anti-horaire
        i=0
        L = []
        while i<4 :
            L.append(taille)
            L.append(-1)
            i = i+1

        return L


    def avance_objectif(self,robot,xx,yy):
        x,y,z = robot.position
        L = []
        while x != xx :
            if x < xx :
                L.append(('x',1))
                x = x + 1
            if x > xx :
                L.append(('x',-1))
                x = x - 1


        L.append(('r',-90))
        
        while y != yy:
            if y < yy :
                L.append(('y',1))
                y = y + 1

            if y > yy :
                L.append(('y',-1))
                y = y - 1
                
        return L

    
        
                
        
        
        
        
        
