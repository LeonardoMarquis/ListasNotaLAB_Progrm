def main():

    print("\nVou imprimir a soma de todos os numeros impares de 1 ate esse numero INTEIRO")
    num = int(input("Numero Inteiro:\n"))

    soma_impares = 0
    i = 1
    while i < num:

        if i%2 != 0:
            soma_impares += i

        i+=1

    print(f"Numero: {num}")
    print("\n*1 esta incluso")
    print(f"Soma dos numeros impares de 1 ate {num}: \n{soma_impares}")

if __name__ == "__main__":
    main()