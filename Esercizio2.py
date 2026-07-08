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

#-----------------------------------

lista_righe = testo_originale.splitlines()                                 #in questo modo divido il testo riga per riga, le righe vengono inserite in una lista
lista_righe_piene = []                                           #creo la lista momentaneamente vuota

for riga in lista_righe:
    if riga != '':
      lista_righe_piene.append(riga)                             #se la riga non è vuota allora viene aggiunta alla lista di righe piene

print(len(lista_righe_piene))


#------------------------------------

lista_parole = testo_originale.split()                                     #in questo modo isolo ogni parola del testo, le parole vengono inserite in una lista
print(len(lista_parole))


#------------------------------------


lista_caratteri_alfanum = [lettera for lettera in testo_originale if lettera.isalnum()]      #così studia tutti i caratteri e mette dentro la lista quelli alfanumerici. list comprehension!
print(len(lista_caratteri_alfanum))


#------------------------------------


n = input()
lista_lettera = []

for lettera in testo_originale:                                            #'lettera' è l'indice, con questo loop for analizza tutte le lettere della variabile testo
   if n == lettera:
      lista_lettera.append(lettera)                              #se la lettera analizzata in questione è uguale all'input, essa viene messa nella lista

print(len(lista_lettera))


#---------------------------------------

testo_1 = testo_originale
parole_da_sostituire = ['day', 'Day', 'about', 'About', 'water', 'Water']       #creo una lista con le parole da sostituire
for parola in parole_da_sostituire:
    testo_1 = testo_1.replace(parola, 'PYTHON')                         #scorro la lista creata e sostituisco le parole nel testo, e creo t per non modificare il testo originale

print(testo_1)


#----------------------------------------

testo_2 = list(testo_originale.split())                #rendo il testo una lista per agire sugli indici
for i, parola in enumerate(testo_2):         #con enumerate tengo traccia degli indici
    if i % 2 != 0:
        testo_2[i] = parola.upper()          #sostituisco nel testo (lista) le posizioni dispari con le posizioni DISPARI


testo_2 = " ".join(testo_2)                    #ricostruisco il testo, con " " metto gli spazi tra le parole
print(testo_2)

#------------------------------------------

testo_3 = testo_originale.splitlines()
testo_3.reverse()                       #inverto l'ordine delle righe
testo_3 = "\n".join(testo_3)            #ricostruisco il testo, con "\n" vado a capo a ogni riga 
print(testo_3)

#-------------------------------------------

testo_4 = testo_originale.splitlines()
for i, verso in enumerate(testo_4):
    if i == 2 or i ==7 or i == 12 or i == 17:          #sono le posizioni corrispondenti ai versi numero due di ogni strofa
        testo_4[i] = verso[::-1]                       #è uno slicing, infatti [inizio, fine, passo] in questo caso è composto solo dal passo, che essendo -1 va all'indietro

testo_4 = "\n".join(testo_4)
print(testo_4)

#-------------------------------------------

strofe = testo_originale.split("\n\n")        #divido il testo in strofe
liste_parole = []

for strofa in strofe:
    parole = set(strofa.split())              #creo un set per ogni strofa con al suo interno le parole della strofa
    liste_parole.append(parole)               #aggiungo i 4 set dentro la lista

parole_comuni = set.intersection(*liste_parole)       #con * l'intersezione viene fatta tra tutti gli elementi della lista, cioè tutti e 4 i set di parole

print(parole_comuni)

#-------------------------------------------

for i in range(len(lista_parole)):                       #algoritmo di insertion sort
    key = lista_parole[i]                                #creo una variabile chiave
    j = i - 1                                            #creo un altro puntatore
    while j >= 0 and len(lista_parole[j]) > len(key):    #finché la parola che precede la parola interessata è più lunga, scambio le due parole
        lista_parole[j + 1] = lista_parole[j]
        j = j - 1
    lista_parole[j + 1] = key 
lista_parole_ordinate = lista_parole
print(lista_parole_ordinate)

#---------------------------------------------

lista_caratteri = list(testo_originale)              #così divido il testo in singoli caratteri
dizionario = {}                                      #creo il dizionario per il momento vuoto
for carattere in lista_caratteri:
    occorrenza = lista_caratteri.count(carattere)    #conto l'occorrenza per ogni carattere
    dizionario[carattere] = occorrenza               #assegno a ogni chiave 'carattere' il suo corrispettivo valore 'occorrenza'
print(dizionario)

#----------------------------------------------

lista_caratteri_minuscoli = list(testo_originale.lower())           #in questo modo tutte le lettere sono minuscole

dizionario = {}
for carattere in lista_caratteri_minuscoli:
    if carattere.isalnum():                                         #considera solo i caratteri alfanumerici
        occorrenza = lista_caratteri_minuscoli.count(carattere)
        dizionario[carattere] = occorrenza
print(dizionario)