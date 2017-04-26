from random import randint,random #random
from operator import add #Per usare add (perazione su lambda)->reduce((lambda x, y: x + y), [1, 2, 3, 4])
import functools #Per usare reduce (functools.reduce)
#Definisco degli individui (membri della popolazione)
popolo = 100
gpersona =100
minimo = 0
bersaglio=400
graziati = 0.05
mutati = 0.02
restano = 0.5
massimo = bersaglio
Popolazione = []

                        #PRE EVOLUTION (Setting up the population)
############################################################################
def individui(lunghezza,minimo,massimo):
    return[randint(minimo,massimo) for x in range(lunghezza)]

def popolazione(quanti,lunghezza,minimo,massimo):
    print('\nCreo una popolazione di: ',quanti,' elementi con lunghezza di : ',lunghezza)
    return[individui(lunghezza,minimo,massimo) for _ in range(quanti)]

def printpop(howmany,howmuch,minimo,massimo):
    Popolazione=popolazione(howmany,howmuch,minimo,massimo)
    count=0
    for x in Popolazione:
        #print("Individuo numero[",count,"] ",x)
        count=count+1
    return Popolazione
#Funzione che controlla qunto un individuo della popolazione sia vicino al risultato
def fitness(individuo,bersaglio):
    somma = functools.reduce(add, individuo, 0) #reduce(operazione sulla lista,lista,valore iniziale)
    #Faccio meno somma cosi che il fitness piu\ piccolo si avvicina di piu al risultato
    return abs(bersaglio-somma) #Valore assoluto


def grado(popolazione,bersaglio):
    #Trovo la media di fitness per la popolazione
    somma = functools.reduce(add,(fitness(individui,bersaglio) for individui in popolazione),0) #Sommo ogni elemento della poplazione
    return somma/(len(popolazione)*1.0)


############################################################################



                                #EVOLUTION
############################################################################

def evoluzione(popolazione,bersaglio,restano,graziati,mutati):
    #Ordino la mia popolazione
    promossi=[(fitness(individuo,bersaglio),individuo) for individuo in popolazione] #Setto una lista con (fitness,individuo)
    promossi=[individuo[1] for individuo in sorted(promossi)] #La sorto e ricreo lla lista con solo l`individuo (Quindi sorto gli individui grazie al fitness(che essendo all`inizio permette il corretto sorting))
    rimangono = int(len(promossi)*restano) ## Calcolo quandi ne devo prendere
    rimasti = promossi[:rimangono] #Prendo tot dal fondo perche` erano sortati crescenti
    
    #Prendo un 0.05 random
    for individuo in promossi[rimangono:]:
        if graziati > random():
            rimasti.append(individuo)

    #Prendo i mutati
    for individuo in rimasti:
        if mutati>random():
            dove_mutare=randint(0,len(individuo)-1)
            individuo[dove_mutare] = randint(minimo,massimo)


    #Mischio i rimasti per fare altri figli.
    nuoviFigli=len(Popolazione)-len(rimasti) #Trovo quanti ne devo fare
    figlo=[]
    while len(figlo) < nuoviFigli:  #Sino a quando non ho ripopolato
        maschio= randint(0,len(rimasti)-1) 
        femmina= randint(0,len(rimasti)-1)
        if maschio!=femmina:  #spero sempre
            maschio=rimasti[maschio]  
            femmina=rimasti[femmina]
            half=int(len(maschio)/2)
            bambino=maschio[:half]+femmina[half:]
            figlo.append(bambino)

    rimasti.extend(figlo)
    return rimasti


############################################################################

##FROM HERE ONLY PRINT
Popolazione = printpop(popolo,gpersona,minimo,massimo)
generazione=1
trovato=None
while not trovato:
    generazione=generazione+1
    print("Generazione: ",generazione)
    for individuo in Popolazione:
        result=functools.reduce(add, individuo, 0)
        if result == bersaglio:
            print("Trovato",bersaglio)
            prescelto=individuo
            trovato=1
            break
#Faccio un'altra generazione
    Popolazione = evoluzione(Popolazione,bersaglio,restano,graziati,mutati) 

print("Generazione: ",generazione)
print("Individuo cazzuto: ",prescelto)
print("Grado: ",grado(Popolazione,bersaglio))

