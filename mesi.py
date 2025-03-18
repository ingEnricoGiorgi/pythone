def traduci_mese(numero):
    mesi = {
        1: "Gennaio",
        2: "Febbraio",
        3: "Marzo",
        4: "Aprile",
        5: "Maggio",
        6: "Giugno",
        7: "Luglio",
        8: "Agosto",
        9: "Settembre",
        10: "Ottobre",
        11: "Novembre",
        12: "Dicembre"
    }
    return mesi.get(numero, "Numero di mese non valido")

numero = int(input("Inserisci un numero di mese (1-12): "))
print("Il mese corrisponde a:", traduci_mese(numero))

