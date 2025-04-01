#Shift + Alt + F
reddito = float(input("Immetti il tuo reddito in numeri: \n"))

if reddito <= 0:
    print("Il reddito deve essere maggiore di 0.")
elif reddito <= 28000:
    tasse = reddito * 0.23
    print("Paghi il 23% di tasse: ", tasse)
elif reddito <= 50000:
    tasse = (28000 * 0.23) + ((reddito - 28000) * 0.35)
    print("Paghi il 23% fino a 28.000 €, e il 35% sul resto: ", tasse)
else:
    tasse = (28000 * 0.23) + (22000 * 0.35) + ((reddito - 50000) * 0.43)
    print("Paghi il 23% fino a 28.000 €, il 35% fino a 50.000 €, e il 43% sul resto: ", tasse)
