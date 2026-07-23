#File: Esercizio5.py
#
#Autore: Samuele Follin
#
#Data: 21/07/2026
#
#Descrizione: Svolgimento dell'Esercizio 5

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"'''
    dy = abs(y1 - y0)
    dx = abs(x1 - x0) 
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti'''
    for c in range(col):     
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True       
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione'''
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False 
    return True 



import random
import time 

def main():
    '''trova una soluzione al problema delle 8 regine e calcola il tempo impiegato'''
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
            return scacchiera                                    #aggiungo questo return perché senza da problemi con la funzione di rotazione, perché riconosce soluzione come oggetto None

#----- PUNTO 1 -----

lista_tempi = []                                                 #voglio raggruppare tutti i tempi in una lista

for i in range(10):
    start = time.time()                                          #assegno il tempo di inizio per ognuna delle 10 iterazioni
    main()
    lista_tempi.append(time.time() - start)                      #aggiungo ogni tempo alla lista

print(sum(lista_tempi) / 10, 'è il tempo medio.\n')                #faccio la media dei tempi sommandoli tra loro e dividendo per 10

#----- PUNTO 2 -----

lista_tentativi = []                                             #creo una lista in cui inserire i tentativi

def accumula_tentativi():                                        #funzione simile alla main, ma aggiunge tutti i tentativi dentro la lista prima di trovare la soluzione
    '''Risolve il problema delle 8 regine e aggiunge tutti i tentativi in una lista'''
    random_generator = random.Random() 
    scacchiera = list(range(8))           
    solutions = 0
    while solutions < 1:
        tentativo = random_generator.shuffle(scacchiera)         #ogni permutazione è un tentativo
        lista_tentativi.append(tentativo)                        #ogni tentativo aggiunge un elemento alla lista
        if soluzione_ok(scacchiera):
            solutions += 1
accumula_tentativi()
print(f'Ci sono voluti {len(lista_tentativi)} tentativi prima di trovare la soluzione.\n')

#----- PUNTO 3 -----

def main_alternativo():                                            #per comodità creo un altro main senza il calcolo del tempo per non modificare quello principale
    '''trova una soluzione al problema delle 8 regine'''
    random_generator = random.Random() 
    scacchiera = list(range(8))           
    solutions = 0
    start_time = time.time()  
    while solutions < 1:
        random_generator.shuffle(scacchiera) 
        if soluzione_ok(scacchiera): 
            solutions += 1      
            start_time = time.time()
            return scacchiera                                     
    
soluzioni = set()                                                  #grazie al return posso inserire gli elementi dentro le strutture dati, uso set perché non ammette doppioni
while len(soluzioni) < 10:
    soluzione = main_alternativo()
    soluzioni.add(tuple(soluzione))                                #serve cambiare il tipo in tupla perché i set ammettono solo oggetti non modificabili (una lista è modificabile, una tupla no)
print('soluzioni uniche:', soluzioni, '\n')

#----- PUNTO 4 -----

soluzioni = []

for i in range(10):
    soluzione = main_alternativo()
    soluzioni.append(tuple(soluzione))                                           #devo trasformare le soluzioni da aggiungere alla lista in tuple, così poi posso trasformare la lista in set

duplicati = len(soluzioni) - len(set(soluzioni))                                 #attraverso questa sottrazione ottengo i duplicati perché nei set i duplicati non ci sono
print('tra queste soluzioni:', soluzioni, 'i duplicati sono', duplicati, '\n')

#----- PUNTO 5 -----

n = int(input('Quali saranno le dimensioni della prossima scacchiera? '))                     #metto un input e impongo che sia un numero intero

def main_NxN(n):                                                                              #definisco un'altra funzione main
    '''Risolve il problema delle regine in una scacchiera N x N'''
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
print('\n')

#----- PUNTO 6 -----

tempi_brevi = []

dimensione = 8                                                 #parto da 8 per semplicità, se parto da 0 ci sono problemi con 2 e 3
while True:                                                    #ciclo infinito che viene interrotto solo dal break
    start_time = time.time()
    main_NxN(dimensione)
    tempo = time.time() - start_time                           #il tempo di ogni soluzione
    if tempo > 15:
        break                                                  #il procedimento si ferma quando c'è il promo N con tempo superiore a 15 secondi
    tempi_brevi.append(dimensione)                             #aggiungo alla lista ogni dimensione con tempo minore di 15 secondi
    dimensione += 1
print(f'Il lato N più grande possibile per cui si riesce a torvare una soluzione in meno di 15s è {tempi_brevi[-1]}')   #stampo l'ultimo elemento della lista, è quello più grande con tempo < 15

#----- PUNTO 7 -----

def rotazione_90_gradi(soluzione):
    '''calcola la rotazione di 90 gradi della soluzione'''
    rotazione = [0, 0, 0, 0, 0, 0, 0, 0]                       #inizializziamo la rotazione
    for col in range(8):
        riga = soluzione[col]                                  #passa in rassegna la riga di ogni regina (la colonna corrisponde all'indice nella lista)
        col_90 = 7 - riga                                      #7 perché in python si conta dallo 0, stiamo svolgendo una rotazione in senso orario
        riga_90 = col                                          #il nuovo valore della riga corrisponde al vecchio vaore della colonna
        rotazione[col_90] = riga_90                            #accoppiamo le nuove coordinate
    return rotazione

def tutte_le_rotazioni(soluzione):                                    #per semplicità applico ogni volta la rotazione di 90 senza creare altre 2 funzioni
    '''calcola le rotazioni di 90, 180 e 270 gradi della soluzione'''
    rotazione90 = rotazione_90_gradi(soluzione)                    
    rotazione180 = rotazione_90_gradi(rotazione90)
    rotazione270 = rotazione_90_gradi(rotazione180)
    return [soluzione, rotazione90, rotazione180, rotazione270]       #ritorna una lista contenente le rotazioni della soluzione

soluzioni_uniche = []
while len(soluzioni_uniche) < 5:
    soluzione = main_alternativo()                                    #main_alternativo perché il tempo è irrilevante
    rotazioni = tutte_le_rotazioni(soluzione)                         #con gli and controllo se la soluzione è realmente unica oppure no
    if soluzione not in soluzioni_uniche and rotazioni[1] not in soluzioni_uniche and rotazioni[2] not in soluzioni_uniche and rotazioni[3] not in soluzioni_uniche:
        soluzioni_uniche.append(soluzione)
        print('\nSoluzione unica', len(soluzioni_uniche))             #len(soluzioni_uniche) è momentaneo e corrisponde al numero della soluzione unica
        print('Soluzione:', rotazioni[0])
        print('Rotazione di 90°:', rotazioni[1])
        print('Rotazione di 180°:', rotazioni[2])
        print('Rotazione di 270°:', rotazioni[3])