def main():

    print("\nVou imprimir todos os numeros pares de 0 ate esse numero INTEIRO")
    num = int(input("Numero Inteiro:\n"))

    n_pares = []
    i = 0
    while i < num:

        if i%2 == 0:
            n_pares.append(i)

        i+=1

    print(f"Numero: {num}")
    print(f"Numeros pares de 0 ate {num}: \n{n_pares}")

if __name__ == "__main__":
    main()