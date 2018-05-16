#imports

from tkinter import *

from robot_sim.capteur import *
from robot_sim.robot2 import *
from basiques.arene import * 
from basiques.cube import * 
from basiques.mur import * 
from basiques.sol import * 

#code

class Interface:
    def __init__(self):
        #Frame.__init__(self)
        
        self.root = Tk()
        self.canvas = Canvas(self.root, bg="ivory", width=500, height=500)
        self.canvas.pack()
        ##self.root.mainloop()
        #self.frame = LabelFrame(self, text="Ceci est un LabelFrame", borderwidth=2, relief=GROOVE)
        #self.frame.pack(side=TOP, padx=5, pady=5)

        #self.canvas = Canvas(self, bg="white", width=500, height=500)
        #self.canvas.pack()
        #self.pack()
        
    def dessiner_robot(self, robot):
        #self.canvas.delete(ALL)
        #self.canvas.create_text(250,100,text="Ceci est un Canvas", fill="black", activefill="grey")
        x, y, z = robot.position
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = robot.coords
        milieu_avant_robot_xy = (((x0 + x1)/2), ((y0+y1)/2))
        long, larg, haut = robot.dimension
        dirx, diry = robot.direction
        dirtetex, dirtetey = robot.tete.orientation
        self.canvas.create_polygon(robot.coords, fill="blue")
        self.canvas.create_line((x0+x1)/2, (y0+y1)/2, ((x0+x1)/2 + dirtetex*100), ((y0+y1)/2 + dirtetey*100), fill="black", arrow='last')
        self.canvas.create_oval(milieu_avant_robot_xy[0]-4, milieu_avant_robot_xy[1]-4, milieu_avant_robot_xy[0]+4, milieu_avant_robot_xy[1]+4, fill="red")
        #print("Action:dessin robot")
        
    def dessiner_cube(self, cube):
        #if isinstance(cube, Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        self.canvas.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        self.canvas.create_text(cube.x + cube.larg / 2, cube.y + cube.long / 2, text="Cube", fill="darkgrey",activefill="black")
        #print("Action:dessin cube")
    
    def dessiner_mur(self, mur):
        #if isinstance(mur, Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
        self.canvas.create_rectangle(mur.x, mur.y, mur.x + mur.larg, mur.y + mur.long, fill="yellow")
        self.canvas.create_text(mur.x + mur.larg / 2, mur.y + mur.long / 2, text="Mur", fill="yellow", activefill="Black")
        #print("Action:dessin mur")

    def dessiner_sol(self, sol):
        self.canvas.create_rectangle(sol.x, sol.y, sol.x + sol.larg, sol.y + sol.long, fill="grey")
        self.canvas.create_text(sol.x + sol.larg / 2, sol.y + sol.long / 2, text="Sol", fill="grey", activefill="Black")
        #print("Action:dessin sol")


    def rafraichir(self, robot):
        #self.canvas.delete(ALL) 
        i = 0
        for c in robot.arene.liste_cube:
            if isinstance(c, Sol):
                self.dessiner_sol(c)
            if isinstance(c, Mur):
                self.dessiner_mur(c)
            elif isinstance(c, Cube):
                self.dessiner_cube(c)
        self.dessiner_robot(robot)


    def animate(self, robot):
        self.rafraichir(robot)
        self.after(100, animate)


        
if __name__ == '__main__':
    robot1 = Creation_Robot()
    interface = Interface()
    print(robot1.safficher())
    interface.rafraichir(robot1)
