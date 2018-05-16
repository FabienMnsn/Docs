#imports strategies
from strategies.simulation import *
from strategies.strategieToutDroit70 import *
from strategies.strategieRot90 import *
from strategies.strategieCarre import *
from strategies.strategieRotServo import *

#imports robots
#from robot_sim.robot2 import *
from robot_gopy.robot2I013 import *

#code


#________________VARIABLES DE SELECTION___________________


STRAT = 0

###____numero de la strategie____####
# 0 = strategietoutdroit70          #
# 1 = strategieRot90                #
# 2 = strategieRotServo             #
# 3 = strategieCarre                #
# 4 = NON ASSIGNEE                  #
#####################################

ROBOT = 1           #(0=simulation, 1=gopigo)

#________________INSTANCES DE ROBOT_______________________
rob_phy = Robot2I013()
#rob_sim = Creation_Robot()

#________________SWITCH ENTRE SIMULATIONS_________________
if  (STRAT == 0):
    ## tout droit 70
    if(ROBOT == 1):
        #robot physique
        strategie = strategieToutDroit70(rob_phy)
    else:
        strategie = strategieToutDroit70(rob_sim)
        
#____________________________________________________   
elif(STRAT == 1):
    ## rotation90
    if(ROBOT == 1):
        strategie = strategieRot90(rob_phy)
    else:
        strategie = strategieRot90(rob_sim)
        
#____________________________________________________
elif(STRAT == 2):
    ## rotation servo
    if(ROBOT == 1):
        strategie = strategieRotServo(rob_phy)
    else:
        strategie = strategieRotServo(rob_sim)
        
#____________________________________________________
elif(STRAT == 3):
    ## dessin carre
    print("strat <carre:",STRAT,"> non definie !")
    
#____________________________________________________
elif(STRAT == 4):
    ##autre strat a venir...
    print("strat",STRAT," non definie !")
    
#____________________________________________________
else:
    print("Error : bad 'SIM' number <",STRAT,">")
    
#________________LANCEMENT DE LA SIMULATION_______________

simulation = Simulation(strategie)
print("**Debut de la strategie**")
simulation.run()
print("**Fin de la strategie**")