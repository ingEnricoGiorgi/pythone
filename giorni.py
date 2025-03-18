def traduci_settimana(numero):
    giorni = {
        1: "Lunedì",
        2: "Martedì",
        3: "Mercoledì",
        4: "Giovedì",
        5: "Venerdì",
        6: "Sabato",
        7: "Domenica"
    }
    return giorni.get(numero, "Numero di giorno non valido")

tastiera = input("Inserisci un numero di giorno (1-7): ")

num = int(tastiera)
print("Il giorno corrisponde a:", traduci_settimana(num))



