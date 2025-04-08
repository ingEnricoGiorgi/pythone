#massimo.py

prova = []
userInput= input("Inserisci un numero: ")
while userInput != "q":
    prova.append(int(userInput))
    userInput= input("Inserisci un numero: ")
print("valore max",max(prova))

