import json
import random

impiccato ={'parola_uno': 'ombrello', 'parola_due': 'cristallo', 'parola_tre':'girasole', 'parola_quattro':'labirinto', 'parola_cinque':'tempesta', 
            'parola_sei': 'coccinella', 'parola_sette':'piramide', 'parola_otto':'zucchero', 'parola_nove':'fenicottero', 'parola_dieci': 'bussola'}

with open('impiccato.json', 'w') as file_impiccato:                                   #riporto in un file json il dizionario 'impiccato'
    json.dump(impiccato, file_impiccato)

with open('impiccato.json', 'r') as file_impiccato:
    rubrica_parole = dict(json.load(file_impiccato))                                  #dassegno il contenuto del file alla variabile rubrica_parole. Devo mettere dict(), se no non mi fa accedere ai valori tramite il metodo .values()

selezionatore = random.Random()                                                       #creo un oggetto seezionatore di tipo random

parola_segreta = selezionatore.choice(list(rubrica_parole.values()))                  #con .choice() scelgo casualmente una parola. devo convertire in lista i valori del dizionario, perché .choice non agisce sui dizionari, dà errore
#l'altra alternativa era creare una lista e inserirci tutti i valori con un loop, ma più pesante

#--------------------------------------------------------------------------

print("Ciao! Ti va di giocare al gioco dell'impiccato? Hai un totale di sette vite, ma usale bene: a ogni errore te ne verrà tolta una. Buona fortuna!")
print('Ricorda, sono ammesse solo lettere. Questa è la parola che il fato ha scelto per te:')
lettere_mancanti = ['_'] * len(parola_segreta)                                          #per vsiaulizzare a schermo i trattini sotto le lettere mancanti
print(' '.join(lettere_mancanti))                                                       #per visualizzare meglio, separo gli elementi della lista con uno spazio grazie  a.join()

vite_rimanenti = [1, 2, 3, 4, 5, 6, 7]
lettere_inserite = set()                                                                #creo un set per evitare la ripetizione di lettere
try:                                                                                    #questo try è riferito all'except finale di ctrl c
    while len(vite_rimanenti) >= 1 and parola_segreta != ''.join(lettere_mancanti):
        lettera = input('Inserisci una lettera: ').lower()                                 #queata volta l'input lo metto all'inizio del while, se no prima del messaggio finale chiede un input poi ignorato
        try:
            lettera = int(lettera)                                                         #controllo se l'input è un numero, se non lo è ci sarà un ValueError
            del vite_rimanenti[0]
            print(f'Ehi, ti avevo detto di inserire solo lettere! Chiaramente {lettera} non è nella parola, e per punirti ti toglierò comunque una vita')
            print(f'Quindi, hai a disposizione ancora {len(vite_rimanenti)} vite. Non sprecarle in questo modo!')
        except ValueError:
            try:                                                                              #controllo se l'input è un carattere speciale
                'abcdefghijklmnopqrstuvwxyzéèòçàù'.index(lettera)                             #se .index non trova la lettera dentro queata stringa allora l'input è un carattere speciale
                try:                                                                          #controllo se la lettera è gia stata inserita
                    lettere_inserite.remove(lettera)                                          #se la lettera è già nel set la rimuovo e poi la riaggiungo
                    lettere_inserite.add(lettera)
                    print("Hai già inserito questa lettera!")
                except KeyError:                                                              #se provo a rimuovere un elemento non esistente nel set ho un KeyError
                    lettere_inserite.add(lettera)
                    try:                                                                      #controllo se la lettera è contenuta nella parola segreta
                        parola_segreta.index(lettera)
                        print(f"Sì! La lettera {lettera} è presente nella parola")
                        try:
                            posizione = -1                                                          #se posizione = 0 la ricerca di .index parte da 1, in qesto modo parte da 0
                            while True:                                                             #while True perché non so l'occorrenza della lettera nella parola 
                                posizione = parola_segreta.index(lettera, posizione + 1)            #passo in rassegna tutte le posizioni della parola, posizione + 1 è il punto d'inizio dell'analisi
                                lettere_mancanti[posizione] = lettera
                        except ValueError:                                                          #quando la lettera in input non è più trovata nella stringa si genera un ValueError
                            pass                                                                    #così, anche se si genera un ValueError, il codice non si blocca
                    except ValueError:                                                              #se la lettera non è contenuta nella parola .index() genera un ValueError
                        del vite_rimanenti[0]
                        print(f"No, la lettera {lettera} non è presente nella parola")
                        print(f'Hai a disposizione ancora {len(vite_rimanenti)} vite')
            except ValueError:                                                                     #è l'except dei caratteri speciali
                del vite_rimanenti[0]
                print(f'Ehi, ti avevo detto di inserire solo lettere! Chiaramente {lettera} non è nella parola, e per punirti ti toglierò comunque una vita')
                print(f'Quindi, hai a disposizione ancora {len(vite_rimanenti)} vite. Non sprecarle in questo modo!')

            print(' '.join(lettere_mancanti))

    try:
        lettere_mancanti.index('_')                                                              #se in lettere mancanti è presente ancora almeno un _ la parola non è stata indovinata
        print(f'Hai perso, le tue vite sono finite! La parola era {parola_segreta}. La prossima volta sarai più fortunato!')
    except ValueError:                                                                           #se nella lista non ci sono '_' risuta un value error
        print(f'Hai vinto! La parola era {parola_segreta}. Ben fatto!')

except KeyboardInterrupt:                                                                        #se si interrompe il codice con Ctrl + c esce questo messaggio
    print('\nTi sei già stufato? Pazienza... grazie comunque per aver provato!')