import json

class Rubrica:
    def __init__(self, rubrica = None):                              #imposto un valore di default, se una rubrica non verrà aperta, allora ilvalore rimarrà None. serve per il metodo aggiungi
        self.rubrica = rubrica

    @classmethod                                                    #creo un metodo di classe per l'inizializzazione in json, grazie a cls ogni oggetto della classe 'memorizza' questo metodo
    def inizializzazione_in_json(cls, file):
        with open(file, 'r') as file_rubrica:
            rubrica = json.load(file_rubrica)
        return cls(rubrica)

    @classmethod                                                    #creo un metodo di classe per l'inizializzazione in testo
    def inizializzazione_in_txt(cls, file):
        with open(file, "r") as file_rubrica:
            rubrica = {}
            for riga in file_rubrica:                               #leggo tutti i dati grazie a questo ciclo for
                dati = riga.split(",")                              #così ogni riga diventa una lista, gli elementi sono tutti i dati, poiché sono separati da virgole
                personaggio = dati[0]                               #il personaggio è il primo elemento, il giorno è il secondo, ecc.
                rubrica[personaggio] = {
                    'giorno': int(dati[1]),
                    'mese': dati[2],
                    'anno': int(dati[3]),
                    'età': int(dati[4]),
                    'sesso': dati[5],
                    'mail': dati[6]
                    }
        return cls(rubrica)
    
    def apri(self, file):
        if file.endswith('.json'):                                  #distinguo i due casi tramite endswith, in entrambi i casi apro il file in modalità read
            with open(file, 'r') as file_rubrica:
                self.rubrica = json.load(file_rubrica)

        elif file.endswith('.txt'):                                 #NON posso utilizzare .read(), se lo faccio trasforma in stringa e poi si intralcia con gli altri metodi
            self.rubrica = {}
            with open(file, 'r') as file_rubrica:
                for riga in file_rubrica:                           #stesso procedimento dell'inizializzazione
                    dati = riga.split(",")
                    personaggio = dati[0]
                    self.rubrica[personaggio] = {
                    'giorno': int(dati[1]),
                    'mese': dati[2],
                    'anno': int(dati[3]),
                    'età': int(dati[4]),
                    'sesso': dati[5],
                    'mail': dati[6]
                }
    
    def aggiungi(self, personaggio, dati):
        if self.rubrica is None:                                   #la rubrica risulta None se nessuna variabile le è stata assegnata: infatti il default di rubrica in init è None
            print('Prima apri una rubrica')
        else:
            self.rubrica[personaggio] = dati

    def rimuovi(self, personaggio):
        if len(self.rubrica) == 0:                                 #se la rubrica è vuota
            print('La rubrica è vuota')
        elif personaggio in self.rubrica:
            del self.rubrica[personaggio]
        else:
            print('Il contatto', personaggio, 'non esiste in rubrica')

    def salva(self, file):
        if len(self.rubrica) == 0:
            print('La rubrica è vuota')
        elif file.endswith('.json'):                                         #utilizzo il metodo .dump del modulo json
            with open(file, 'w') as file_rubrica:
                json.dump(self.rubrica, file_rubrica)
        elif file.endswith('.txt'):
                with open(file, 'w') as file_rubrica:
                    for personaggio, dati in self.rubrica.items():            #devo mettere .items per riuscire ad accedere anche ai valori
                        riga = (                                              #compatto in righe perché .write ammette un solo elemento
                        personaggio + ','
                        + str(dati['giorno']) + ','
                        + dati['mese'] +','
                        + str(dati['anno']) + ','
                        + str(dati['età']) + ','
                        + dati['sesso'] + ','
                        + dati['mail']
                        )
                        file_rubrica.write(riga + '\n')
                
    
    def stampa(self, personaggio):
        if len(self.rubrica) == 0:
            print('La rubrica è vuota')
        elif personaggio in self.rubrica:
            dati = self.rubrica[personaggio]                                #i dati sono i valori delle chiavi personaggio (cioè dei dizionari)
            print('nome: ', personaggio)
            print('giorno: ', dati['giorno'])                               #stampo ogni valore del dizionario annidato
            print('mese: ', dati['mese'])
            print('anno: ', dati['anno'])
            print('età: ', dati['età'])
            print('sesso: ', dati['sesso'])
            print('mail: ', dati['mail'])
        else:
            print('Il contatto', personaggio, 'non esiste in rubrica')
