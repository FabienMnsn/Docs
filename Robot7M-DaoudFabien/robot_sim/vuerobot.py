#imports

import pyglet
from pyglet.gl import *
from robot_sim.robot2 import *

#code

class VueRobot:
    def __init__(self, robot_att):

        self.robot = robot_att
        #print("(%.0f, %.0f, %.0f)"%(self.robot.position[0],self.robot.position[1],self.robot.position[2]))
        #position = self.robot.getPosition() + self.robot.getDimension()
        #dimension = (position[3], position[4], position[5])
        
        self.batch = pyglet.graphics.Batch()

        texture_fileR = "robot_sim/textures/right2.png"
        texture_fileF = "robot_sim/textures/front.png"
        texture_fileT = "robot_sim/textures/top.png"
        texture_fileB = "robot_sim/textures/back.png"
        
        tex1 = pyglet.image.load(texture_fileR).texture
        tex2 = pyglet.image.load(texture_fileF).texture
        tex3 = pyglet.image.load(texture_fileT).texture
        tex4 = pyglet.image.load(texture_fileB).texture
        
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        
        view1 = pyglet.graphics.TextureGroup(tex1)
        view2 = pyglet.graphics.TextureGroup(tex2)
        view3 = pyglet.graphics.TextureGroup(tex3)
        view4 = pyglet.graphics.TextureGroup(tex4)
        
        view_coordsR = ('t2f',(0,0, 1,0, 1,0.92, 0,0.92, ))
        view_coordsL = ('t2f',(1,0, 0,0, 0,0.92, 1,0.92, ))
        view_coordsF = ('t2f',(0,1, 1,1, 1,0, 0,0, ))
        view_coordsT = ('t2f',(0,1, 1,1, 1,0, 0,0, ))
        view_coordsB = ('t2f',(0,1, 1,1, 1,0, 0,0, ))
        
        
        colorf1 = ('c3f', (1., 1., 1.,) * 4)
        colorf2 = ('c3f', (0.95, 0.95, 0.95,) * 4)
        colorf3 = ('c3f', (1, 0, 0,) * 4)
        colorf4 = ('c3f', (0.8, 0, 0,)*2 +(0.85, 0.85, 0.85,) * 2)
        colorf5 = ('c3f', (0.80, 0.80, 0.80,) * 4)
        colorf6 = ('c3f', (0.75, 0.75, 0.75,) * 4)

        # faces
        # f1 arriere
        self.batch.add(4, GL_QUADS, view4, (
            'v3f', (self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2])),
                       view_coordsB)

        # f2 dessous
        #print(type(robot))
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2],
                    self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2],
                    self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2])),
                       colorf2)

        # f3 avant
        self.batch.add(4, GL_QUADS, view2, (
            'v3f', (self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2])),
                       view_coordsF)

        # f4 dessus
        self.batch.add(4, GL_QUADS, view3, (
            'v3f', (self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2])),
                       view_coordsT)

        # f5 cote droit
        self.batch.add(4, GL_QUADS, view1, (
            'v3f', (self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2])),
                       view_coordsR)

        # f6 cote gauche
        self.batch.add(4, GL_QUADS, view1, (
            'v3f', (self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2],
                    self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2])),
                       view_coordsL)
