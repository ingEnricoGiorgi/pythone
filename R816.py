# Stringa di partenza
testo = "Ciao mondo! Questo è un esempio di stringaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."

# Rendo tutto minuscolo
testo = testo.lower()


alfabeto = "abcdefghijklmnopqrstuvwxyz"
conteggio = {}

#azzero
for lettera in alfabeto:
    conteggio[lettera] = 0

for carattere in testo:
    if carattere in alfabeto:
        conteggio[carattere] += 1

massimo = 0
lettera_piu_frequente = ""

for lettera in alfabeto:
    if conteggio[lettera] > massimo:
        massimo = conteggio[lettera]
        lettera_piu_frequente = lettera

lettere_mancanti = []

for lettera in alfabeto:
    if conteggio[lettera] == 0:
        lettere_mancanti.append(lettera)

print("Lettera più frequente:", lettera_piu_frequente)
print("Lettere minuscole mancanti:", lettere_mancanti)
