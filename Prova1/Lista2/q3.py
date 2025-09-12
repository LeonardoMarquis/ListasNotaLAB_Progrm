def main():

    conjunto1 = {}
    conjunto2 = {}
    conjunto3 = {}

    conjunto1 = {"azul", "amarelo", "verde", "branco"}
    conjunto2 = {"vermelho", "branco", "prata", "laranja"}
    conjunto3 = {"roxo", "prata", "rosa", "laranja", "marrom"}


    lista = ["arr", conjunto1, conjunto2, conjunto3]

    while True:
        print("\n____________________________________________")
        print(f"CONJUNTO 1: {conjunto1}")
        print(f"CONJUNTO 2: {conjunto2}")
        print(f"CONJUNTO 3: {conjunto3}")

        print("\n_________________________________________________________________-")
        print("\n1-Fazer União entre 2 Conjuntos")
        print("\n2-Fazer Intercessão entre 2 Conjuntos")
        print("\n3-Fazer a Diferença entre 2 Conjuntos")
        print("\n4-Sair")
        print("_________________________________________________________________\n")

        op = int(input())

        match op:
            case 1:
                print(f"\n========União entre Conjuntos")

                n_conjunto_a = int(input("\nN° do conjunto: "))
                n_conjunto_b = int(input("\nN° do conjunto: "))

                if n_conjunto_a > 0 and n_conjunto_a <= 3 and n_conjunto_b > 0 and n_conjunto_b <=3:

                    resul = lista[n_conjunto_a] | lista[n_conjunto_b]
                    print(f"\nUnião entre {n_conjunto_a} e {n_conjunto_b}\n\n {resul}")

                else:

                    print("\nExcedeu o n° de conjuntos! digite de 1 a 3!")



            case 2:
                print(f"\n========Intercessão entre Conjuntos")

                n_conjunto_a = int(input("\nN° do conjunto: "))
                n_conjunto_b = int(input("\nN° do conjunto: "))

                if n_conjunto_a > 0 and n_conjunto_a <= 3 and n_conjunto_b > 0 and n_conjunto_b <=3:

                    resul = lista[n_conjunto_a] & lista[n_conjunto_b]
                    print(f"\nIntercessão entre {n_conjunto_a} e {n_conjunto_b}\n\n {resul}")

                else:

                    print("\nExcedeu o n° de conjuntos! digite de 1 a 3!")




            case 3:
                print(f"\n========Diferença entre Conjuntos (o que o 1° tem de diferente do 2°)")

                n_conjunto_a = int(input("\nN° do conjunto: "))
                n_conjunto_b = int(input("\nN° do conjunto: "))

                if n_conjunto_a > 0 and n_conjunto_a <= 3 and n_conjunto_b > 0 and n_conjunto_b <=3:

                    resul = lista[n_conjunto_a] - lista[n_conjunto_b]

                    print(f"\nDiferença entre {n_conjunto_a} e {n_conjunto_b}\n\n {resul}")

                else:

                    print("\nExcedeu o n° de conjuntos! digite de 1 a 3!")




            case 4:
                print("\nSaiu")
                break

            case _:
                print("\nDigitaste algo errado!")




if __name__ == "__main__":
    main()