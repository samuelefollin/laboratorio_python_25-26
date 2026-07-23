#File: Esercizio3.py
#
#Autore: Samuele Follin
#
#Data: 14/07/2026
#
#Versione: 1.0
#
#Descrizione: Svolgimento dell'Esercizio 3

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

#----- PUNTO 1 -----

def punto_uno():
    '''stampa a schermo delle stringhe contenenti i dati dei personaggi'''
    for personaggio in rubrica.keys():                                 #loop iterato per ogni chiave del dizionario
        print(personaggio, end = ', ')                                 #stampo prima le chiavi principali, con end = ', ' la stampa termina con virgola e spazio
        for dato in rubrica[personaggio]:                               
         print(str(dato), end = ': ')                                  #i valori dei personaggi sono altri dizionari, stampo le chiavi di questi dizionari, ossia le chiavi dei dizionari annidati
         print(str(rubrica[personaggio][dato]), end = ', ')            #stampo i valori dei dizionari annidati
         

punto_uno()
print('\n')
#----- PUNTO 2 -----

def punto_due():
    '''costruisce la lista crescente delle età'''
    lista_età = []
    for personaggio in rubrica:
        lista_età.append(rubrica[personaggio]['età'])                 #inserisco nella lista il valore di 'età', che è valore del personaggio
    lista_età.sort()                                                  #con .sort() ordino in ordine crescente
    print(lista_età)
    print('Personaggi in ordine crescente di età:')
    for anni in lista_età:                                            #prendo in rassegna la lista appena creata
        for personaggio in rubrica:                                   #prendo in rassegna i 4 personaggi del dizionario
            if rubrica[personaggio]['età'] == anni:                   #controllo per ogni personaggio se la sua età corrisponde, in caso affermativo lo stampo
             print(personaggio)

punto_due()

#----- PUNTO 3 -----

def punto_tre():
    '''costruisce la lista decrescente delle età'''
    lista_età = []
    for personaggio in rubrica:
        lista_età.append(rubrica[personaggio]['età'])
    lista_età.sort()
    lista_età_decrescente = lista_età[::-1]                          #è uno slicing, infatti [inizio, fine, passo] in questo caso è composto solo dal passo, che essendo -1 va all'indietro
    print(f'Lista delle età in ordine decrescente: {lista_età_decrescente}')

punto_tre()

#----- PUNTO 4 -----

def punto_quattro():
    '''scrive una frase personalizzata per ogni personaggio'''
    for personaggio in rubrica:                                      #prepariamo una formattazione f-string, assegnamo tutte le variabili ai valori correlati
        nome = personaggio
        giorno = rubrica[personaggio]['giorno']
        mese = rubrica[personaggio]['mese']
        anno = rubrica[personaggio]['anno']
        età = rubrica[personaggio]['età']
        mail = rubrica[personaggio]['mail']
        if rubrica[personaggio]['sesso'] == 'M':                     #dividiamo i due casi per il sesso
            sesso = 'o'
        else: sesso = 'a'

        frase = f'Car{sesso} {nome}, sei nat{sesso} il {giorno} di {mese} del {anno} e quindi a breve compirai {età} anni. Ti manderemo gli auguri per {mail}'
        print(frase)

punto_quattro()

#----- PUNTO 5 -----

import sys                                                                        #necessario per utilizzare argv

for personaggio in rubrica:
    chiave = sys.argv[1]                                                          #la chiave deve essere uguale al secondo valore della lista di argomenti (il primo è il nome del programma)
    print(f'{chiave} di {personaggio}: {rubrica[personaggio][chiave]}')           #stampa il dato della chiave per ogni personaggio

#----- PUNTO 6 -----

import argparse

parser = argparse.ArgumentParser()                       #creo una variabile e le assegno un oggetto ArgumentParser
parser.add_argument('-nome')                             #aggiungo il parametro da inserire al momento dell'esecuzione del programma
args = parser.parse_args()                               #così avviene la lettura dell'argomento

personaggio = args.nome                                  #la variabie personaggio diventa il nome indicato all'esecuzione del programma

nome = personaggio                                       #senza questo il nome all'inizio della frase è quello dell'ultimo personaggio della rubrica
giorno = rubrica[personaggio]['giorno']
mese = rubrica[personaggio]['mese']
anno = rubrica[personaggio]['anno']
età = rubrica[personaggio]['età']
mail = rubrica[personaggio]['mail']
if rubrica[personaggio]['sesso'] == 'M':                     
    sesso = 'o'
else: sesso = 'a'
frase = f'Car{sesso} {nome}, sei nat{sesso} il {giorno} di {mese} del {anno} e quindi a breve compirai {età} anni. Ti manderemo gli auguri per {mail}'
print(frase)

#----- PUNTO 7 -----

def punto_cinque(dato):                                               #creo la funzione con parametro per il punto 5
    for personaggio in rubrica:
        print(f'{dato} di {personaggio}: {rubrica[personaggio][dato]}')

parser  = argparse.ArgumentParser()
parser.add_argument('-punto_uno', action = 'store_true')              #aggiungo i vari parser, action = store_true serve alle funzioni che non necessitano un valore nella chiamata
parser.add_argument('-punto_due', action = 'store_true')
parser.add_argument('-punto_tre', action = 'store_true')
parser.add_argument('-punto_quattro', action = 'store_true')
parser.add_argument('-punto_cinque')                                 #nel caso del quinto punto è necessario un valore di fianco a -punto_cinque nella chiamata
args = parser.parse_args()
if args.punto_uno:                                                   #verrà eseguito l'if del punto indicato
    punto_uno()
elif args.punto_due:
    punto_due()
elif args.punto_tre:
    punto_tre()
elif args.punto_quattro:
    punto_quattro()
elif args.punto_cinque:
    punto_cinque(args.punto_cinque)
