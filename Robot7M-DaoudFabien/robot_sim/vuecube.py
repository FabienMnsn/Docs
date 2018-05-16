#imports

import pyglet
from pyglet.gl import *
from basiques.cube import *

#code

class VueCube:
    def __init__(self, cube):
        if isinstance(cube, Cube):

            self.batch = pyglet.graphics.Batch()

            texture_file = "robot_sim/textures/crate.png"
            tex = pyglet.image.load(texture_file).texture
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
            view = pyglet.graphics.TextureGroup(tex)
            view_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))

            
            colorf1 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf2 = ('c3f', (0.65, 0.65, 0.65,) * 4)
            colorf3 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf4 = ('c3f', (0.55, 0.55, 0.55,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.45, 0.45, 0.45,) * 4)
            # faces
            # f1
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2)),
                           view_coords)
            # f2
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2)),
                           view_coords)
            # f3
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2)),
                           view_coords)
            # f4
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2)),
                           view_coords)
            # f5
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2)),
                           view_coords)
            # f6
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (cube.x - cube.larg/2,
                        cube.y,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long,
                        cube.z - cube.haut/2)),
                           view_coords)
