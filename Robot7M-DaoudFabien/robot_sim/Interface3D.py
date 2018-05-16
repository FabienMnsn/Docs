import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay


class Cube:
    def __init__(self, sx, sy, sz, l, h, p, setcolor):
        # initialisation des coordonnees de l objet
        self.px = sx
        self.py = sy
        self.pz = sz
        # initialisation des dimensions de l objet
        self.cl = l
        self.ch = h
        self.cp = p

        self.type = setcolor

        self.batch = pyglet.graphics.Batch()

        # ne pas confondre ces valeurs de coordonnees qui correspondent
        # aux coordonnes pour calculer les positions des sommets
        # et les coordonnees du centre du mur qui seront utilisees plus loin
        x, y, z = self.px, self.py, self.pz
        lm, hm, pm = self.cl / 2, self.ch / 2, self.cp / 2

        # setcolor murs
        if (setcolor == 1):
            colorf1 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.5, 0.5, 0.5,) * 4)

        # setcolor robot
        if (setcolor == 2):
            colorf1 = ('c3f', (1., 1., 1.,) * 4)
            colorf2 = ('c3f', (0.95, 0.95, 0.95,) * 4)
            colorf3 = ('c3f', (0.90, 0.90, 0.90,) * 4)
            colorf4 = ('c3f', (0.85, 0.85, 0.85,) * 4)
            colorf5 = ('c3f', (0.80, 0.80, 0.80,) * 4)
            colorf6 = ('c3f', (0.75, 0.75, 0.75,) * 4)

        # setcolor Sol
        if (setcolor == 3):
            colorf1 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf4 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf5 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf6 = ('c3f', (0.7, 0.7, 0.7,) * 4)

        if (setcolor == 4):  # rouge ~> jaune
            colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0.9, 0.9, 0,) * 4)
        if (setcolor == 5):  # vert
            colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0, 0.9, 0,) * 4)
        if (setcolor == 6):  # bleu ~> rouge
            colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0.9, 0, 0,) * 4)
        if (setcolor == 7):  # jaune ~> bleu
            colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0, 0, 0.9,) * 4)

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

        # f6
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (x - lm, y - hm, z - pm, x - lm, y - hm, z + pm, x - lm, y + hm, z + pm, x - lm, y + hm, z - pm)),
                       colorf6)
        # face cote gauche

    def draw(self):
        self.batch.draw()

    def update_object(self):
        if self.type == 3:
            self.pz += 10


class Balise:
    def __init__(self, cx, cy, cz, size, orientation):
        bpx = cx
        bpy = cy
        bpz = cz
        self.cubesbalisel = list()

        i = 4
        if (orientation == 'c'):

            while i <= 7:
                if i == 4:
                    self.cubesbalisel.append(Cube(bpx, bpy + (size / 4), bpz - (size / 4), 2, size / 2, size / 2, i))
                elif i == 5:
                    self.cubesbalisel.append(Cube(bpx, bpy + (size / 4), bpz + (size / 4), 2, size / 2, size / 2, i))
                elif i == 6:
                    self.cubesbalisel.append(Cube(bpx, bpy - (size / 4), bpz - (size / 4), 2, size / 2, size / 2, i))
                elif i == 7:
                    self.cubesbalisel.append(Cube(bpx, bpy - (size / 4), bpz + (size / 4), 2, size / 2, size / 2, i))
                i += 1
        else:
            while i <= 7:
                if i == 4:
                    self.cubesbalisel.append(Cube(bpx - (size / 4), bpy + (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 5:
                    self.cubesbalisel.append(Cube(bpx + (size / 4), bpy + (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 6:
                    self.cubesbalisel.append(Cube(bpx - (size / 4), bpy - (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 7:
                    self.cubesbalisel.append(Cube(bpx + (size / 4), bpy - (size / 4), bpz, size / 2, size / 2, 2, i))
                i += 1


# creation d'une fenetre
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # attributs qui serviront pour la simu
        self.frame_rate = 1 / 600.0
        fps_display = FPSDisplay(self)
        fps_display.label.font_size = 20

        self.set_minimum_size(100, 100)  # securite

        # methodes et variables propres
        self.listcube = list()
        # self.listrobot = list()
        self.w = args[0]
        self.h = args[1]
        self.INDROT = 2
        self.INDTRSLT = 20

        # methodes et variables de champ fenetre
        glClearColor(0.7, 0.2, 0.5, 1)

        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    xRotation = yRotation = zRotation = 5

    # methodes pour le rafraichissement de l affichage du robot
    def update(self, dt):
        for e in self.listcube:
            e.update_object()

    def addcube(self, x, y, z, h, l, p, setcolor):
        self.listcube.append(Cube(x, y, z, h, l, p, setcolor))
        self.on_draw()

    def addbalise(self, x, y, z, size, orientation):
        self.listcube = self.listcube + Balise(x, y, z, size, orientation).cubesbalisel

    # definition de la methode de dessin des vues sur la fenetre
    def on_draw(self):
        # type: () -> object
        # Push Matrix onto stack
        glPushMatrix()

        self.clear()
        i = 0
        while i < len(self.listcube):
            self.listcube[i].draw()
            i += 1

        # Pop Matrix off stack
        glPopMatrix()

    def on_resize(self, w, h):

        # set the Viewport
        glViewport(0, 0, w, h)
        # width gere "l'applatissement" horizontale du cube, height le vertical
        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = w / h
        gluPerspective(50, aspectRatio, 1, 4000)
        # premier argument gere le rapprochement du cube de la camera

        # repositionnement de la camera par rapport au robot
        eyex, eyey, eyez = 0, 70, 70
        visex, visey, visez = 0, 0, 0
        for o in self.listcube:
            if o.type == 2:
                # glTranslatef(o.px, o.py, o.pz-(o.cp/2))
                eyex, eyey, eyez = o.px, o.py, o.pz - (o.cp / 2)
                visex, visey, visez = o.px, o.py, o.pz - o.cl
        """gluLookAt(
            eyex, eyey, eyez,  # eye
            visex, visey, visez,  # lookAt
            0.0, 1.0, 0.0)  # up
        """
        #vue temporaire pour voir larene des le debut
        gluLookAt(
            0, 100, 400,  # eye
            0, 0, 0,  # lookAt
            0.0, 1.0, 0.0)  # up
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_key_press(self, symbol, modifiers):
        
        if symbol == key.LEFT:
            glRotatef(self.yRotation, 0, self.INDROT, 0)
        elif symbol == key.RIGHT:
            glRotatef(self.yRotation, 0, -self.INDROT, 0)
        elif symbol == key.Q:  # vers la gauche
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(self.INDTRSLT, 0, 0)
                self.listcube[i].px += self.INDTRSLT
                i += 1
        elif symbol == key.D:  # vers la droite
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(-self.INDTRSLT, 0, 0)
                self.listcube[i].px -= self.INDTRSLT
                i += 1
        
        elif symbol == key.P:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, self.INDTRSLT)
                self.listcube[i].pz += self.INDTRSLT
                i += 1
        elif symbol == key.M:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, -self.INDTRSLT)
                self.listcube[i].pz -= self.INDTRSLT
                i += 1

        # action screenshot
        elif symbol == key.V:

            pyglet.image.get_buffer_manager().get_color_buffer().save('screen.png')


            
if __name__ == "__main__":
    newwindow = Window(720, 480, "Arene Virtuelle", resizable=False)
    #la taille de la fenetre est importante pour le screenshot et le traitement d'image potentiels bugs...
    #C = Cube(0,0,0,400,300,20,1)

    newwindow.addcube(0, 0, 0, 10000, 0, 20000,3) #SOL
    #newwindow.addcube(0, 0, 0, 400, 300, 20,1)
    #newwindow.addcube(200, 0, 200, 20, 300, 400,4)
    #newwindow.addcube(200, 0, 600, 20, 300, 400,1)
    newwindow.addcube(0, 25, 50, 50, 50, 50, 2) #robot
    newwindow.addbalise(0, 50, 0, 100, "f")  # pour les mur de face en z
    newwindow.addbalise(-100, 50, 200, 100, "c")
    
    pyglet.clock.schedule_interval(newwindow.update, newwindow.frame_rate)
    pyglet.app.run()

# ps: lien utile: http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/graphics.html

