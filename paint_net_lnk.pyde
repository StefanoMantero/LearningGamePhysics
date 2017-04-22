from random import randint,random #random
from operator import add #Per usare add (perazione su lambda)->reduce((lambda x, y: x + y), [1, 2, 3, 4])
import functools #Per usare reduce (functools.reduce)
from collections import namedtuple
#Definisco degli individui (membri della popolazione)
preso=False
massa=1.95
raggio=18
quanti=3
location=[]
gravity=[]
velocity=[]
ogetti=[]
count=0
vento=0.000
collisione=False

def setup():
    global bg
    bg = loadImage("bg.jpg")
    size(1240,660);
    location.append([50,80]) #Posizione iniziale
    velocity.append([0,0]) #Velocita` iniziale
    gravity.append([0,0.4]) #Gravita`
    #for _ in range(quanti):
        #ogetti.append([randint(0,width),randint(0,height),randint(15,width-300),randint(15,height-600),123,213,123,250] )
    textSize(18)
    ogetti.append([30,100,100,height,123,213,123,250] )
    ogetti.append([100,500,300,height,123,213,123,250] )
    ogetti.append([300,300,100,100,123,213,123,250] )





def draw():
    physics_moves()
    grabbed()
    check_collision()
    fill(150)
    image(bg, 0, 0)
    _text="Vento: "+str(vento)+" m/s  "+"- Massa:  "+str(massa)+" Kg  "+"- Gravita`: "+str(gravity[0][1])+" g"
    text(_text, 80, 20)
    stroke(200)
    ellipse(location[0][0],location[0][1],raggio*2,raggio*2)
    for oggetto in ogetti:
        fill(oggetto[4],oggetto[5],oggetto[6],oggetto[7])
        rect(oggetto[0],oggetto[1],oggetto[2],oggetto[3])
    
        

def keyPressed():
    global vento
    if key == CODED:
        if keyCode == RIGHT:
            vento+=0.002
        elif keyCode == LEFT:
            vento-=0.002
      #Se collide
        '''
        0------------------------
        |   <=ball<=
        |   -------  #La sua x deve essere compresa tra x,x+width dell`oggeto
        |   |     |  #La sua y deve essere compresa tra y,y+height dell`oggetto
        |   -------
        |
        |
        |
        ''' 
def check_collision():
    global collisione
    #Controllo collisione
    for oggetto in ogetti:   
        if location[0][0]+raggio>=oggetto[0]+1 and location[0][0]<=oggetto[0]+oggetto[2]+raggio and location[0][1]+raggio>=oggetto[1]-1 and location[0][1]<=oggetto[1]+oggetto[3]+raggio:
            oggetto[4]=255 #Cambio il colore se collide
            collisione=True 
            #Controllo dove sto facendo collisione, se sono
            if location[0][0]+raggio>=oggetto[0] and location[0][0]-raggio<=oggetto[0]+oggetto[2] and location[0][1]+raggio/2>oggetto[1] and location[0][1]-raggio/2<oggetto[1]+oggetto[3]:
                velocity[0][0]*=-1*massa/2 #inverti coordinate
            else:
               velocity[0][1]*=-1*massa/2 #inverti coordinate
            
    if location[0][0]+raggio > width or location[0][0]-raggio < 0 :
        velocity[0][0]*=-1*massa/2 #Moltiplico -1 per invertier andamento
        #velocity[0][0]*=massa
    #Quando tocca il terreno    
    if location[0][1] > height-raggio:
        velocity[0][1]*=-0.5 #Inverto l`andamento con velocita` * -massa                        
        
##################
def physics_moves():
    global peso,raggio,count
    location[0][0]+=velocity[0][0]
    location[0][1]+=velocity[0][1] #Aggiorno asse y *0.1 for slowmotion
    #Aggiorno la velocita` (aggiungendo la gravita`)
    velocity[0][0]+=gravity[0][0]+vento #Aggiorno asse x + n se voglio vento 
    velocity[0][1]+=gravity[0][1] # Aggiungo atrito per fermarlo
    cursor(CROSS) #Cursore croce
    #Per il tetto    
    #if location[0][1] < 0+raggio:
     #   velocity[0][1]=velocity[0][1]*-massa
      #  location[0][1] = 0+raggio
      
#############################################
def grabbed():
    global preso
    if  mouseX>location[0][0]-raggio and mouseX<location[0][0]+raggio and mouseY>location[0][1]-raggio and mouseY<location[0][1]+raggio or preso:
        cursor(HAND)
        if mousePressed:
            preso=True
            location[0][0]=mouseX
            location[0][1]=mouseY
            noCursor()
            velocity[0][1]=0
            velocity[0][0]=0
        else:
            preso=False