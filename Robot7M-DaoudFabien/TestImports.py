
#import de basiques
from basiques import cube
from basiques import arene
from basiques import mur
from basiques import sol

#imports de images
from images import traitementimage

#imports de interface
"""from interface import interfacegraphique"""
#cet import lance une interface => a ne decommenter qu'en cas de besoin...
from interface import classinterface

#imports de robot_gopy
"""
from robot_gopy import distance_sensor
from robot_gopy import easygopigo3
from robot_gopy import gopigo3
from robot_gopy import I2C_mutex
from robot_gopy import robot2I013
from robot_gopy import setup
"""
"""les tests marchent pas sans le robot physique => manque distancesensor"""

#imports de robot_sim
from robot_sim import capteur
from robot_sim import robot2
from robot_sim import teterobot

#imports de strategies
from strategies import simulation
from strategies import strategy
from strategies import stop
from strategies import strategieCapture
from strategies import strategieCarre
from strategies import strategieObstacle
from strategies import strategieRot90
from strategies import strategieToutDroit
from strategies import strategieToutDroit70

"""ce fichier sert a tester les import depuis un script de test
    par exemple TestStrategie doit importer une strategie une simulation etc...
"""
