import datetime

#s1= "2025/05/07 09:59:12"

#data_ora=datetime.datetime.strptime(s1, "%Y/%m/%d %H:%M:%S")
#print(data_ora)

with open("messaggi.txt")as infile:
    righe= infile.readlines()
    for riga in righe:
        riga = riga.strip()
        campi= riga.split(";")
        data_ora=datetime.datetime.strptime(campi[0], "%Y/%m/%d %H:%M:%S").time()
        mittente= campi[1]
        destinatario= campi[2]
        messaggio= campi[3]
        print(f"da {mittente} a {destinatario} alle {data_ora}: {messaggio}")