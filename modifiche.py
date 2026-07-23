print('Ciao! Ti va di fare un paio di tabelline?')
while True:                                                                                      #ciclo infinito, condizione sempre vera... si esce solo grazie al break
    try:                                                                                         #uso try-except, così gestisco i caratteri e i numeri che sono decimali
        numero = int(input('Dimmi un numero intero! '))                                          #senza int() l'input è considerato stringa e i risultati delle tabelline sono sbagliati
        break                                                                                    #permette di uscire dal ciclo, l'unico modo è passare per break scegliendo un numero intero
    except ValueError:
        print('Ehi, scegli un numero intero! Non digitare lettere, caratteri speciali o numeri decimali.')                        #continuo finché non viene digitato un numero intero

print(f'Ok... hai scelto il numero {numero}, eh? Vediamo come te la cavi, dovrai indovinare tutti i risultati! Quanto fa {numero} x 0?')

lista_corrette = []                                                                                        #questa lista serve a tenere il conto delle soluzioni corrette
def tabelline(numero):
    for i in range(10):                                                                                    #passo in rassegna tutti i numeri da 0 a 9
        while True:                                                                                        #anche qui devo assicurarmi di ricevere solo interi, stesso while di prima con try-except
            try:
                risposta = int(input())                                                                    #anche qui ho bisogno che l'input sia di tipo int, non str
                break
            except ValueError:
                print('Il risultato della moltiplicazione di due interi è un intero, suvvia!')
        if risposta == numero * i:                                                                          #creo due diverse frasi in base alla risposta data
            lista_corrette.append(risposta)
            yield f'Corretto! Era {numero * i}. E ora, quanto fa {numero} x {i+1}?'
        else:
            yield f'Hai sbagliato! Il risultato corretto era {numero * i}. Dai, prova a calcolare {numero} x {i+1}'

 
g = tabelline(numero)                                               #creo così l'oggetto generatore

for i in range(10):
    print(next(g))                                              #grazie allo yield posso andare avanti con gli indici del range

while True:                                                           #per il risultato di n x 10, stesso try-except di prima
    try:
        risposta = int(input())                                       #anche qui ho bisogno che l'input sia intero
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
    print('Wow, ottimo risultato! Puoi senza dubbio raggiungere la perfezione, se ti eserciti ancora un po')
elif len(lista_corrette) == 11:
    print('Le tabelline sono il tuo forte! Ben fatto')
