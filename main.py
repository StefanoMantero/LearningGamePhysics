from random import randint,random #random
from operator import add #Per usare add (perazione su lambda)->reduce((lambda x, y: x + y), [1, 2, 3, 4])
import functools #Per usare reduce (functools.reduce)
import ga
bot=True
popolo = 1000 #Una pallina
minimo = 0
massimo = 100
graziati = 0.05 #Graziati per generazione
mutati = 0.02 #Mutati per generazione
restano = 0.5 #Rimanenti per generazione
Popolazione = []
raggio=20  #Raggio pallina
vento= 0.01 
gravity = 0.98
attrito = -0.6 ## 10*=-0.1 e` -1 quindi numero minore piu` attrito.
##Macro orribile
x=0 
y=1
vel_x=2 #Velocita` di x
vel_y=3 #Velocita` di y
grav=4
##Fine macro orribile
palline=[]
preso=False 
scelta=False
quanti=4 #Quanti ostacoli random (Se create_random_stuff e` on)
oggetti=[] 
done=False #Finito?
frame_count=0
gpersona = 700 #Numero di frame che deve usare per battere il livello
tryit=[]



def setup():
    global bg
    textSize(18)
    bg = loadImage("bg.jpg")
    frameRate(60);
    create_random_stuff(scelta) 
    size(1240,660) 
    frameRate(60)
    print(sys.argv)
    if bot:
        create_bot_balls()
#Draw the entire game
def draw():
    global x,y,vento,gravity,attrito,frame_count
    image(bg, 0, 0) #Buffer del background
    stroke(200) #Colori bordi della palla
    move()
    collision() #Funzione per muovere
    gm_grab() #Grabbing the sfera
    fill(123,213,250,1)
    if bot:
        for pallina in palline:
            ellipse(pallina[0],pallina[1],raggio*2,raggio*2)
    else:
        ellipse(x,y,raggio*2,raggio*2) #Disegno la mia palla
    #Ciclo per la list di oggetti
    for oggetto in oggetti:
        fill(oggetto[4],oggetto[5],oggetto[6],oggetto[7])
        rect(oggetto[0],oggetto[1],oggetto[2],oggetto[3])
    _text="Vento: "+str(vento)+" Km/h  "+"- Morbidezza:  "+str(abs(attrito))+"- Gravita`: "+str(gravity)+" g"+"- x: "+str(x)+" y:"+str(y)
    text(_text, 80, 20) #Scritte

    # if frame_count<len(tryit):
    #     print(tryit[frame_count])
    #     if tryit[frame_count]==[1]:
    #         print("yolo")
    #         gravity*=-1
    # elif frame_count>len(tryit):      
    #     restart()
    frame_count+=1

def create_bot_balls():
    for _ in range(popolo):
        palline.append([randint(0,width),randint(0,height),0,0,gravity])
    if bot:
        Popolazione = ga.printpop(popolo,gpersona,minimo,massimo)
        print(Popolazione)

#actionlistener
def keyPressed():
    global vento,gravity,oggetti,done
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
            create_random_stuff(scelta)
            restart()

#Funzione per prendere la sfera e muoverla in giro
def gm_grab():
    global preso
    for pallina in palline:
        if  mouseX>pallina[x]-raggio and mouseX<pallina[x]+raggio and mouseY>pallina[y]-raggio and mouseY<pallina[y]+raggio:
            cursor(HAND)
            if mousePressed:
                preso=True
                pallina[x]=mouseX
                pallina[y]=mouseY
                pallina[vel_x]=0
                pallina[vel_y]=0
                noCursor()
            else:
                preso=False

def create_random_stuff(random):
    if random:        
        for _ in range(quanti):
            oggetti.append([randint(0,width),randint(0,height),randint(15,width-300),randint(15,height-600),123,213,123,250])
    else:
        oggetti.append([80,300,300,50,123,213,123,250])
        oggetti.append([250,400,300,50,123,213,123,250])
        oggetti.append([450,100,300,50,123,213,123,250])
        oggetti.append([150,height-100,50,50,123,213,123,250])
        oggetti.append([width-200,height-100,100,50,123,213,123,250])

def move():
    for pallina in palline:
        pallina[vel_y]+=pallina[grav]
        pallina[vel_x]+=vento
        pallina[x]+=pallina[vel_x]
        pallina[y]+=pallina[vel_y]


def collision():
    global attrito
    for pallina in palline:
        if (pallina[x])+raggio>width: #Se tocca destra
            pallina[x]=width-raggio #Posizione esatta pavimento
            pallina[vel_x]*=attrito #Inverto usando morbidezza {(attrito) -0.3}
        elif pallina[x]-raggio<0: #Se tocca sinistra
            pallina[x]=raggio #
            pallina[vel_x]*=attrito #Same as before
        if pallina[y]+raggio > height: #Pavimento
            pallina[y]=height-raggio
            pallina[vel_y]*=attrito  
        elif pallina[y]-raggio <0: #Tetto
            pallina[y]=raggio
            pallina[vel_y]*=attrito
        for oggetto in oggetti:   
           
            # Surprisingly or not, rectangle-circle collisions are not all too different 
            # - first you find the point of rectangle that is the closest to the circle' center, and check that point is in the circle.
            # And, if the rectangle is not rotated, finding a point closest to the circle' 
            # center is simply a matter of clamping the circle' center coordinates to rectangle coordinates:
            
            DeltaX = pallina[x] - max(oggetto[0], min(pallina[x], oggetto[0] + oggetto[2]))
            DeltaY = pallina[y] - max(oggetto[1], min(pallina[y], oggetto[1] + oggetto[3]))
            #In case of debug
            # ellipse(max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])),10,10)
            # line(x,y,max(oggetto[0], min(x, oggetto[0] + oggetto[2])),max(oggetto[1], min(y, oggetto[1] + oggetto[3])))
            if (DeltaX * DeltaX + DeltaY * DeltaY) < (raggio*raggio):
                oggetto[6]=250 #Cambio il colore se tocca
                #Debug
                #print(DeltaX,DeltaY)
                #Quando tocca nel lato sinistro
                if DeltaX<DeltaY  and DeltaX<raggio/2 and DeltaX!=0 and DeltaY<=-raggio:
                    #print("Lato sinistro")
                    pallina[x]=(oggetto[0]-raggio)-1
                    pallina[vel_x]*=attrito #Inverto usando morbidezza {(attrito) -0.3}
                #Quando tocca nel lato destro
                elif DeltaX>DeltaY  and DeltaX>raggio/2 and DeltaX!=0 and DeltaY<=raggio:
                    #print("Lato destro")
                    pallina[x]=(oggetto[0]+oggetto[2])+raggio+1 
                    pallina[vel_x]*=attrito #Inverto usando morbidezza {(attrito) -0.3}          
                #Quando tocca il lato superiore
                elif DeltaY<DeltaX and (DeltaX>=0 or pallina[x]+raggio>=oggetto[0]):
                    #print("Lato superiore")
                    pallina[y]=oggetto[1]-raggio
                    pallina[vel_y]*=attrito
                #Quando tocca il lato inferiore
                elif DeltaY>DeltaX and DeltaX<=0 :
                    #print("Lato inferiore")
                    pallina[y]=(oggetto[1]+oggetto[3])+raggio
                    pallina[vel_y]*=attrito