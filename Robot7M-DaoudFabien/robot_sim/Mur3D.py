from pyglet.gl import *
from pyglet.window import key

class Cube:
    def __init__(self, sx, sy, sz, l, h, p, setcolor):
        #initialisation des variables getter self
        self.px = sx
        self.py = sy
        self.pz = sz
        self.l=l
        self.h=h
        self.p=p
        self.type = setcolor

        self.batch = pyglet.graphics.Batch()

        # ne pas confondre ces valeurs de coordonnees qui correspondent
        # aux coordonnes pour calculer les positions des sommets
        # et les coordonnees du centre du mur qui seront utilisees plus loin
        x, y, z = self.px, self.py, self.pz
        lm, hm, pm = l / 2, h / 2, p / 2

        #setcolor murs
        if(setcolor==1):
            colorf1 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.5, 0.5, 0.5,) * 4)
        """
        #setcolor cubes
        if(setcolor==2):
            colorf1 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf2 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf3 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf5 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf6 = ('c3f', (0.8, 0.8, 0.8,) * 4)
        """
        #setcolor robot
        if (setcolor == 3):
            colorf1 = ('c3f', (0.4, 0., 0.3,) * 4)
            colorf2 = ('c3f', (0.5, 0., 0.4,) * 4)
            colorf3 = ('c3f', (0.5, 0., 0.4,) * 4)
            colorf4 = ('c3f', (0.6, 0., 0.5,) * 4)
            colorf5 = ('c3f', (0.6, 0., 0.5,) * 4)
            colorf6 = ('c3f', (0.5, 0., 0.4,) * 4)

        #setcolor Sol
        if (setcolor == 4):
            colorf1 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf2 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf3 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf4 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf5 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf6 = ('c3f', (0.4, 0.4, 0.4,) * 4)

        # creation des faces
        
        # f1
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z + pm, x - lm, y - hm, z + pm, x - lm, y + hm, z + pm, x + lm, y + hm, z + pm)),
                       colorf1)
        # face avant
        
        # f2
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z + pm, x - lm, y - hm, z + pm, x - lm, y - hm, z - pm, x + lm, y - hm, z - pm)),
                       colorf2)
        # face dessous
        
        # f3
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z - pm, x - lm, y - hm, z - pm, x - lm, y + hm, z - pm, x + lm, y + hm, z - pm)),
                       colorf3)
        # face arriere
        
        # f4
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y + hm, z + pm, x - lm, y + hm, z + pm, x - lm, y + hm, z - pm, x + lm, y + hm, z - pm)),
                       colorf4)
        # face dessus
        
        # f5
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z - pm, x + lm, y - hm, z + pm, x + lm, y + hm, z + pm, x + lm, y + hm, z - pm)),
                       colorf5)
        # face cote droit
        
        #(x + lm, y - hm, z - pm, x + lm, y + hm, z + pm, x + lm, y + hm, z + pm, x + lm, y + hm, z - pm))
        
        # f6
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x - lm, y - hm, z - pm, x - lm, y - hm, z + pm, x - lm, y + hm, z + pm, x - lm, y + hm, z - pm)),
                       colorf6)
        # face cote gauche
        
    def draw(self):
        self.batch.draw()

