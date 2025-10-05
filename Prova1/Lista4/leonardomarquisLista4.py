def main():
    def cadastrar_pessoas():

        pessoas_arquivo = open('bd.txt', 'a+', encoding='utf-8')
        

        cpf = int(input("\ncpf: ")).strip()
        if cpf in pessoas_arquivo:        # se existir....
            print("\nJá existe alguem com esse cpf!")
                
        else:
            nome = str(input("\nNome: ")).strip()
            endereco = str(input("\nEndereço: ")).strip()
            telefones_primitivo = []

            while True:
                option = str(input("\nDigitar telefones, min 8 e max 11 digitos (sim/nao): "))

                match option.lower():

                    case "sim":
                        telefone = str(input("Telefone: ")).strip()

                        if len(telefone) < 8 or len(telefone)> 11:
                            print("Errou numero de digitos do telefone")
                            break

                        telefones_primitivo.append(telefone)
                    case "nao":
                        separador = ","
                        telefones_separados_virgu = separador.join(telefones_primitivo)   # para separar os telefones por ,

                        telefones = telefones_separados_virgu

                        linha_pessoa = f"{cpf};{nome};{endereco};{telefones}"
                        with open('bd.txt', mode='a', encoding='utf-8') as file:
                            file.write(linha_pessoa)
                        
                        print(f"\n{cpf} | {nome} adicionado com sucesso")
                        break
                        
                    case _:
                        print("\nDigitaste algo errado! Nenhuma alteração feita")
                        break

    
    def linha_to_pessoa(linha):
        linha = linha.strip()
        if not linha:
            return None
        
        elementos = linha.split(";", 3)     # corta os tres ; que separam os 4 atributos de pessoa linha
        if len(elementos) != 4:             # se o n de elementos separados por ; for diferente de 4
            return None

        cpf, nome, endereco, telefones = elementos

        return{"cpf": cpf, "nome": nome, "endereco": endereco, "telefones": telefones}

    def listar_pessoas():
        pessoas_arquivo = open('bd.txt', 'r', encoding='utf-8')
        pessoas = pessoas_arquivo.readlines()
        if len(pessoas) == 0:
            print("\nA lista está vazia!")

        for i in pessoas:
            print(pessoas[i])
        


                
    def buscar_pessoa_p_cpf(cpf):
        try:
            with open('bd.txt', 'r', encoding='utf-8') as file:
                for linha in file:
                    pessoa = linha_to_pessoa(linha)
                    if pessoa and pessoa["cpf"] == cpf:
                        return pessoa

        except FileNotFoundError:
            print("\nArquivo não encontrado")
            pass

        print("\ncpf não encontrado")
        return None

    def buscar_pessoa_p_telefone(telefone, lista):
        telefone = str(telefone).strip()    # garante que o numero de telefone buscado sera uma string e estara sem espaços

        for pessoa in lista.values():       # esse lista.values ja atravessa os indices, e pega os valores dentro dos indices e 
                                            # e assim "pessoa" recebendo os valores dentro de lista que foram guardados nos indices cpf
                                            # ex: "pessoa" vai ser lista[cpf tal], lista[cpf tal2], lista[cpf tal3] 
            if telefone in pessoa['telefones']:
                print(pessoa)
                return
        
        print("\nTelefone não encontrado!")


    def deletar_pessoa_p_cpf(cpf):
        pessoas_arquivo = open('bd.txt', 'r', encoding='utf-8')

        buscar_pessoa_p_cpf(cpf, conteudo)

        if cpf in conteudo:
            aux = conteudo[cpf]
            print(f"{aux['nome']} removido")
            
            com_deletado = conteudo.


    #------------------------------------------------------------------------------
    # apenas testando se o arquivo existe, se nao ja cria, isso aqui so executa 1 vez por execucao do codigo
    try:
        pessoas_arquivo = open('bd.txt', 'a')
    except:
        pessoas_arquivo = open('bd.txt', 'w')
        pessoas_arquivo.close()


    while True:
        op = int(input("\n1-inserir Pessoa" \
        "\n2-Listar Pessoas cadastradas" \
        "\n3-Buscar Pessoas por cpf" \
        "\n4-Buscar Pessoa por Telefone" \
        "\n5-Remover pessoa por cpf\n"))

        match op:

            case 1:
                print("\n========CADASTRAR PESSOA====================================================================")
                cadastrar_pessoas()

            case 2:
                print("\n========LISTAR PESSOAS====================================================================")
                listar_pessoas()

            case 3:
                print("\n========BUSCAR PESSOAS POR CPF====================================================================")

                cpf = int(input("\nCpf: ")).strip()     # o strip() é para remover os espaços em branco
                buscar_pessoa_p_cpf(cpf)

            case 4:
                print("\n========BUSCAR PESSOAS PELO TELEFONE====================================================================")

                telefone = str(input("\nTelefone: "))
                buscar_pessoa_p_telefone(telefone).strip()

            case 5:
                print("\n========DELETAR PESSOAS POR CPF====================================================================")
                
                cpf = str(input("\nCpf: ")).strip()
                deletar_pessoa_p_cpf(cpf)
                
                

            case 6:
                print("\n========SAIR====================================================================")
                print("Saiu")
                break

            case _:
                print("Digitaste algo errado!")


if __name__ == "__main__":
    main()