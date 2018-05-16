#imports

import pyglet
from pyglet.gl import *
from basiques.balise import *

#code

class VueBalise:
    def __init__(self, balise):
        if isinstance(balise, Balise):

            self.batch = pyglet.graphics.Batch()

            texture_file = "robot_sim/textures/paper.png"
            tex = pyglet.image.load(texture_file).texture
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
            view = pyglet.graphics.TextureGroup(tex)
            view_coords = ('t2f',(0,0.6, 0.8,0.6, 0.8,0, 0,0,))
            
            h=balise.haut
            l=balise.haut * 1.5
            epaisseur = 30
            # jaune
            yellow = ('c3f', (0.9, 0.9, 0,) * 4)
            # vert
            green = ('c3f', (0, 0.9, 0,) * 4)
            # rouge
            red = ('c3f', (0.9, 0, 0,) * 4)
            # bleu
            blue = ('c3f', (0, 0, 0.9,) * 4)
            # noir
            white = ('c3f', (1, 1, 1,) * 4)
            # gris
            grey = ('c3f', (0.6, 0.6, 0.6,) * 4)
            dark_grey = ('c3f', (0.5, 0.5, 0.5,) * 4)
            
            #carre jaune
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h,
                        balise.z,
                        balise.x,
                        balise.y + h,
                        balise.z,
                        balise.x,
                        balise.y + h/2,
                        balise.z,
                        balise.x - l/2,
                        balise.y + h/2,
                        balise.z)),
                           yellow)
            #carre vert
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x,
                        balise.y + h,
                        balise.z,
                        balise.x + l/2,
                        balise.y + h,
                        balise.z,
                        balise.x + l/2,
                        balise.y + h/2,
                        balise.z,
                        balise.x,
                        balise.y + h/2,
                        balise.z)),
                           green)
            #carre bleu
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x,
                        balise.y + h/2,
                        balise.z,
                        balise.x + l/2,
                        balise.y + h/2,
                        balise.z,
                        balise.x + l/2,
                        balise.y,
                        balise.z,
                        balise.x,
                        balise.y,
                        balise.z)),
                           blue)
            #carre rouge
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h/2,
                        balise.z,
                        balise.x,
                        balise.y + h/2,
                        balise.z,
                        balise.x,
                        balise.y,
                        balise.z,
                        balise.x - l/2,
                        balise.y,
                        balise.z)),
                           red)
            
            #tranches de balise (cote R & J)
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h,
                        balise.z,
                        balise.x - l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x - l/2,
                        balise.y,
                        balise.z - epaisseur,
                        balise.x - l/2,
                        balise.y,
                        balise.z)),
                           dark_grey)
            #tranches de balise (cote J & V)
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h,
                        balise.z,
                        balise.x - l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y + h,
                        balise.z)),
                           grey)
            #tranches de balise (cote V & B)
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x + l/2,
                        balise.y + h,
                        balise.z,
                        balise.x + l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y,
                        balise.z)),
                           dark_grey)
            #tranches de balise (cote R & B)
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x + l/2,
                        balise.y,
                        balise.z,
                        balise.x + l/2,
                        balise.y,
                        balise.z - epaisseur,
                        balise.x - l/2,
                        balise.y,
                        balise.z - epaisseur,
                        balise.x - l/2,
                        balise.y,
                        balise.z)),
                           grey)
            
            #arriere de la balise
            self.batch.add(4, GL_QUADS, view, (
                'v3f', (balise.x - l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y + h,
                        balise.z - epaisseur,
                        balise.x + l/2,
                        balise.y,
                        balise.z - epaisseur,
                        balise.x - l/2,
                        balise.y,
                        balise.z - epaisseur)),
                           view_coords)
            
