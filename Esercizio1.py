#File: Esercizio1.py
#
#Autore: Samuele Follin
#
#Data: 18/07/2026
#
#Descrizione: Svolgimento dell'Esercizio 1


print('Quanti numeri vuoi testare?')
tentativi = int(input())
if int(tentativi) <= 0:
    print('Peggio per te...')
else:
    print('Ottimo, inizia pure.')

#----- PUNTO 1 -----

n = int(input())                                         #l'input deve essere un nmero intero

def is_pari(n):                                              #il parametro della funzione è il numero inserito in input
    '''controlla se il numero inserito è un numero pari'''
    if int(n) % 2 == 0:                                      #se il resto della divisione è uguale a zero
        return True
    else:
        return False
    
#----- PUNTO 2 -----

def is_positivo(n):
    '''controlla se l'input è un numero positivo e lo restituisce se lo è'''
    while int(n) <= 0:                                       #uso while perché è un loop con condizione
        n = int(input())                                     #finché n è negativo o zero il ciclo continua
    return n        

#----- PUNTO 3 -----

def genera_lista(n):
    '''applica la congettura di Collatz al numero e genera una lista con tutti i numeri risultanti'''
    lista = [n]                               #creo una lista che momentaneamente contiene solo l'input
    while n != 1 and len(lista) <= 100:       #appena una delle due condizioni viene smentita il ciclo si arresta
        if int(n) % 2 == 0:                   #se il numero è pari viene diviso per due
            n = int(int(n) / 2)
        else:                                 #se il numero è dispari viene moltiplicato per 3 e sommato di 1
            n = int(int(n) * 3 + 1)           
        lista.append(n)                       #in ogni caso, il numero viene aggiunto alla lista
    return lista                        

#----- PUNTO 4 -----

lista = genera_lista(n)                              #associo alla variabile lista la lista generata dal punto precedente

def analizza_sequenza(lista):
    '''definisce il massimo e la lunghezza della lista e la somma di tutti i suoi elementi'''
    return max(lista), len(lista), sum(lista)        #la funzione restituisce una tupla contenente questi tre valori

#----- PUNTO 5 -----

def ricerca(lista):
    ''' analizza la lista e stampa a schermo i valori divisibili per 5'''
    for valore in lista:
        if valore % 5 == 0:                                       #se il resto della divisione per 5 è 0 (cioè il numero è multpilo di 5)
            print(valore)
    if all(valore % 5 != 0 for valore in lista):                  #all() restituisce True se tutti i valori di un iterabile sono True, False se almeno uno è False
        print('Non sono presenti numeri divisibili per 5')        #l'if va messo fuori dal for, se no stampa il messaggio per ogni numero non multiplo di 5

#----- PUNTO 6 -----

lunghezza_massima = 0                                                    #inizializzo: do un valore di partenza alla lunghezza massima
numero_migliore = 0                                                      #inizializzo: do un valore di partenza al numero migliore

for tentativo in range(tentativi):                                       #le funzioni sono ripetute il numero di volte indicato dall'utente                                                    
    print(is_pari(n))                                                    #chiamo is_pari con il print, così il return viene stampato a schermo
    n = is_positivo(n)                                                   #chiamo la funzione is_positivo e salvo il valore generato in una variabile
    lista = genera_lista(n)                                              #in questo modo genera sempre nuove liste, se no studia sempre e solo la prima
    print(genera_lista(n))                                               #chiamo genera_lista e stampo a schermo la lista generata con return
    print(analizza_sequenza(lista))                                      #chiamo analizza_sequenza e stampo a schermo i valori (raggruppati in una tupla) del return
    ricerca(lista)                                                       #chiamo ricerca senza print perché è già all'interno della funzione
    if len(lista) > lunghezza_massima:                                   #cerco la lista più lunga, con questo if aggiorno la lunghezza massima e il numero migliore a essa associato
        lunghezza_massima = len(lista)                                   
        numero_migliore = n
    if tentativo < tentativi - 1:                                        #senza questo if chiederebbe un input per poi ignorarlo e stampare il messaggio dei tentativi esauriti
        print('Prossimo numero?')
        n = int(input())
    
    print('Hai finito i tentativi. Il numero iniziale che ha generato la sequenza più lunga è il:', numero_migliore)