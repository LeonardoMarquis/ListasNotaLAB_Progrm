def main():

    print("\nVou calcular o fatorial do numero")
    num = int(input("Numero Inteiro:\n"))


    i = num
    fatorial_num = 1
    while i > 0:
        fatorial_num = fatorial_num*i
        
        i -= 1

    print(f"O fatorial: {fatorial_num}")

if __name__ == "__main__":
    main()