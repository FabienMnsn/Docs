#imports

import pyglet
from pyglet.gl import *
from basiques.mur import *

#code

class VueMur:
    def __init__(self, mur):
        if isinstance(mur, Mur):

            self.batch = pyglet.graphics.Batch()

            texture_file = "robot_sim/textures/wall2.png"
            tex = pyglet.image.load(texture_file).texture
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
            view = pyglet.graphics.TextureGroup(tex)
            view_coords = ('t2f',(0,0, 7,0, 7,1, 0,1, ))

            colorf3 = ('c3f', (0.5, 0, 0,) * 4)
            
            # faces
            # f1 arriere
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (mur.x + mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2)),
                           view_coords)
            # f2 dessous
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (mur.x + mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2)),
                           view_coords)
            # f3 devant
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (mur.x + mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2)),
                           view_coords)
            # f4 dessus
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2)),
                           colorf3)
            # f5
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (mur.x + mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2,
                        mur.x + mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2)),
                           view_coords)
            # f6
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (mur.x - mur.larg/2,
                        mur.y,
                        mur.z - mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z + mur.haut/2,
                        mur.x - mur.larg/2,
                        mur.y + mur.long,
                        mur.z - mur.haut/2)),
                           view_coords)
