#imports

from PIL import Image
import time
import operator
import random
#code
#resultats des test (jugement a l oeil nu)


def detection_carre(img,x,y,couleur,zone):
    for i in range(x,x+zone):
        for j in range(y,y+zone):
            if (img.getpixel((i,j)) == couleur):
                
                #print("pixel trouve",couleur)
                return True
    return False

"""
test 4 couleurs minimum~> (7/11 images detectees)
test 3 couleusr minimum ~>(11/11 images detectees)
test detection des 4 zones de couleur entiere ou presque ~> (6/11 detectees)
"""
#fic0 = "ImageCopie.jpg"


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
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            liste_couleur = [("r",r),("g",g),("b",b)]
            #print("list:",liste_couleur)
            liste_couleur.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste
            #print("trie:",liste_couleur)
            #time.sleep(2)
            #print()
            #if(liste_couleur[0][1] > liste_couleur[1][1] + MARGE_CONVERTED):
            if(liste_couleur[0][0] == "r" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED):
                #print("dominante rouge")
                img.putpixel((x,y),(255,0,0))
                cptR += 1
            elif(liste_couleur[0][0] == "g" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED / 7):
                #print("dominante vert")
                img.putpixel((x,y),(0,255,0))
                cptG += 1
            elif(liste_couleur[0][0] == "b" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED):
                #print("dominante bleu")
                img.putpixel((x,y),(0,0,255))
                cptB += 1
            elif(liste_couleur[0][1] > 210 and
                 (liste_couleur[0][0] == "r" or
                  liste_couleur[0][0] == "g")and
                 liste_couleur[0][1] - liste_couleur[1][1] < TAUX_CONVERTED and
                 liste_couleur[1][1] > liste_couleur[2][1] + TAUX_CONVERTED):
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
    return (-1, -1) #return (-1,-1) si l'ago ne trouve pas de balise                    


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
    print(t)
#lien utile pour les valeurs RGB des pixels de l'image : https://www.imagecolorpicker.com/
"""
