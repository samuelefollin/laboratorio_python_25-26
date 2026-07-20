#File: Esercizio2.py
#
#Autore: Samuele Follin
#
#Data: 20/07/2026
#
#Descrizione: Svolgimento dell'Esercizio 2


testo_originale = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#----- PUNTO 1 -----

lista_righe = testo_originale.splitlines()                       #in questo modo divido il testo in righe (separatore:\n), le righe vengono inserite automaticamente in una lista
lista_righe_piene = []                                           

for riga in lista_righe:
    if riga != '':
      lista_righe_piene.append(riga)                             #se la riga non è vuota allora viene aggiunta alla lista di righe piene

print(len(lista_righe_piene))                                    #quantità di elementi della lista nonché numero di righe non vuote


#----- PUNTO 2 -----

lista_parole = testo_originale.split()                           #in questo modo isolo ogni parola del testo (separatore: ''), le parole vengono inserite automaticamente in una lista
print(len(lista_parole))

#----- PUNTO 3 -----

lista_caratteri_alfanum = [lettera for lettera in testo_originale if lettera.isalnum()]      #così studia tutti i caratteri e mette dentro la lista quelli alfanumerici, è una list comprehension
print(len(lista_caratteri_alfanum))

#----- PUNTO 4 -----

let = input('Scegli una lettera: ')
conteggio_lettera = []

for lettera in testo_originale:                                  #'lettera' è l'indice, questo loop for analizza tutte le lettere del testo originale
   if let == lettera:
      conteggio_lettera.append(lettera)                          #se la lettera analizzata in questione è uguale all'input, essa viene messa nella lista

print(len(conteggio_lettera))

#----- PUNTO 5 -----

testo_1 = testo_originale
parole_da_sostituire = ['day', 'Day', 'about', 'About', 'water', 'Water']       #creo una lista con le parole da sostituire
for parola in parole_da_sostituire:
    testo_1 = testo_1.replace(parola, 'PYTHON')                                 #testo_1 diventa testo_1 con PYTHON al posto della parola in questione

print(testo_1)

#----- PUNTO 6 -----

testo_2 = testo_originale.split()            #testo_2 al momento è la lista di parole del testo originale
for i, parola in enumerate(testo_2):         #con enumerate tengo traccia degli indici, assegna un indice per ogni elemento (parola) della lista
    if i % 2 != 0:
        testo_2[i] = parola.upper()          #sostituisco nel testo (lista) parola con PAROLA grazie a .upper() nelle posizioni dispari

testo_2 = " ".join(testo_2)                  #.join() compatta gli elementi di un iterabile in una stringa, quindi ricostruisco il testo, con " " metto gli spazi tra le parole
print(testo_2)

#----- PUNTO 7 -----

testo_3 = testo_originale.splitlines()
testo_3.reverse()                       #uso .reverse(), che inverte l'ordine degli elementi in una lista
testo_3 = "\n".join(testo_3)            #ricostruisco il testo, con separatore "\n" vado a capo a ogni riga
print(testo_3)

#----- PUNTO 8 -----

testo_4 = testo_originale.splitlines()
for i, verso in enumerate(testo_4):
    if i == 2 or i == 7 or i == 12 or i == 17:          #sono le posizioni corrispondenti ai versi numero due di ogni strofa
        testo_4[i] = verso[::-1]                        #è uno slicing, infatti [inizio, fine, passo] in questo caso è composto solo dal passo, che essendo -1 va all'indietro

testo_4 = "\n".join(testo_4)
print(testo_4)

#----- PUNTO 9 -----

strofe = testo_originale.split("\n\n")                #divido il testo in strofe, che sono distanziate da un doppio \n
liste_parole = []

for strofa in strofe:
    parole = set(strofa.split())                      #creo un set per ogni strofa con al suo interno le parole della strofa, i set non contengono duplicati
    liste_parole.append(parole)                       #aggiungo i 4 set dentro la lista

parole_comuni = set.intersection(*liste_parole)       #con * (operatore di unpacking) l'intersezione viene fatta tra tutti gli elementi della lista, cioè tutti e 4 i set di parole

print(parole_comuni)

#----- PUNTO 10 -----

for i in range(len(lista_parole)):                       #algoritmo di insertion sort, la lista_parole è quella del punto 2
    key = lista_parole[i]                                #creo una variabile chiave
    j = i - 1                                            #creo un altro puntatore
    while j >= 0 and len(lista_parole[j]) > len(key):    #finché la parola che precede la parola interessata è più lunga,
        lista_parole[j + 1] = lista_parole[j]            #scambio le due parole
        j = j - 1                                        #e decremento j
    lista_parole[j + 1] = key 
lista_parole_ordinate = lista_parole                     #per comodità creo una nuova lista di parole ordinate 
print(lista_parole_ordinate)

#----- PUNTO 11 -----

lista_caratteri = list(testo_originale)              #in questo modo divido il testo in singoli caratteri, ora all'interno di una lista
dizionario = {}                                      #creo il dizionario
for carattere in lista_caratteri:
    occorrenza = lista_caratteri.count(carattere)    #conto l'occorrenza per ogni carattere
    dizionario[carattere] = occorrenza               #assegno a ogni chiave 'carattere' il suo corrispettivo valore 'occorrenza'
print(dizionario)

#----- PUNTO 12 -----

lista_caratteri_minuscoli = list(testo_originale.lower())           #in questo modo tutte le lettere sono minuscole e raggruppate in una lista

dizionario = {}
for carattere in lista_caratteri_minuscoli:
    if carattere.isalnum():                                         #considera solo i caratteri alfanumerici
        occorrenza = lista_caratteri_minuscoli.count(carattere)
        dizionario[carattere] = occorrenza
print(dizionario)