#File: Esercizio4.py
#
#Autore: Samuele Follin
#
#Data: 15/07/2026
#
#Versione: 1.0
#
#Descrizione: Svolgimento dell'Esercizio 4

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

with open('rubrica.txt', 'w') as file_rubrica:                                 #apro il file con il context manager, così non devo chiuderlo alla fine
    for personaggio in rubrica:                                                #scrivo uno per uno i dati necessari all'interno del file, separandoli con le virgole
        file_rubrica.write(personaggio)
        file_rubrica.write(', ')
        file_rubrica.write(str(rubrica[personaggio]['giorno']))                #serve convertire in stringa perché .write() ammette solo stringhe al suo interno
        file_rubrica.write(', ')
        file_rubrica.write(rubrica[personaggio]['mese'])
        file_rubrica.write(', ')
        file_rubrica.write(str(rubrica[personaggio]['anno']))
        file_rubrica.write(', ')
        file_rubrica.write(str(rubrica[personaggio]['età']))
        file_rubrica.write(', ')
        file_rubrica.write(rubrica[personaggio]['sesso'])
        file_rubrica.write(', ')
        file_rubrica.write(rubrica[personaggio]['mail'])
        file_rubrica.write('\n')                                               #in questo modo si va a capo per ogni personaggio

#----- PUNTO 2 -----

import json

with open('rubrica.json', 'w') as file_rubrica:                          #così creo un file rubrica.json e lo affido alla variabile file_rubrica
    json.dump(rubrica, file_rubrica)                                     #rubrica è l'oggetto che salvo in file_rubrica (ossia il file 'rubrica.json')

#----- PUNTO 3 -----

with open('rubrica.json', 'r') as file_rubrica:
    dati = json.load(file_rubrica)                                      #leggo il file in un dizionario tramite .load e assegno alla variabile dati

print(dati)