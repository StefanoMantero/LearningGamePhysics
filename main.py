
from random import randint,random #random
#import ga
raggio=20 
vento= 0.01;
gravity = 0.98;
attrito = -0.9; ## 10*=-0.1 e` -1 quindi numero minore piu` attrito.
x=100 # Posizione inziale della sfera
y=100 # Posizione inziale della sfera
preso=False 
vel_x=0 #Velocita` di x
vel_y=0 #Velocita` di y
quanti=4
oggetti=[]
done=False
toggle=False
count=0
tryit=[]
def setup():
    global bg
    textSize(18)
    bg = loadImage("bg.jpg")
    frameRate(60);
    #create_random_stuff()
    create_level()
    size(1240,660) 
    frameRate(800)
    for _ in range(1000):
        tryit.append([randint(0,1)])
#Draw the entire game
def draw():
    global x,y,vento,gravity,attrito,count,toggle
    image(bg, 0, 0) #Buffer del background
    stroke(200) #Colori bordi della palla
    move()
    collision() #Funzione per muovere
    gm_grab() #Grabbing the sfera
    fill(123,213,250,1)
    ellipse(x,y,raggio*2,raggio*2) #Disegno la mia palla
    #Ciclo per la list di oggetti
    for oggetto in oggetti:
        fill(oggetto[4],oggetto[5],oggetto[6],oggetto[7])
        rect(oggetto[0],oggetto[1],oggetto[2],oggetto[3])
    _text="Vento: "+str(vento)+" Km/h  "+"- Morbidezza:  "+str(abs(attrito))+"- Gravita`: "+str(gravity)+" g"+"- x: "+str(x)+" y:"+str(y)
    text(_text, 80, 20) #Scritte
    if count<len(tryit):
        print(tryit[count])
        if tryit[count]:
            print("yolo")
            gravity*=-1
    elif count>len(tryit):
        restart()
    count+=1
    finish()



def finish():
    global done
    if not done:
        for oggetto in oggetti:
            if oggetto[6]!=250:
                return False
        print(count)
        done=True

def keyPressed():
    global vento,gravity,oggetti,done,toggle
    if key == CODED:
        if keyCode == RIGHT:
            vento+=0.01
        elif keyCode == LEFT:
            vento-=0.01
        elif keyCode == UP:
            gravity*=-1
        elif keyCode == DOWN:
            del oggetti[:]
            done=False
            #create_random_stuff()
            restart()

def restart():
    global x,y,vel_x,vel_y,count
    x=100 # Posizione inziale della sfera
    y=100 # Posizione inziale della sfera
    preso=False
    count=0
    vel_x=0 #Velocita` di x
    vel_y=0 #Velocita` di y
    del oggetti[:]
    create_level()
#Funzione per prendere la sfera e muoverla in giro
def gm_grab():
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

def create_random_stuff():
    for _ in range(quanti):
        oggetti.append([randint(0,width),randint(0,height),randint(15,width-300),randint(15,height-600),123,213,123,250])

def create_level():
    oggetti.append([80,300,300,50,123,213,123,250])
    oggetti.append([250,400,300,50,123,213,123,250])
    oggetti.append([450,100,300,50,123,213,123,250])
    oggetti.append([150,height-100,50,50,123,213,123,250])
    oggetti.append([width-200,height-100,100,50,123,213,123,250])


def move():
    global x,y,vel_x,vel_y
    vel_y+=gravity ##Aggiungo gravita`
    vel_x+=vento
    x+=vel_x#Sommo la posizione con la velocita`
    y+=vel_y

def collision():
    global x,y,vel_x,vel_y,attrito 

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
            ellipse(max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])),10,10)
            line(x,y,max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])))
            if (DeltaX * DeltaX + DeltaY * DeltaY) < (raggio*raggio):
                oggetto[6]=250 #Cambio il colore se collide
                #Debug
                print(DeltaX,DeltaY)
                #Quando tocca nel lato sinistro
                if DeltaX<DeltaY  and DeltaX<raggio/2 and DeltaX!=0 and DeltaY<=-raggio:
                    print("Lato sinistro")
                    x=oggetto[0]-raggio-1 #Posizione esatta pavimento
                    vel_x*=attrito #Inverto usando morbidezza {(attrito) -0.3}
                #Quando tocca nel lato destro
                elif DeltaX>DeltaY  and DeltaX>raggio/2 and DeltaX!=0 and DeltaY<=raggio:
                    print("Lato destro")
                    x=(oggetto[0]+oggetto[2])+raggio+1 #Posizione esatta pavimento
                    vel_x*=attrito #Inverto usando morbidezza {(attrito) -0.3}          
                #Quando tocca il lato superiore
                elif DeltaY<DeltaX and (DeltaX>=0 or x+raggio>=oggetto[0]):
                    print("Lato superiore")
                    y=oggetto[1]-raggio
                    vel_y*=attrito
                #Quando tocca il lato inferiore
                elif DeltaY>DeltaX and DeltaX<=0 :
                    print("Lato inferiore")
                    y=(oggetto[1]+oggetto[3])+raggio
                    vel_y*=attrito
