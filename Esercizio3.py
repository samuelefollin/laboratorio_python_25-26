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

#-----------------------------------------------

def punto_uno():
    for personaggio in rubrica.keys():
        print(str(personaggio), end = ', ')                               #stampo prima le chiavi principali, con end = ', ' la stampa termina con virgola e spazio
        for dato in rubrica[personaggio]:                               
         print(str(dato), end = ': ')                                  #stampo i valori delle chiavi personaggi, ossia le chiavi delle liste annidate
         print(str(rubrica[personaggio][dato]), end = ', ')            #stampo i valori delle chiavi delle liste annidate

punto_uno()
#------------------------------------------------

def punto_due():
    lista_età = []
    for personaggio in rubrica:
        lista_età.append(rubrica[personaggio]['età'])                 #inserisco nella lista il valore di 'età', che è valore del personaggio
    lista_età.sort()                                                  #con .sort() ordino in ordine crescente
    print(lista_età)
    for anni in lista_età:                                            #prendo in rassegna la lista appena creata
        for personaggio in rubrica:                                   #prendo in rassegna i 4 personaggi del dizionario
            if rubrica[personaggio]['età'] == anni:                   #se il valore dell'età del personaggio è uguale al valore nella lista, stampo il nome del personaggio
             print(personaggio)

punto_due()
#-------------------------------------------------

def punto_tre():
    lista_età = []
    for personaggio in rubrica:
        lista_età.append(rubrica[personaggio]['età'])
    lista_età_decrescente = lista_età[::-1]                           #slicing di passo -1 e di inizio-fine nulli
    print(lista_età_decrescente)

punto_tre()
#-------------------------------------------------

def punto_quattro():
    for personaggio in rubrica:                                      #prepariamo una formattazione f-strings, assegnamo tutte le variabili ai valori correlati
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
#---------------------------------------------------

'''import sys                                                    #necessario per utilizzare argv

for personaggio in rubrica:
    chiave = sys.argv[1]                                      #la chiave deve essere uguale al secondo valore della lista di argomenti (il primo è il nome del programma)
    print(rubrica[personaggio][chiave])'''

#----------------------------------------------------

import argparse

'''parser = argparse.ArgumentParser()                       #creo una variabile e le assegno un oggetto ArgumentParser
parser.add_argument('-nome')                             #aggiungo il parametro da inserire al momento dell'esecuzione del programma
args = parser.parse_args()                               #così avviene l lettura dell'argomento

personaggio = args.nome                                 #la variabie personaggio diventa il nome indicato all'esecuzione del programma

nome = personaggio                                      #senza questo il nome all'inizio della frase è quello dell'ultimo personaggio della rubrica
giorno = rubrica[personaggio]['giorno']
mese = rubrica[personaggio]['mese']
anno = rubrica[personaggio]['anno']
età = rubrica[personaggio]['età']
mail = rubrica[personaggio]['mail']
if rubrica[personaggio]['sesso'] == 'M':                     
    sesso = 'o'
else: sesso = 'a'
frase = f'Car{sesso} {nome}, sei nat{sesso} il {giorno} di {mese} del {anno} e quindi a breve compirai {età} anni. Ti manderemo gli auguri per {mail}'
print(frase)'''

#----------------------------------------------------
def punto_cinque(dato):                                               #trasformo i punti precedenti in funzioni, per il 5° punto creo una funzione a parte con parametro 
    for persona in rubrica:
        print(rubrica[persona][dato])

parser  = argparse.ArgumentParser()
parser.add_argument('-punto_uno', action = 'store_true')              #aggiungo i vari parser, action = store_true serve alle funzioni che non necessitano un valore nella chiamata
parser.add_argument('-punto_due', action = 'store_true')
parser.add_argument('-punto_tre', action = 'store_true')
parser.add_argument('-punto_quattro', action = 'store_true')
parser.add_argument('-punto_cinque')                                 #nel caso del quinto punto è necessario un valore di fianco a -punto_cinque nella chiamata
args = parser.parse_args()
if args.punto_uno:
    punto_uno()
if args.punto_due:
    punto_due()
if args.punto_tre:
    punto_tre()
if args.punto_quattro:
    punto_quattro()
if args.punto_cinque:
    punto_cinque(args.punto_cinque)
