import random

class Starter:                                                                    #creo la classe starter, principalmente per il metodo attacca che serve per attaccare il pokemon selvatico
    def __init__(self, nome):
        self.nome = nome

    def attacca(self):
        self.mossa = input('Quale mossa vuoi utilizzare? ')
        danni_possibili = [0, 10, 20, 30, 40]
        danni_inflitti = random.choice(danni_possibili)                           #numero casuale di danni
        hp_attuali = int(selezionatore.hp) - int(danni_inflitti)                  #calcolo gli hp dopo ogni danno
        selezionatore.hp = hp_attuali                                             #resetto gli hp attuali, senza questa riga dopo ogni attacco si rigenererebbe la vita
        if selezionatore.hp < 0:
            selezionatore.hp = 0
        if danni_inflitti == 0:
            print(f"il {selezionatore.nome} ha evitato l'attacco!")
        else:
            print(f'{starter.nome} ha sferrato la mossa {self.mossa} e ha inflitto {danni_inflitti} danni')
        print(f'{selezionatore.nome} ha {selezionatore.hp} HP rimanenti')

class Pokemon:                                                                    #classe dei pokemon selvatici con tutti gli attributi necessari
    def __init__(self, nome, hp, rarità, cattura):
        self.nome = nome
        self.hp = hp
        self.hp_massimi = hp
        self.rarità = rarità
        self.cattura = cattura

class Pokeball:                                                                  #classe delle pokeball
    def __init__(self, nome, bonus_cattura):
        self.nome = nome
        self.bonus_cattura = bonus_cattura

    def lancia(self):                                                                           #metodo di pokeball
        bonus_hp = int((selezionatore.hp_massimi - selezionatore.hp) / 2)                       #calcolo il bonus per gli HP rimanenti
        probabilità_di_cattura = selezionatore.cattura + self.bonus_cattura + bonus_hp         #probabilità definita dall'attributo iniziale, dalla pokeball e dal bonus hp
        if probabilità_di_cattura > 99:
            probabilità_di_cattura = 99                                                        #evito che vada sopra il 100 e aggiungo una minima possibilità di errore sempre
        print(f'Hai il {probabilità_di_cattura}% di catturare {selezionatore.nome}. Premi invio per lanciare la {self.nome}')
        input()
        percentuale = range(100)
        risultato = random.choice(percentuale)                                                  #sceglie un numero casuale tra 0 e 99
        if risultato <= probabilità_di_cattura:                                                 #se il numero estratto è minore della percentuale calcolata in precedenza
            print(f'Hai catturato {selezionatore.nome}! Grande!')
        else:
            print(f'{selezionatore.nome} è uscito dalla {self.nome}.')
            print(f'Hai un secondo tentativo. Premi invio per lanciare la {self.nome}')
            input()
            risultato = random.choice(percentuale)
            if risultato <= probabilità_di_cattura:                                                 #se il numero estratto è minore della percentuale calcolata in precedenza
                print(f'Hai catturato {selezionatore.nome}! Grande!')
            else:
                print(f'{selezionatore.nome} è uscito  dalla {self.nome}. Oh no, è scappato! Andrà meglio la prossima volta...')


print('Benvenuto nel simulatore di cattura Pokémon.')
print("Prima di cimentarti nella cattura dovrai scegliere un Pokémon con cui iniziare l'avventura, ce ne sono tre a disposizione:\n1) Bulbasaur\n2) Charmander\n3) Squirtle")
starter = input('Quale scegli? Bulbasaur, Charmander o Squirtle? ')
while starter not in ['Bulbasaur', 'Charmander', 'Squirtle']:                   #se non è uno dei tre si continua a chiedere input
    starter = input('So che è difficile, però devi scegliere! ')
print(f"Quindi hai scelto {starter}, eh? Ottima scelta, Buona fortuna!")
starter = Starter(starter)                                                      #lo starter diventa un oggetto di tipo starter

input('Premi invio per continuare')
print("\nScegli un ambiente in cui andare a caccia di Pokémon. I Pokémon selvatici che incontrerai saranno determinati dall'ambiente che scegli.")
print('Gli ambienti disponibili sono:\n1) Bosco\n2) Zona vulcanica\n3) Lago \n4) Centrale elettrica \n5) Caverna\n6) Tempio psichico\n7) Torre spettrale')
ambiente = input('Hai una vasta scelta! Forza, quale preferisci? ')

while ambiente not in [str(1), str(2), str(3), str(4), str(5), str(6), str(7)]:          #scelta dell'ambiente con i rispettivi pokemon selvatici
    ambiente = input('Scegli, 1), 2), 3), 4), 5), 6) o 7)? ')

if ambiente == str(1):
    pokemon_selvatici = [Pokemon("Caterpie", 45, "Comune", 80),
                         Pokemon("Pidgey", 40, "Comune", 75),
                         Pokemon("Oddish", 55, "Non comune", 55),
                         Pokemon("Scyther", 75, "Raro", 25),
                         Pokemon("Exeggutor", 100, "Molto raro", 10)]
elif ambiente == str(2):
    pokemon_selvatici = [Pokemon("Vulpix", 50, "Comune", 70),
                         Pokemon("Growlithe", 60, "Non comune", 50),
                         Pokemon("Ponyta", 65, "Non comune", 40),
                         Pokemon("Magmar", 80, "Raro", 25),
                         Pokemon("Moltres", 120, "Leggendario", 1)]
elif ambiente == str(3):
    pokemon_selvatici = [Pokemon("Magikarp", 30, "Comune", 80),
                         Pokemon("Poliwag", 45, "Comune", 70),
                         Pokemon("Staryu", 55, "Non comune", 45),
                         Pokemon("Lapras", 100, "Raro", 25),
                         Pokemon("Articuno", 120, "Leggendario", 1)]
elif ambiente == str(4):
    pokemon_selvatici = [Pokemon("Magnemite", 40, "Comune", 75),
                         Pokemon("Voltorb", 50, "Comune", 65),
                         Pokemon("Pikachu", 70, "Non comune", 50),
                         Pokemon("Electabuzz", 100, "Raro", 25),
                         Pokemon("Zapdos", 120, "Leggendario", 1)]
elif ambiente == str(5):
    pokemon_selvatici = [Pokemon("Zubat", 40, "Comune", 75),
                         Pokemon("Geodude", 55, "Comune", 60),
                         Pokemon("Sandshrew", 65, "Non comune", 55),
                         Pokemon("Onix", 110, "Raro", 25),
                         Pokemon("Kabutops", 100, "Raro", 10)]
elif ambiente == str(6):
    pokemon_selvatici = [Pokemon("Abra", 50, "Comune", 60),
                         Pokemon("Psyduck", 55, "Comune", 70),
                         Pokemon("Drowzee", 80, "Non comune", 40),
                         Pokemon("Mr Mime", 90, "Raro", 25),
                         Pokemon("Mewtwo", 130, "Leggendario", 1)]
elif ambiente == str(7):
    pokemon_selvatici = [Pokemon("Gastly", 60, "Comune", 60),
                         Pokemon("Haunter", 80, "Non comune", 40),
                         Pokemon("Gengar", 100, "Raro", 10)]

selezionatore = random.choice(pokemon_selvatici)                                #sceglie a caso un pokemon dalla lista, metodo di random


pokeball = Pokeball("Pokeball", 0)                                            #creo tre oggetti pokeball
megaball = Pokeball("Megaball", 10)
ultraball = Pokeball("Ultraball", 20)


print('\nOttima scelta!')
input('Premi invio per iniziare')




print(f'\nTi sei imbattuto in un {selezionatore.nome} selvatico, un pokemon {selezionatore.rarità}! Cosa vuoi fare?')            #la prima scelta: attaccare o tentare subito la cattura
print('1) Attaccare')
print('2) Tentare la cattura')
print('Se tenti la cattura subito, poi non potrai più attaccare! Inoltre, per la cattura hai due tentativi a disposizione.')
scelta = input('Scegli, 1 o 2? ')
while scelta not in [str(1), str(2)]:
    scelta = input('Scegli, 1 o 2? ')

if scelta == str(1):                                                                         #se l'utente sceglie di attaccare
    starter.attacca()
    scelta_due = input('Vuoi sferrare un altro attacco?\n1) Si\n2) No ')
    while scelta_due not in [str(1), str(2)]:
        scelta_due = input('Scegli! 1) o 2)?')
    while scelta_due == str(1):
        starter.attacca()
        if selezionatore.hp <= 0:                                                            #se il pokemon esaurisce gli HP
            print(f'Il {selezionatore.nome} selvatico è andato KO! Dovevi andarci più piano...')
            break
        scelta_due = input('Vuoi sferrare un altro attacco?\n1) Si\n2) No\n ')
    if selezionatore.hp > 0:
        sfera = input('Allora è il momento di catturarlo! Scegli:\n1) Pokéball\n2) Megaball\n3) Ultraball\n')
        while sfera not in [str(1), str(2), str(3)]:
            sfera = input('Scegli una sfera! 1), 2) o 3)?')
        if sfera == str(1):                                                                   #assegno ogni scelta alla pokeball corrispondente
            sfera = pokeball
        elif sfera == str(2):
            sfera = megaball
        elif sfera == str(3):
            sfera = ultraball
        sfera.lancia()

else:
    print('Vuoi lanciare una Pokéball, una Megaball o una Ultraball? Più e prestigata la sfera, più alta sarà la possibilità di catturarlo')
    sfera = input('Scegli:\n1) Pokéball\n2) Megaball\n3) Ultraball\n')
    while sfera not in [str(1), str(2), str(3)]:
        sfera = input('Scegli una sfera! 1), 2) o 3)?')
    if sfera == str(1):                                                                      #assegno ogni scelta alla pokeball corrispondente
        sfera = pokeball
    elif sfera == str(2):
        sfera = megaball
    elif sfera == str(3):
        sfera = ultraball
    sfera.lancia()