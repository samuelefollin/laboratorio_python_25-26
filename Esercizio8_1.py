#File: Esercizio8_1.py
#
#Autore: Samuele Follin
#
#Data: 21/07/2026
#
#Versione: 1.0
#
#Descrizione: Svolgimento dell'Esercizio 8, approccio LBYL

import json
import random

impiccato = {'parola_uno': 'ombrello', 'parola_due': 'cristallo', 'parola_tre':'girasole', 'parola_quattro':'labirinto', 'parola_cinque':'tempesta', 
            'parola_sei': 'coccinella', 'parola_sette':'piramide', 'parola_otto':'zucchero', 'parola_nove':'fenicottero', 'parola_dieci': 'bussola'}

with open('impiccato.json', 'w') as file_impiccato:                                   #riporto in un file json il dizionario 'impiccato' con le possibili parole del gioco
    json.dump(impiccato, file_impiccato)

with open('impiccato.json', 'r') as file_impiccato:
    rubrica_parole = dict(json.load(file_impiccato))                                  #devo usare il type constructor dict(), se no non mi fa accedere ai valori tramite il metodo .values()

selezionatore = random.Random()                                                       #creo un oggetto selezionatore di tipo random

parola_segreta = selezionatore.choice(list(rubrica_parole.values()))                  #con .choice() scelgo casualmente una parola, devo convertire in lista i valori del dizionario, per far funzionare il metodo
#l'altra alternativa era creare una lista e inserirci tutti i valori con un loop, ma più pesante

#--------------------------------------------------------------------------

print("Ciao! Ti va di giocare al gioco dell'impiccato? Hai un totale di sette vite, ma usale bene: a ogni errore te ne verrà tolta una. Buona fortuna!")
print('Ricorda, sono ammesse solo lettere. Questa è la parola che il fato ha scelto per te:')
lettere_mancanti = ['_'] * len(parola_segreta)                                          #per vsiaulizzare a schermo i trattini delle lettere mancanti, '_' in una lista per usare .join() dopo
print(' '.join(lettere_mancanti))                                                       #per visualizzare meglio, separo gli elementi della lista con uno spazio grazie a .join()

vite_rimanenti = [1, 2, 3, 4, 5, 6, 7]
lettere_inserite = set()                                                                #creo un set per evitare la ripetizione di lettere

lettera = input('Inserisci una lettera: ').lower()                                      #se l'input è una lettera maiuscola, .lower() la rende minuscola

while len(vite_rimanenti) >= 1 and parola_segreta != ''.join(lettere_mancanti):         #qui prima del join non ci vanno gli spazi: non sarà mai uguale a ' '.join() perché esso è solo nel print, non cambia lettere_mancanti
        while lettera in lettere_inserite:                                              #senza questo blocco while non viene controllata la lettera inserita dopo a quella già inserita due volte
            lettera = input("Hai già inserito questa lettera! Inseriscine un'altra: ").lower()
        if lettera.isalpha():                                                               #il meccanismo si attiva solo se l'input è una lettera
            lettere_inserite.add(lettera)
            if lettera in parola_segreta:
                print(f'Si! La lettera {lettera} è presente nella parola:')
                for posizione in range(len(parola_segreta)):                                #passo in rassegna tutte le posizioni delle lettere per trovare quella corrispondente all'input
                    if lettera == parola_segreta[posizione]:
                        lettere_mancanti[posizione] = lettera                               #sostituisco l'underscore con la lettera dell'input
                print(' '.join(lettere_mancanti))                                           #lettere mancanti sarà sempre 'parola' e non 'p a r o l a' perché il ' '.join è dentro il print
            else:
                del vite_rimanenti[0]                                                       #rimuove un elemento dalla lista, così le vite calano (non è importante quale elemento è rimosso)
                print(f'No, la lettera {lettera} non è presente nella parola.')
                print(f'Hai a dispisizione ancora {len(vite_rimanenti)} vite.')
        else:                                                                               #se l'input non è una lettera
            del vite_rimanenti[0]
            print(f'Ehi, ti avevo detto di inserire solo lettere. Chiaramente {lettera} non è nella parola, e per punirti ti toglierò comunque una vita.')
            print(f'Quindi, hai a disposizione ancora {len(vite_rimanenti)} vite. Non sprecarle in questo modo!')
                
        if parola_segreta == ''.join(lettere_mancanti):
            print(f'Hai vinto, grande! La parola era {parola_segreta}')                                                                              #messaggio dedicato se si indovina la parola
            break                                                                                                                                    #break serve a non chiedere un input per poi ignorarlo
        elif len(vite_rimanenti) == 0:
            print(f'Hai perso, le tue vite sono finite! La parola era {parola_segreta}. La prossima volta sarai più fortunato')
            break                                                                                                                                    #stessa cosa qui, il break serve a ignorare l'input finale, e a terminare il gioco
        lettera = input('Inserisci una lettera: ').lower()                                                                                           #se l'input è una lettera maiuscola, .lower() la rende minuscola