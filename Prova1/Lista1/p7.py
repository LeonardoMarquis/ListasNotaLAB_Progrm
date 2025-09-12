def main():

    frase = str(input("Frase (max 100 caracteres): "))

    while len(frase) > 100:
        frase = str(input("Frase (max 100 caracteres): "))


    print(f"Vou inverter essa frase!")
    frase_inv = frase[::-1]
    print(f"Frase invertida: \n{frase_inv}")    


if __name__ == "__main__":
    main()