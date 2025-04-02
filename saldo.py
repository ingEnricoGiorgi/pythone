saldo_iniziale = float(input("Immetti saldo iniziale: \n"))
anni_input = input("Immetti per quanti anni vuoi percepire interessi: \n")
interesse = 0.04  # 4%

def calcolo_interessi(saldo, anni, interesse):
    for i in range(anni):
        saldo *= (1 + interesse)
        print("Il saldo dopo", i + 1, "anni è:", round(saldo, 2))
    return saldo

if anni_input == "0" or anni_input == "":
    result = calcolo_interessi(saldo_iniziale, 20, interesse)
else:
    anni = int(anni_input)
    result = calcolo_interessi(saldo_iniziale, anni, interesse)

print("Il saldo finale è:", round(result, 2))
