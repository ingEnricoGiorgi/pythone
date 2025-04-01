#Shift + Alt + F
reddito = float(input("Immetti il tuo reddito in numeri: \n"))
scaglione1 = 28000
scaglione2 = 50000      
residuo = 22000

if reddito <= 0:
    print("Il reddito deve essere maggiore di 0.")
else: 
    if reddito <= scaglione1:
        tasse = reddito * 0.23
        print("Paghi il 23% di tasse: ", tasse)
    else:
        if reddito <= scaglione2:
            tasse = (scaglione1 * 0.23) + ((reddito - scaglione1) * 0.35)
            print("Paghi il 23% fino a 28.000 €, e il 35% sul resto: ", tasse)
        else:
            tasse = (scaglione1 * 0.23) + (residuo * 0.35) + ((reddito - scaglione2) * 0.43)
            print("Paghi il 23% fino a 28.000 €, il 35% fino a 50.000 €, e il 43% sul resto: ", tasse)
