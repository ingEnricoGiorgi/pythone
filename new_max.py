def main():
    file_name = input("Inserisci il nome del file: ")
    
    #set {}
    #numbers è una lista []
    with open(file_name, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    
    max_value = max(numbers)
    print(f"Il valore massimo trovato nel file è: {max_value}")

if __name__ == "__main__":
    main()