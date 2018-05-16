#import

#code

class Simulation:
    def __init__(self,strategie):
        self.strategie=strategie

    def run(self):
        cpt=0
        
        while self.strategie.stop==False:
            self.strategie.update()
            cpt+=1

        print("Arret")
        self.strategie.robot.stop()
        
