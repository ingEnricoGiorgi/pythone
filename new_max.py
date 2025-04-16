def main():
    file_name = input("Inserisci il nome del file: ")
    
    #set {}
    #numbers è una lista []
    with open(file_name, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    
    max_value = max(numbers)
    media = sum(numbers) / len(numbers)
    print(f"La media è: {media}")
    print(f"Il valore massimo trovato nel file è: {max_value}")
    print(f"valore trovato alla posizione: {numbers.index(max_value)+1}")

#ci garantisce che viene eseguito solo se il file viene eseguito direttamente
#In pratica, mettendo la funzione main() sotto questa condizione, ti assicuri 
# che venga eseguita solo quando avvii direttamente lo script, ma non quando qualcun altro importa il tuo file come modulo.
#if __name__ == "__main__":
main()