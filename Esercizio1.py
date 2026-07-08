print('Quanti numeri vuoi testare?')
tentativi = input()
tentativi = int(tentativi)
print('Ottimo, inizia pure')


n = input()
n = int(n)                      # l'input è un numero intero

def is_pari(n):
    if int(n) % 2 == 0:         #se il resto della divisione è uguale a zero
        return True
    else:
        return False
    
#----------------------------------------------

def is_positivo(n):
    while int(n) <= 0:          #uso while perché è un loop con condizione
        n = int(input())             #impongo di continuare a inserire n finché n è positivo

    return n        

#-----------------------------------------------

def genera_lista(n):
    lista = [n]                                #così mette gli elemnti tra parentesi[], con n dentro [] impone che il primo numero della lista sia n
    while n != 1 and len(lista) <= 100:       #appena una delle due condizioni viene smentita il processo si ferma
        if int(n) % 2 == 0:
            n = int(int(n) / 2)
        else:
            n = int(int(n) * 3 + 1)           
        lista.append(n)                       #così continua a generare elementi della lista
    return lista                        

#-----------------------------------------------

lista = genera_lista(n)                       #in questo modo la funzione nuova agisce sulla lista di quella vecchia, non serve riscriverlo dopo 

def analizza_sequenza(lista):
    return max(lista), len(lista), sum(lista)

#-----------------------------------------------

def ricerca(lista):
    for i in lista:
        if i % 5 == 0:
            print(i)
    if all(i % 5 != 0 for i in lista):                                    #l'if va messo fuori dal for, se no stampa il messaggio per ogni numero non multiplo di 5
        print('Non sono presenti numeri divisibili per 5')

#-------------------------------------------------

lunghezza_massima = 0                                                       #inizializzo: do un valore di partenza alla lunghezza massima
numero_migliore = 0                                                         #inizializzo: do un valore di partenza al numero migliore

for i in range(0, tentativi):                                               #così ripete le funzioni il numero di volte che ha detto l'utente all'inizio                                                      
    print(is_pari(n))
    n = is_positivo(n)                                                   #chiamo la funzione e salvo il valore generato dalla funzone di positività
    lista = genera_lista(n)                                              #in questo modo genera sempre nuove liste, se no studia sempre e solo la prima
    print(genera_lista(n))                                            
    print(analizza_sequenza(lista))                                      #mostra la lunghezza il massimo e la somma dei valori nella lista
    ricerca(lista)                                                       #mostra tutti i numeri nella lista divisibili per 5 altrimenti da messaggio non ci sono numeri divisibili per 5
    if len(lista) > lunghezza_massima:
        lunghezza_massima = len(lista)                                      #con questo if aggiorno la lunghezza massima e il numero migliore a essa associato
        numero_migliore = n
    if i < tentativi - 1:                                                   #senza questo chiederebbe un input per poi ignorarlo e dire che hai finito i tentativi
        print('Prossimo numero?')
        n = int(input())
    lista = genera_lista(n)
    
    
print('Hai finito i tentativi. Il numero iniziale che ha generato la sequenza più lunga è il:', numero_migliore)