def main():
    def cadastrar_pessoas():
        cpf = int(input("\ncpf: "))
        if cpf in pessoas:        # se existir....
            print("\nJá existe alguem com esse cpf!")
                
        else:
            nome = str(input("\nNome: "))
            endereco = str(input("\nEndereço: "))
            telefones = []

            while True:
                option = str(input("Digitar telefones, min 8 e max 11 digitos (sim/nao): "))

                match option.lower():

                    case "sim":
                        telefone = str(input("Telefone: "))

                        if len(telefone) < 8 or len(telefone)> 11:
                            print("Errou numero de digitos do telefone")
                            break

                        telefones.append(telefone)
                    case "nao":

                        pessoa = {'cpf': cpf, 'nome': nome, 'endereco': endereco, 'telefones': telefones}
                        pessoas[cpf] = pessoa   # no caso, a posicao n°cpf sera a posicao do dicionario pessoa, cpf sera um indice

                        print(f"\n{pessoas[cpf]} adicionado com sucesso")
                        break
                        
                    case _:
                        print("\nDigitaste algo errado! Nenhuma alteração feita")
                        break




    def listar_pessoas(lista):
        print("\n========LISTAR PESSOAS====================================================================")
        for i in lista:
            print(i)


                
    def buscar_pessoa_p_cpf(cpf, lista):
        if cpf not in lista:
            print("\nCPF não encontrado")

        
        elif cpf in lista:
            print(lista[cpf])

    def buscar_pessoa_p_telefone(telefone, lista):
        for i in lista:
            for telefone in i[telefone]:
                if telefone in i[telefone]:
                    print(i)

                else:
                    print("Telefone não encontrado!")


    def deletar_pessoa_p_cpf(cpf, lista):
        buscar_pessoa_p_cpf(cpf, lista)

        if buscar_pessoa_p_cpf(cpf, lista):
            for cpf in lista:
                lista.pop(cpf)
                print(f"{lista[cpf].nome} removido")


    #------------------------------------------------------------------------------

    pessoas = {}

    while True:
        op = int(input("\n1-inserir Pessoa" \
        "\n2-Listar Pessoas cadsatradas" \
        "\n3-Buscar Pessoas por cpf" \
        "\n4-Buscar Pessoa por Telefone" \
        "\n5-Remover pessoa por cpf\n"))

        match op:

            case 1:
                cadastrar_pessoas()

            case 2:
                listar_pessoas()

            case 3:
                print("\n========BUSCAR PESSOAS POR CPF====================================================================")

                cpf = int(input("\nCpf: "))
                buscar_pessoa_p_cpf(cpf, pessoas)

            case 4:
                print("\n========BUSCAR PESSOAS PELO TELEFONE====================================================================")

                telefone = int(input("\nTelefone: "))
                buscar_pessoa_p_telefone(telefone, pessoas)

            case 5:
                print("\n========DELETAR PESSOAS POR CPF====================================================================")
                
                cpf = int(input("\nCpf: "))
                deletar_pessoa_p_cpf(cpf, pessoas)
                
                

            case 6:
                print("\n========SAIR====================================================================")
                print("Saiu")
                break

            case _:
                print("Digitaste algo errado!")


if __name__ == "__main__":
    main()