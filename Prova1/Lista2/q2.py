
def main():

    rota = []

    while True:
        print("\n_________________________________________________________________-")
        print("\n1-Inserir Novo ponto GPS à rota")
        print("\n2-Remover Ponto GPS da rota")
        print("\n3-Exibir rota atual(relacao de todos os pontos cadastrados ate agora)")
        print("\n4-Sair")
        print("_________________________________________________________________\n")

        op = int(input())



        match op:
            case 1:
                n_do_ponto = len(rota)
                print(f"\n========Adicionar o ponto n{n_do_ponto+1}")

                
                x_ponto = int(input("\nPonto X: "))
                y_ponto = int(input("\nPonto Y: "))
                ponto = {"x": x_ponto, "y": y_ponto}

                rota.append(ponto)

                print(f"\n-----------------------\nEstado atual: {rota}\n-----------------------")

            case 2:
                print(f"\n========Remover Ponto")
            
                x_ponto_alvo = int(input("\nPonto x: "))
                y_ponto_alvo = int(input("\nPonto y: "))
                ponto_alvo = {"x": x_ponto_alvo, "y": y_ponto_alvo}

                encontrado = False
                for i, ponto in enumerate(rota):             # foi pedido para que usasse o del, entao usei manipulacao de indice de vetor
                    if ponto == ponto_alvo:           # usei enumerate porque o tamanho do vetor rota muda durante o processo
                        print("\nEncontrado.")              # o enumerate, o 1° e o indice, o 2° o valor assumido

                        del rota[i]
                    
                        print("\nRemovido.")
                        print(f"\n----------------------\nEstado atual: {rota}\n----------------------")

                        encontrado = True
                        break

                if encontrado is not True:

                    print("\nPonto nao encontrado, tente novamente!")

            case 3:
                print(f"\n========Mostrar Rota")

                print("\n--------------------\nEstado atual:")
                for p in rota:
                    print(p)

                print("\n----------------------")
            case 4:
                print("\nSaiu")
                break


            case _:
                print("\nDigitaste algo errado!")






if __name__ == "__main__":
    main()