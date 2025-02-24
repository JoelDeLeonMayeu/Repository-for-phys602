# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
#Hmmm this code is in french, I'll start updating it to english

#Function to draw spirograph-like patern
def Spirographe(R,r,d,phi=0, color='k'):
    
    #lists to host coordinates of points of curve
    x=[]
    y=[]
    
    #dummy variable for now
    m=1
    
    #
    while True:
        
        #Verification that the user-inserted data are valid
        if r>1000 or R>1000 or d>1000:
            print('Erreur: données trop larges')
            n=0
            break
        
        #Equation to solve to find n
        n=r/(R-r)*m
        
        #If n in an integer stop
        if n%1==0:
            break
        
        #If n isnt an integer continue
        else:
            m+=1
            
    #
    n=int(n)
    
    #Arrays now because old me's reflex was to use lists
    x=np.array(x)
    y=np.array(y)
    
    #
    theta=0
    for i in range(360*n+1):
        theta+=1
        
        #création de mes tableaux de coordonées des points
        #à "plot"
        x=np.append(x,(R-r)*np.cos(np.radians(theta))+\
                    d*np.cos(np.radians(-(R-r)/r*theta+phi)))
        y=np.append(y,(R-r)*np.sin(np.radians(theta))+\
                    d*np.sin(np.radians(-(R-r)/r*theta+phi)))
            
    #la dernière étape de la fonction est de faire appel 
    #à la fonction "plot" pour dessiner nos courbes
    plt.plot(x,y,color)


#J'avais mal compris ce qui m'était demandé au début et donc,
#je croyais qu'il fallait que j'écrive un code qui demande
#directemenet à l'utilisatateur comment il souhaite "plot"
#son dessin. J'ai donc gardé cette fonction en commentaire
#ici comme vestige de mon travail additionnel/accidentel      

#while True:
#   print('Bienvenu dans ce simulateur de spirographe.')
#    stop=input("Souhaitez-vous ajouter une courbe? Si non,\
# tapez 'True'. Si oui, tapez autre chose, n'importe quoi!")
#    if stop=='True':
#        break
#    r=input('Entrez votre valeur de r')
#    R=input('Entrez votre valeur de R')
#    d=input('Entrez votre valeur de d')
#    r=float(r)
#    R=float(R)
#    d=float(d)
#    qcolor=input("Si vous souhaitez une couleur, \
# tapez 'oui'").upper
#    if qcolor=='OUI':
#        colorarg=input("Tapez votre couleur")
#        Spirographe(r,R,d,color==colorarg)
#        plt.axis('equal')
#    else:
#        Spirographe(r,R,d)
#        plt.axis('equal')
        

#Commandes pour créer le dessin demandé
Spirographe(240,100,80, color='midnightblue')
Spirographe(252,105,80, color='royalblue', phi=20)
Spirographe(264,110,80, color='yellowgreen', phi=40)
Spirographe(252,105,80, color='royalblue', phi=60)
Spirographe(60,35,20, color='olive')
Spirographe(70,15,10, color='midnightblue')

#Les axes seront gradués de la même manière (pas d'effet
#"étiré")
plt.axis('equal')

#Les axes disparaissent du dessin
plt.axis('off')

plt.savefig('spirographe.png')
