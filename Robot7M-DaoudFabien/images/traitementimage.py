#imports

from PIL import Image
import time
import operator
import random
#code
#resultats des test (jugement a l oeil nu)

"""
def detection_carre(img,x,y,couleur,zone):
    for i in range(x,x+zone):
        for j in range(y,y+zone):
            if (img.getpixel((i,j)) == couleur):
                
                #print("pixel trouve",couleur)
                return True
    return False


test 4 couleurs minimum~> (7/11 images detectees)
test 3 couleusr minimum ~>(11/11 images detectees)
test detection des 4 zones de couleur entiere ou presque ~> (6/11 detectees)

fic0 = "ImageCopie.jpg"
"""

def traitement_image(image):
    """traite une image et cherche une balise
    return True si une balise a ete trouvee, False sinon"""
    #for i in range(0,len(liste_fic)):
    #img = Image.open(liste_fic[i]+".jpg")

    img = Image.open(image+".jpg")

    COEF_FENETRE_RECHERCHE = 80 
    TAUX = 20 #en pourcent
    TAUX_CONVERTED = TAUX*255/100 #conversion pourcent en valeur pixel

    cptR = 0
    cptG = 0
    cptB = 0
    cptY = 0
    l = []
    taille_carre = 10
    for x in range(img.size[0]-taille_carre):
        for y in range(img.size[1]-taille_carre):
            r,g,b,c = img.getpixel((x+taille_carre,y)) # Vert
            r2,g2,b2,c2 = img.getpixel((x+taille_carre,y+taille_carre)) # Bleu
            r3,g3,b3,c3 = img.getpixel((x,y+taille_carre)) # Rouge
            r4,g4,b4,c4 = img.getpixel((x,y)) # Jaune
            
            liste_couleur = [("r",r),("g",g),("b",b)] # Vert
            liste_couleur2 = [("r",r2),("g",g2),("b",b2)] # Bleu
            liste_couleur3 = [("r",r3),("g",g3),("b",b3)] # Rouge
            liste_couleur4 = [("r",r4),("g",g4),("b",b4)] # Jaune
            
            liste_couleur.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste
            liste_couleur2.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste
            liste_couleur3.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste
            liste_couleur4.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste

            test_rouge = liste_couleur3[0][0] == "r" and liste_couleur3[0][1] > liste_couleur3[1][1] + TAUX_CONVERTED
            test_vert = liste_couleur3[0][0] == "r" and liste_couleur3[0][1] > liste_couleur3[1][1] + TAUX_CONVERTED
            test_bleu = liste_couleur2[0][0] == "b" and liste_couleur2[0][1] > liste_couleur2[1][1] + TAUX_CONVERTED
            test_jaune = liste_couleur4[0][1] > 210 and (liste_couleur4[0][0] == "r" or liste_couleur4[0][0] == "g") and liste_couleur4[0][1] - liste_couleur4[1][1] < TAUX_CONVERTED and liste_couleur4[1][1] > liste_couleur4[2][1] + TAUX_CONVERTED

            if ( test_rouge and test_vert and test_bleu and test_jaune):
                #print('Balise trouvee')
                #img.putpixel((x+(taille_carre//2),y+(taille_carre//2)),(255,0,255)) # pixel violet pour reperer le centre 
                #img.show() 
                return ((x+(taille_carre//2),y+(taille_carre//2)), (img.size[0], img.size[1])) # coordonnées du centre

    return -1 # valeur qui indique qu'aucune balise n'a ete trouvee

            #ceci est une ancienne version bcp trop longue (en temps de calcul)
    """if(liste_couleur3[0][0] == "r" and liste_couleur3[0][1] > liste_couleur3[1][1] + TAUX_CONVERTED): # Rouge
            #print("dominante rouge")
                img.putpixel((x,y),(255,0,0))
                cptR += 1
            elif(liste_couleur3[0][0] == "r" and liste_couleur3[0][1] > liste_couleur3[1][1] + TAUX_CONVERTED): # Vert
                #print("dominante vert")
                img.putpixel((x,y),(0,255,0))
                cptG += 1
            elif(liste_couleur2[0][0] == "b" and liste_couleur2[0][1] > liste_couleur2[1][1] + TAUX_CONVERTED): # Bleu
                #print("dominante bleu")
                img.putpixel((x,y),(0,0,255))
                cptB += 1
            elif(liste_couleur4[0][1] > 210 and # Jaune
                 (liste_couleur4[0][0] == "r" or
                  liste_couleur4[0][0] == "g")and
                 liste_couleur4[0][1] - liste_couleur4[1][1] < TAUX_CONVERTED and
                 liste_couleur4[1][1] > liste_couleur4[2][1] + TAUX_CONVERTED):
                img.putpixel((x,y),(255,255,0))
                cptY += 1 
                
    #affichage nb pxl R, V, B, J            
    #print("rouge:",cptR,"vert:",cptG,"bleu:",cptB,"jaune:",cptY)
    
    #mise en commentaire temporaire...


    #DETECTION DE LA BALISE QUI MARCHE :)
    #le carre d'observation est une subdivision entiere de l'image ~> 1/10

    TAILLE = 40
    #TAILLE_Y = img.size[1]//10
    ZONE_DETEC = 5
    for x in range(0, img.size[0]-TAILLE):
        for y in range(0, img.size[1]-TAILLE):
            if detection_carre(img,x,y,(255,255,0),ZONE_DETEC) :
                if detection_carre(img,x+TAILLE-ZONE_DETEC,y,(0,255,0),ZONE_DETEC) :
                    if detection_carre(img,x+TAILLE-ZONE_DETEC,y+TAILLE-ZONE_DETEC,(0,0,255),ZONE_DETEC) :
                        if detection_carre(img,x,y+TAILLE-ZONE_DETEC,(255,0,0),ZONE_DETEC) :
                            img.putpixel( (x+TAILLE-3,y+TAILLE-3),(255,0,255))
                            img.show()
                            img.close()
                            return (x+TAILLE-3,y+TAILLE-3)
    return (-1, -1) #return (-1,-1) si l'ago ne trouve pas de balise     """               



if __name__ == '__main__':
    
    print(traitement_image('screen'))
    
    #liste des differentes images pour tester plusieur detetction de couleurs (temporaire)
    """liste_fic = [
            "2018-03-06 02_51_06.486124",
            "2018-03-06 02_51_13.082451",
            "2018-03-06 02_51_18.273973",
            "2018-03-06 02_51_23.256724",
            "2018-03-06 02_51_28.118059",
            "2018-03-06 02_51_43.625168",
            "2018-03-06 02_51_48.413961",
            "2018-03-06 02_51_54.161908",
            "2018-03-06 02_52_18.483662",
            "Image",
            "ImageCopie"]

    #test du traitement image:
    for picture in liste_fic:
        t = traitement_image(picture)
        print(t)"""
    #lien utile pour les valeurs RGB des pixels de l'image : https://www.imagecolorpicker.com/

