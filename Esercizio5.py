def stessa_diagonale(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0) 
    return dx == dy     


def incrocia_colonne(posizioni, col):
    for c in range(col):     
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True       
    return False   


def soluzione_ok(soluzione_posizioni):
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False 
    return True 



import random
import time 

def main():
    random_generator = random.Random() 
    scacchiera = list(range(8))           
    solutions = 0
    start_time = time.time()  
    while solutions < 1:
        random_generator.shuffle(scacchiera) 
        if soluzione_ok(scacchiera): 
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
            solutions += 1      
            start_time = time.time()
            return scacchiera                                   #aggiungo questo return perché senza da problemi con la funzione di rotazione, perché riconosce soluzione come oggetto None

#------------------------------------------------------------------------

lista_tempi = []                                                 #voglio raggruppare tutti i tempi in una lista

for i in range(10):
    start = time.time()                                          #resetto il tempo di inizio per ognuna delle 10 iterazioni
    main()
    lista_tempi.append(time.time() - start)                      #aggiungo ogni tempo alla lista

print(sum(lista_tempi) / 10, 'è il tempo medio')                 #faccio la media dei tempi sommandoli tra loro e dividendo per 10

#--------------------------------------------------------------------------

lista_tentativi = []                                             #creo una lista in cui inserire i tentativi

def accumula_tentativi():                                        #funzione simile alla main, ma aggiunge tutti i tentativi dentro la lista prima di trovare la soluzione
    random_generator = random.Random() 
    scacchiera = list(range(8))           
    solutions = 0
    while solutions < 1:
        tentativo = random_generator.shuffle(scacchiera)         #ogni permutazione è un tentativo
        lista_tentativi.append(tentativo)                        #ogni tentativo aggiunge un elemento alla lista
        if soluzione_ok(scacchiera):
            solutions += 1
accumula_tentativi()
print(f'Ci sono voluti {len(lista_tentativi)} tentativi prima di trovare la soluzione')

#--------------------------------------------------------------------------

def main_alternativo():                                      #creo un altro main per non modificare quello principale
    random_generator = random.Random() 
    scacchiera = list(range(8))           
    solutions = 0
    start_time = time.time()  
    while solutions < 1:
        random_generator.shuffle(scacchiera) 
        if soluzione_ok(scacchiera): 
            solutions += 1      
            start_time = time.time()
            return scacchiera                                      #rimuovo print e lo sostituisco con un return che mi rende una copia della soluzione
    


soluzioni = set()                                                   #grazie al return posso inserire gli elementi dentro le strutture dati, uso set perché non ammette doppioni
while len(soluzioni) < 10:
    soluzione = main_alternativo()
    soluzioni.add(tuple(soluzione))                                 #serve cambiare il tipo in tupla perché i set ammettono solo oggetti non modificabili (una lista è modificabile, una tupla no)
print('soluzioni uniche:', soluzioni)

#------------------------------------------------------------------------------

soluzioni = []

for i in range(10):
    soluzione = main_alternativo()
    soluzioni.append(tuple(soluzione))                                                 #devo trasformare le soluzioni da aggiungere alla lista in tuple, così poi posso trasformare la lista in set

duplicati = len(soluzioni) - len(set(soluzioni))                                       #attraverso questa sottrazione ottengo i duplicati perché nei set i duplicati non ci sono
print('tra queste soluzioni:', soluzioni, 'i duplicati sono', duplicati)

#--------------------------------------------------------------------------------

n = int(input('Quali saranno le dimensioni della prossima scacchiera? '))                                                                              #metto un input e impongo che sia un numero intero
def main_NxN(n):                                                                              #definisco un'altra funzione main
    random_generator = random.Random()                                                        
    scacchiera = list(range(n))                                                               #la scacchiera diventa NxN
    solutions = 0
    start_time = time.time()  
    while solutions < 1:
        random_generator.shuffle(scacchiera) 
        if soluzione_ok(scacchiera): 
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
            solutions += 1      
            start_time = time.time()
main_NxN(n)

#-----------------------------------------------------------------------------------
tempi_brevi = []

dimensione = 8                                                 #parto da 9 per semplicità, se parto da 0 ci sono problemi con 2 e 3
while True:                                                    #ciclo infinito che viene interrotto solo dal break
    start_time = time.time()
    main_NxN(dimensione)
    tempo = time.time() - start_time                           #il tempo di ogni soluzione
    if tempo > 15:
        break                                                  #il procedimento si ferma quando c'è il promo N con tempo superiore a 15 secondi
    tempi_brevi.append(dimensione)                             #aggiungo alla lista ogni dimensione con tempo minore di 15 secondi
    dimensione += 1
print(f'Il lato N più grande possibile per cui si riesce a torvare una soluzione in meno di 15s è {tempi_brevi[-1]}')      #stampo l'ultimo elemento della lista, è quello più grande con tempo < 15

#-------------------------------------------------------------------------------------

def rotazione_90_gradi(soluzione):
    rotazione = [0, 0, 0, 0, 0, 0, 0, 0]                       #inizializziamo la rotazione
    for col in range(8):
        riga = soluzione[col]                                  #passa in rassegna la riga di ogni regina (la colonna corrisponde all'indice nella lista)
        col_90 = 7 - riga                                      #7 perché in python si conta dallo 0
        riga_90 = col                                          #il nuovo valore della riga corrisponde al vecchio vaore della colonna
        rotazione[col_90] = riga_90                            #accoppiamo le nuove coordinate
    return rotazione

def tutte_le_rotazioni(soluzione):                             #per semplicità applico ogni volta la rotazione di 90 senza creare altre 2 funzioni
    rotazione90 = rotazione_90_gradi(soluzione)                    
    rotazione180 = rotazione_90_gradi(rotazione90)
    rotazione270 = rotazione_90_gradi(rotazione180)
    return [soluzione, rotazione90, rotazione180, rotazione270]       #ritorna una lista contenente le rotazioni della soluzione

tutte_le_rotazioni(soluzione)

soluzioni_uniche = []
while len(soluzioni_uniche) < 5:
    soluzione = main_alternativo()
    rotazioni = tutte_le_rotazioni(soluzione)                             #con gli and controllo se la soluzione è realmente unica oppure no
    if soluzione not in soluzioni_uniche and rotazioni[1] not in soluzioni_uniche and rotazioni[2] not in soluzioni_uniche and rotazioni[3] not in soluzioni_uniche:
        soluzioni_uniche.append(soluzione)
        print('\n Soluzione unica', len(soluzioni_uniche))
        print('Soluzione:', rotazioni[0])
        print('Rotazione di 90°:', rotazioni[1])
        print('Rotazione di 180°:', rotazioni[2])
        print('Rotazione di 270°:', rotazioni[3])