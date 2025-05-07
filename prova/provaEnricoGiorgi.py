#Transito class
class Transito:
    def __init__(self, targa, data, ora, velocita):
        # Inizializzazione degli attributi privati
        self.__targa = targa
        self.__data = data
        self.__ora = ora
        self.__velocita = float(velocita)  #virgola

    # Metodo è una multa?
    def is_multa(self):
        limite = 50  
        tolleranza = limite * 0.03  # tolleranza del 3%
        limite_velocita = limite + tolleranza  # limite + tolleranza
        if self.get_velocita() <= limite_velocita:
            return False
        else:
            return True

    # Getter e setter per targa
    def get_targa(self):
        return self.__targa

    def set_targa(self, value):
        self.__targa = value

    # Getter e setter per data
    def get_data(self):
        return self.__data
    def set_data(self, value):  
        self.__data = value

    # Getter e setter per ora
    def get_ora(self):
        return self.__ora   
    def set_ora(self, value):
        self.__ora = value    

    # Getter e setter per velocita
    def get_velocita(self):
        return self.__velocita
    def set_velocita(self, value):
        self.__velocita = value

#--------------------------------------------------------------------------
# Lettura file
transiti = []  # Lista per memorizzare i transiti

with open("transiti_urbani.txt") as file:
    # Saltiamo intestazione
    next(file)  

    for riga in file:
        targa, data_ora, velocita = riga.strip().split(";")  #toglie spazi e splitta riga
        data, ora = data_ora.split(" ")  # Separa data e ora
        transiti.append(Transito(targa, data, ora, velocita))  # aggiungiamo il transito ai transiti




conta_transiti = {}  # dizionario numero di transiti per targa
conta_multe = {}     # dizionario numero di multe per targa
totale_multe = 0     # le multe


for transito in transiti:
    # Conta multe
    if transito.is_multa():
            if transito.get_targa() in conta_multe:
                conta_multe[transito.get_targa()] += 1
            else:
                conta_multe[transito.get_targa()] = 1
            totale_multe += 1
    
    # Conta transiti
    if transito.get_targa() in conta_transiti:
        conta_transiti[transito.get_targa()] += 1
    else:
        conta_transiti[transito.get_targa()] = 1

# debug dizionari conta_transiti e conta_multe
print("Dizionario conta_transiti:", conta_transiti)
print("Dizionario conta_multe:", conta_multe)
#for transito in transiti:
#    print(f"Targa: {transito.get_targa()}, Data: {transito.get_data()}, Ora: {transito.get_ora()}, Velocità: {transito.get_velocita()}")
#---------------------------------------------------------------------------
# Targa con più transiti
targa_piu_transiti = None
massimo_transiti = 0

for targa, numero_transiti in conta_transiti.items():
    if numero_transiti > massimo_transiti:
        massimo_transiti = numero_transiti
        targa_piu_transiti = targa

# Targa con più multe
targa_piu_multe = None
massimo_multe = 0

for targa, numero_multe in conta_multe.items():
    if numero_multe > massimo_multe:
        massimo_multe = numero_multe
        targa_piu_multe = targa

if not conta_multe:
    targa_piu_multe = "Nessuna"



# ------------------------------------------------------------------
# Stampa risultati

print("Targa con più transiti:", targa_piu_transiti)
print("Targa con più multe:", targa_piu_multe)
print("Totale multe:", totale_multe)

