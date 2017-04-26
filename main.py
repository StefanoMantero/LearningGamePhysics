
from random import randint,random #random
raggio=25 
vento= 0.01;
gravity = 0.98;
attrito = -0.7; ## 10*=-0.1 e` -1 quindi numero minore piu` attrito.
x=100 # Posizione inziale della sfera
y=100 # Posizione inziale della sfera
preso=False 
vel_x=0 #Velocita` di x
vel_y=0 #Velocita` di y
quanti=4
oggetti=[]

def setup():
    global bg
    textSize(18)
    bg = loadImage("bg.jpg")    
    createstuff()
    size(1240,660)  
        

#Draw the entire game
def draw():
    global x,y,vento,gravity,attrito
    image(bg, 0, 0) #Buffer del background
    fill(150) #Colore palla
    stroke(200) #Colori bordi della palla
    muoviti_and_collision() #Funzione per muovere
    grabbed() #Grabbing the sfera  
    ellipse(x,y,raggio*2,raggio*2) #Disegno la mia palla
    #Ciclo per la list di oggetti
    for oggetto in oggetti:
        fill(oggetto[4],oggetto[5],oggetto[6],oggetto[7])
        rect(oggetto[0],oggetto[1],oggetto[2],oggetto[3])
    _text="Vento: "+str(vento)+" Km/h  "+"- Morbidezza:  "+str(abs(attrito))+"- Gravita`: "+str(gravity)+" g"+"- x: "+str(x)+" y:"+str(y)
    fill(200)
    text(_text, 80, 20) #Scritte



def keyPressed():
    global vento,gravity,oggetti
    if key == CODED:
        if keyCode == RIGHT:
            vento+=0.01
        elif keyCode == LEFT:
            vento-=0.01
        elif keyCode == UP:
            gravity*=-1
        elif keyCode == DOWN:
            del oggetti[:]
            createstuff()

#Funzione per prendere la sfera e muoverla in giro
def grabbed():
    global preso,x,y,vel_y,vel_x
    if  mouseX>x-raggio and mouseX<x+raggio and mouseY>y-raggio and mouseY<y+raggio or preso:
        cursor(HAND)
        if mousePressed:
            preso=True
            x=mouseX
            y=mouseY
            vel_y=0
            vel_x=0
            noCursor()
        else:
            preso=False
def createstuff():
    for _ in range(quanti):
        oggetti.append([randint(0,width),randint(0,height),randint(15,width-300),randint(15,height-600),123,213,123,250])

def muoviti_and_collision():
    global x,y,vel_x,vel_y,attrito 
    vel_y+=gravity ##Aggiungo gravita`
    vel_x+=vento
    x+=vel_x#Sommo la posizione con la velocita`
    y+=vel_y

    if x+raggio>width: #Se tocca destra
        x=width-raggio #Posizione esatta pavimento
        vel_x*=attrito #Inverto usando morbidezza {(attrito) -0.3}
    elif x-raggio<0: #Se tocca sinistra
        x=raggio #
        vel_x*=attrito #Same as before
    if y+raggio > height: #Pavimento
        y=height-raggio
        vel_y*=attrito  
    elif y-raggio <0: #Tetto
        y=raggio
        vel_y*=attrito
    #Controllo collisione
    for oggetto in oggetti:   
            '''
            Surprisingly or not, rectangle-circle collisions are not all too different 
            - first you find the point of rectangle that is the closest to the circle' center, and check that point is in the circle.
            And, if the rectangle is not rotated, finding a point closest to the circle' 
            center is simply a matter of clamping the circle' center coordinates to rectangle coordinates:
            '''
            DeltaX = x - max(oggetto[0], min(x, oggetto[0] + oggetto[2]))
            DeltaY = y - max(oggetto[1], min(y, oggetto[1] + oggetto[3]))
            #In case of debug
            #ellipse(max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])),10,10)
            #line(x,y,max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])))
            if (DeltaX * DeltaX + DeltaY * DeltaY) < (raggio*raggio):
                oggetto[4]=255 #Cambio il colore se collide
                collisione=True
                #Debug
                print(DeltaX,DeltaY)
                #Quando tocca nel lato sinistro
                if DeltaX<DeltaY  and DeltaX<=-raggio/1.5 and DeltaY==0 :
                    print("Lato sinistro")
                    x=oggetto[0]-raggio-1 #Posizione esatta pavimento
                    vel_x*=attrito #Inverto usando morbidezza {(attrito) -0.3}
                #Quando tocca nel lato destro
                elif DeltaX>DeltaY  and DeltaX>=raggio/1.5 and DeltaY==0:
                    print("Lato destro")
                    x=(oggetto[0]+oggetto[2])+raggio+1 #Posizione esatta pavimento
                    vel_x*=attrito #Inverto usando morbidezza {(attrito) -0.3}          
                #Quando tocca il lato superiore
                elif DeltaY<DeltaX and DeltaX==0:
                    print("Lato superiore")
                    y=oggetto[1]-raggio
                    vel_y*=attrito
                #Quando tocca il lato inferiore
                elif DeltaY>DeltaX and DeltaX==0:
                    print("Lato inferiore")
                    y=(oggetto[1]+oggetto[3])+raggio
                    vel_y*=attrito
                #Controllo dove sto facendo collisione, se sono
                #if x+raggio>=oggetto[0] and x-raggio<=oggetto[0]+oggetto[2] and y+raggio>oggetto[1] and y-raggio<oggetto[1]+oggetto[3]:
                    #vel_x*=attrito #Same as before
                #else:
                    #y=oggetto[1]-raggio
                    #vel_y*=attrito  
