#File: Esercizio7.py
#
#Autore: Samuele Follin
#
#Data: 22/07/2026
#
#Descrizione: Svolgimento dell'Esercizio 7

print('Ciao! Ti va di fare un paio di tabelline?')
while True:                                                                                      #ciclo infinito, condizione sempre vera... si esce solo grazie al break
    try:                                                                                         #uso try-except, così gestisco lettere, caratteri speciali e numeri decimali
        numero = int(input('Dimmi un numero intero! '))                                          #senza int() l'input è considerato stringa e i risultati delle tabelline sono sbagliati
        break                                                                                    #permette di uscire dal ciclo, l'unico modo è passare per break scegliendo un numero intero
    except ValueError:                                                                           #se l'input non è un intero, il tentativo di conversione genera un ValueError
        print('Ehi, scegli un numero intero! Non digitare lettere, caratteri speciali o numeri decimali.')

print(f'Ok... hai scelto il numero {numero}, eh? Vediamo come te la cavi, dovrai indovinare tutti i risultati! Iniziamo, quanto fa {numero} x 0?')

lista_corrette = []                                                                                        #questa lista serve a tenere il conto delle soluzioni corrette
def tabelline(numero):
    '''valuta se la risposta data sulla moltiplicazione è corretta'''
    for i in range(10):                                                                                    #passo in rassegna tutti i numeri da 0 a 9
        while True:                                                                                        #anche qui devo assicurarmi di ricevere solo interi, stesso while di prima con try-except
            try:
                risposta = int(input())                                                                    #anche qui ho bisogno che l'input sia di tipo int, non str
                break
            except ValueError:
                print('Il risultato della moltiplicazione di due interi è un intero, suvvia!')
        if risposta == numero * i:                                                                         #creo due frasei personalizate in base alla risposta data dall'utente
            lista_corrette.append(risposta)
            yield f'Corretto! Era {numero * i}. E ora, quanto fa {numero} x {i+1}?'
        else:
            yield f'Hai sbagliato! Il risultato corretto era {numero * i}. Dai, prova a calcolare {numero} x {i+1}'

 
g = tabelline(numero)                                           #creo così l'oggetto generatore

for i in range(10):                                             #grazie allo yield, la funzione viene messa in pausa e dopo aver chiamato next ricomincia da dove si era fermata
    print(next(g))                                              #in questo caso, per ogni indice del range la funzione si ferma e ricomincia per il successivo

while True:                                                     #per il risultato di n x 10, stesso try-except di prima
    try:
        risposta = int(input())                                       
        break
    except ValueError:
        print('Il risultato della moltiplicazione di due interi è un intero, suvvia!')
if risposta == numero * 10:                                                #per il 10 devo creare un if a parte, se lo metto dentro la funzione dovrei fare range(11) e mi chiederebbe n x 11 senza ottenere risposta
    lista_corrette.append(risposta)
    print('Corretto!\n')     
else:
    print(f'Hai sbagliato! Il risultato corretto era {numero * 10}\n')  

print(f'Hai totalizzato un punteggio di {len(lista_corrette)}/11')                               #il numero di elementi della lista corrisponde alle risposte corrette, stampo a schermo il punteggio
if len(lista_corrette) < 4:                                                                      #stampo un messaggio diverso in base al numero di risposte corrette
    print('Caspita... dovresti fare pratica, puoi solo migliorare!')
elif 4 <= len(lista_corrette) <= 7:
    print('Risultato migliorabile, con della pratica puoi correggere tutti i tuoi errori!')
elif 7 < len(lista_corrette) <= 10:
    print("Wow, ottimo risultato! Puoi senza dubbio raggiungere la perfezione, ma solo se ti eserciti ancora un po'.")
elif len(lista_corrette) == 11:
    print('Le tabelline sono il tuo forte! Ben fatto.')
