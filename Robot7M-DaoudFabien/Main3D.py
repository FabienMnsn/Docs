#imports

from interface.interface3D import *

from basiques.cube import *
from basiques.mur import *
from basiques.balise import *
from basiques.sol import *
from basiques.arene import *
from robot_sim.robot2 import *

from strategies.simulation import *
from strategies.strategieToutDroit70 import *
from strategies.strategieRot90 import *

#code

def run3D():
        main = Window(720, 480, "Arena", resizable=True)

        #setup environnement (arene et ses composants)
        a = Arene(8000,800,8000,[],[]) # en changeant les 3 premieres valeurs on modifie la taille de l'arene
        a.generateur_arene()

        b = Balise(0,0,-2000,500)

        r = Creation_Robot(500,500,1,0)

        c0 = Cube(500,0,500,100,100,100)
        c1 = Cube(2000,0,2500,400,400,400)
        a.ajouter_cube(c0)
        a.ajouter_cube(c1)


        # setup des vue 3D
        main.addVueArene(a)
        main.addVueRobot(r)
        main.addVueBalise(b)
        #main.addStrat(strat70)

        #setup position camera
        main.eye = (0,7000,0)
        main.lookat = (0,100,0)
        main.up = (0,0,-1)
        main.delta_update = 3
        #RUN GENERAL
        pyglet.app.run()
