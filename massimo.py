#massimo.py

prova = []
userInpuit= input("Inserisci un numero: ")
while userInpuit != "**q**":
    prova.append(int(userInpuit))
    userInpuit= input("Inserisci un numero: ")
print("valore max",max(prova))

