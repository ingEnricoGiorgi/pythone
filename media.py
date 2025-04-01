count=0
somma=0
leggi="prova"
while(leggi!="exit"):
    leggi=input("Immetti valore o scrivi exit: \n")
    if(leggi=="exit"):
        break
    else:
        somma=somma+int(leggi)
        count=count+1


media=somma//count
print("La media è: ",media)