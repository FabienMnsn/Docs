#import

#from tkinter import *
#from interface.interface import *

#code

class Simulation:
    def __init__(self,strategie):
        self.strategie=strategie

    def run(self):
        cpt=0
        
        ######
        #view = Interface()
        ######
        
        while self.strategie.stop==False:
            self.strategie.update()

            ######
            #test = self.strategie.robot
            #print(self.strategie.robot.safficher())
            #view.rafraichir(test)
            ######
            
            cpt+=1
        print("Arret")
        self.strategie.robot.stop()
        
