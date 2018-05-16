#imports

import pyglet
from pyglet.gl import *
from basiques.sol import *

#code

class VueSol:
    def __init__(self, sol):
        if isinstance(sol, Sol):

            self.batch = pyglet.graphics.Batch()
            nb_texture = 10
            texture_file = "robot_sim/textures/pierre.png"
            tex = pyglet.image.load(texture_file).texture
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)#GL_REPEAT
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)#GL_LINEAR
            view = pyglet.graphics.TextureGroup(tex)
            view_coords = ('t2f',(0,0, nb_texture,0, nb_texture,nb_texture, 0,nb_texture, ))

            """data = pyglet.image.load(texture_file).get_image_data()
            texture = glGenTextures(1,data)
            glBindTexture(GL_TEXTURE_2D, texture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, (image_width), (image_height), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)"""
            
            #sol
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (sol.x - sol.larg/2,
                        sol.y,
                        sol.z - sol.haut/2,
                        sol.x - sol.larg/2,
                        sol.y,
                        sol.z + sol.haut/2,
                        sol.x + sol.larg/2,
                        sol.y,
                        sol.z + sol.haut/2,
                        sol.x + sol.larg/2,
                        sol.y,
                        sol.z - sol.haut/2)),
                           view_coords)
