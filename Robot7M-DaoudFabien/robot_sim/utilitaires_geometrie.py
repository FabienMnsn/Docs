#imports

import math

#code (ceci est un utilitaire regroupant plusieurs fonctions de valcul vectoriel)

#utilitaire by _Fbn_

def produit_scalaire2D(u, v):
    """calcul le produit scalaire de u et v avec U et V vecteurs 2D (x,y)"""
    if (len(u) and len(v) == 2):
        return u[0]*v[0] + u[1]*v[1]
    else:
        return -1


def produit_scalaire3D(u, v):
    """calcul le produit scalaire de u et v avec U et V vecteurs 3D (x,y,z)
        (y etant la hauteur)"""
    if (len(u) and len(v) == 3):
        return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
    else:
        return -1


def norme_vecteur2D(u):
    """calcul la norme du vecteur 2D u = (x,y)"""
    if (len(u) == 2):
        return math.sqrt(math.pow(u[0],2) + math.pow(u[1],2))
    else:
        return -1


def norme_vecteur3D(u):
    """calcul la norme du vecteur 3D u = (x,y,z)"""
    if (len(u) == 3):
        return math.sqrt(math.pow(u[0],2) + math.pow(u[1],2) + math.pow(u[2],2))
    else:
        return -1


def calcul_angle2D(u,v):
    """calcul l'angle entre deux vecteur U et V en 2D (x,y)"""
    if (len(u) and len(v) == 2):
        det = (u[0]*v[1]-u[1]*v[0])
        angle = round(-math.degrees(math.acos( produit_scalaire2D(u,v) / (norme_vecteur2D(u) * norme_vecteur2D(v)) )), 1)
        if det < 0:
            return 360-angle
        elif det > 0:
            return angle
                
    else:
        return -1
                                
def normalise2D(u):
    """normalise le vecteur u = (x,y)"""
    if (len(u) == 2):
        return (u[0]/norme_vecteur2D(u), u[1]/norme_vecteur2D(u))
    else:
        return -1


def normalise3D(u):
    """normalise le vecteur u = (x,y,z)"""
    if (len(u) == 3):
        return (u[0]/norme_vecteur3D(u), u[1]/norme_vecteur3D(u), u[2]/norme_vecteur3D(u))
    else:
        return -1


def rotation2D(u, theta):
    """calcul la rotation du vecteur u=(x,y) de theta degres
    si theta > 0 alors rotation dans sens anti-horaire (sens trigo)
    sinon si theta < 0 rotation dans sens horaire"""
    if (len(u) == 2):
        return ( u[0]*math.cos(math.radians(theta)) - u[1]*math.sin(math.radians(theta)),
                 u[0]*math.sin(math.radians(theta)) + u[1]*math.cos(math.radians(theta)) )
    else:
        return -1


def milieu_segment(A,B):
    """calcul et retourne le milieu du segment defini par deux points A et B (x,y,z)"""
    if len(A) and len(B) == 3:
        return (A[0]+B[0]/2.0, A[1]+B[1]/2.0, A[2]+B[2]/2.0)
    if len(A) and len(B) == 2:
        return (A[0]+B[0]/2.0, A[1]+B[1]/2.0)
    else:
        return -1




