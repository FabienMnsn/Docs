# Author: Miguel Martinez Lopez pour l'animation du GIF le reste By Shx

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

from Main3D import *

from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Label

from PIL import Image, ImageTk

import os
import time
import subprocess
from winsound import *


#code

class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)


#___________________________________Custom By ShX____________________________________
#____________________________________________________________________________________
def start_music():
    PlaySound('Ressource_Pack/JOYCA - High edit for robot project.wav',  SND_FILENAME | SND_ASYNC)

def stop_music():
    PlaySound(None,  SND_FILENAME | SND_ASYNC)

def QUIT():
    stop_music()
    root.destroy()
    root.quit()  

def refresh_GIF():
        AnimatedGIF(root, "Ressource_Pack/dancing-robot5.gif")

def tuto():
	tuto=Tk()
	tuto.title("Binds")
	tuto.resizable(width=False, height=False)
	Label(tuto, text="\nECHAP = Quitter la simulation 3D\nESPACE = Arret de la strategie en cours\nG = Strategie avancer de 70cm\nH = Strategie rotation90 droite\nF = Strategie rotation90 gauche\nX = Script detection de balise\nC = Strategie carre\n", foreground="white", background="#333333", anchor=CENTER, justify=CENTER).pack(side=TOP, padx=0, pady=0)
	tuto.mainloop()

def aide():
	aide=Tk()
	aide.title("Aide")
	aide.resizable(width=False, height=False)
	Label(aide, text="\nVous voici dans le lanceur de simulation\ndans lequel vous pouvez acceder a la simulation en elle meme (via le menu Simulation)\nmais aussi à d'autres informations interessantes (via les differents menu)\n", foreground="white", background="#333333", anchor=CENTER, justify=CENTER).pack(side=TOP, padx=0, pady=0)
	aide.mainloop()

def credit():
	credit=Tk()
	credit.title("Credits")
	credit.resizable(width=False, height=False)
	Label(credit, text="\nMusique ~> \"HIGH\" de Joyca\nSimulation 3D ~> Daoud & Fabien\nAnimation & texture du robot ~> Fabien\nImage issue du site officiel du GoPiGo\nCode lecteur de .GIF tkinter par Miguel Martinez Lopez\nTextures moteur 3D par Jimmy MALACHIER\n\nEncadrants\nArthur PAJOT\n Nicolas BASKIOTIS\n Vincent GUIGUE\n", foreground="white", background="#333333", anchor=CENTER, justify=CENTER).pack(side=TOP, padx=0, pady=0)
	credit.mainloop()

def bonus():
	bonus=Tk()
	bonus.title("Bonus")
	bonus.resizable(width=False, height=False)
	Label(bonus, text="\nAnnee 2017/2018\nTemps passe sur le projet depuis le debut: un peu plus de 200h\nTemps de production de l'Animation : 6h\n\nlogiciels et bibliotheques utilises :\nPython 3.4 & 3.6.4\nIdle 3.4\nGitKraken & GitHub\nTrello\nPIL\nTkinter\nPyglet(3D)\nPhotoshopCS6 (gratuit...)\nAudacity\n", foreground="white", background="#333333", anchor=CENTER, justify=CENTER).pack(side=TOP, padx=0, pady=0)
	bonus.mainloop()

def start_sim():#cette fct bug il faut relancer l'interface avant de relancer la simulation
    stop_music()
    print("ATTENTION ! cette fonction bug il faut relancer l'interface avant de relancer la simulation 3D")
    run3D()
    start_music()


#_________________________________________________SCRIPT DE LANCEMENT DU MENU 2D_________________________________________________
#________________________________________________________________________________________________________________________________
root = Tk()
root.geometry("636x424")
root.title("Robot 2i013 Alpha 3.1")
root.resizable(width=False, height=False)
start_music()

photo = PhotoImage(file="Ressource_Pack/createurs.png")
canvas = Canvas(root,  width=636, height=40, bg='white')
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(side=TOP)

l = AnimatedGIF(root, "Ressource_Pack/dancing-robot5.gif")
l.pack()

menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Lancer la simulation 3D", command=start_sim)# DONE
menu1.add_command(label="Information touches clavier (binds)", command=tuto)# DONE
menubar.add_cascade(label="Simulation", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Aide", command=aide)# DONE
menu2.add_command(label="Credits", command=credit)# DONE
menu2.add_separator()
menu2.add_command(label="Bonus content", command=bonus)# DONE

menubar.add_cascade(label="Informations", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="couper la musique", command=stop_music)
menu3.add_command(label="relancer la musique", command=start_music)
menu3.add_command(label="recharger GIF", command=refresh_GIF)
menubar.add_cascade(label="Media", menu=menu3)

menubar.add_command(label="Quitter", command=QUIT)

root.config(menu=menubar)
root.mainloop()

