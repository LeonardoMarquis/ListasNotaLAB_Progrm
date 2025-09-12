def main():

    print("\nVou calcular a sequencia de Fibbonaci ate o numero")
    num = int(input("Numero Inteiro:\n"))


    i = 1
    sequencia = []
    anterior = 0
    while i < num:

        sequencia.append(i)
        
        prox = i + anterior
        anterior = i
        i = prox

    print(f"A sequencia: {sequencia}")

if __name__ == "__main__":
    main()