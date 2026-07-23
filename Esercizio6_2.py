#File: Esercizio6_2.py
#
#Autore: Samuele Follin
#
#Data: 18/07/2026
#
#Versione: 1.0
#
#Descrizione: Svolgimento dell'Esercizio 6, seconda parte

from Esercizio6_1 import Rubrica                                                       #importo la classe dall'altro file

formato = input('Vuoi lavorare in un file json oppure in un file di testo? ')
while formato not in ['file json', 'file di testo']:                                   #faccio la domanda finché non ottengo una delle due opzioni
    formato = input('Scegli, file json o file di testo? ')
if formato == 'file json':                                                             #come prima cosa faccio scegliere all'utente quale tipo di file utilizzare, da questo dipende il resto
    r = Rubrica.inizializzazione_in_json('rubrica.json')                               #metodo della classe
elif formato == 'file di testo':
    r = Rubrica.inizializzazione_in_txt('rubrica.txt')                                 #metodo della classe

scelta = ''                                                                            #applico un valore momentaneo a scelta per poter usare il ciclo while 
while scelta != 'EXIT':

    scelta = input('Quale delle operazioni della classe vuoi svolgere? ')

    if scelta == 'apri':                                                               #il metodo apri dipende dal file su cui stiamo lavorando: divido nelle due opzioni json e txt
        if formato == 'file json':
            r.apri('rubrica.json')
        elif formato == 'file di testo':
            r.apri('rubrica.txt')

    elif scelta == 'aggiungi':
        print('Inserisci il nome del personaggio')
        personaggio = input()
        dati = {}                                                     #devo creare un dizionario e inserire singolarmente i vari valori, altrimenti l'input singolo viene riconosciuto come stringa
        dati['giorno'] = int(input('Che giorno è nato/a? '))
        dati['mese'] = input('In che mese? ')
        dati['anno'] = int(input('In che anno? '))
        dati['età'] = int(input('Quanti anni ha '))
        dati['sesso'] = input('Quale è il suo sesso? ')
        dati['mail'] = input('Quale è la sua mail? ')
        r.aggiungi(personaggio, dati)

    elif scelta == 'rimuovi':
        print('Quale personaggio vuoi rimuovere?')                     #non serve creare un messaggio nel caso in cui il personaggio non sia in rubrica, lo fa già il metodo di per sè
        personaggio = input()
        r.rimuovi(personaggio)

    elif scelta == 'salva':                                            #anche qui divido nelle due opzioni json e txt
        if formato == 'file json':
            r.salva('rubrica.json')
        elif formato == 'file di testo':
            r.salva('rubrica.txt')

    elif scelta == 'stampa':
        print('Di quale personaggio vuoi stampare i dati?')               #anche qua, il metodo stampa già un messaggio nel caso in cui il personaggio non esiste
        personaggio = input()
        r.stampa(personaggio)