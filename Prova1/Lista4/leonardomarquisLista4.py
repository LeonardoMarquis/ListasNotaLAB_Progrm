def main():
    def cadastrar_pessoas():

        pessoas_arquivo = open('pessoas.txt', 'a+', encoding='utf-8')
        

        cpf = str(input("\ncpf: ")).strip()
        if not cpf:
            print("\nCpf vazio! Nenhuma alteração feita")
            return 
        
        if buscar_pessoa_p_cpf(cpf) is not None:        # se existir....
            print("\nJá existe alguem com esse cpf!")
            
            return      # para nao sair da funcao

        else:
            nome = str(input("\nNome: ")).strip()
            endereco = str(input("\nEndereço: ")).strip()
            telefones_primitivo = []

            while True:
                option = str(input("\nDigitar telefones, min 8 e max 11 digitos (sim/nao): "))

                match option.lower():

                    case "sim":
                        telefone = str(input("Telefone: ")).strip()

                        if len(telefone) < 8 or len(telefone)> 11 or not telefone.isdigit():
                            print("Errou numero de digitos do telefone")
                            continue            # para permitir tentar outro numero de telefon, nao sair do loop case
                        if telefone in telefones_primitivo:
                            print("Telefone ja adicionado")
                            continue

                        telefones_primitivo.append(telefone)
                    case "nao":
                        separador = ","
                        telefones_separados_virgu = separador.join(telefones_primitivo)   # para separar os telefones por ,

                        telefones = telefones_separados_virgu

                        linha_pessoa = f"{cpf};{nome};{endereco};{telefones}\n"
                        with open('pessoas.txt', mode='a', encoding='utf-8') as file:
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

        cpf, nome, endereco, telefones_texto = elementos

        # transformar telefones de volta em lista
        telefones = [t for t in telefones_texto.split(',') if t]

        return{"cpf": cpf, "nome": nome, "endereco": endereco, "telefones": telefones}

    def listar_pessoas():
        pessoas_arquivo = open('pessoas.txt', 'r', encoding='utf-8')
        pessoas = pessoas_arquivo.readlines()
        if len(pessoas) == 0:
            print("\nA lista está vazia!")

        for pessoa in pessoas:
            print(pessoa)
        


                
    def buscar_pessoa_p_cpf(cpf):
        try:
            with open('pessoas.txt', 'r', encoding='utf-8') as pessoas_arquivo:
                for linha in pessoas_arquivo:
                    pessoa = linha_to_pessoa(linha)
                    if pessoa and pessoa["cpf"] == cpf:
                        return pessoa

        except FileNotFoundError:
            print("\nArquivo não encontrado")
            pass

        print("\ncpf não encontrado")
        return None

    def buscar_pessoa_p_telefone(telefone):
        telefone = str(telefone).strip()        # deixar em string e com strip

        try:
            with open('pessoas.txt', 'r', encoding='utf-8') as pessoas_arquivo:
                for linha in pessoas_arquivo:
                    pessoa = linha_to_pessoa(linha)
                    if pessoa and telefone in pessoa["telefones"]:
                        return pessoa
                    
        except FileNotFoundError:
            print("\nArquivo não encontrado")
            pass

        print("\ntelefone não encontrado")
        return None


    def deletar_pessoa_p_cpf(cpf):
        # no caso, excluir é na verdade reescrever o arquivo mas sem o que eu nao quero
        achado = False
        with open('pessoas.txt', 'r', encoding='utf-8') as pessoas_arquivo:
            linhas = pessoas_arquivo.readlines()

        with open('pessoas.txt', 'w', encoding='utf-8') as pessoas_arquivo:
            for linha in linhas:
                pessoa = linha_to_pessoa(linha)
                if pessoa and pessoa["cpf"] == cpf:
                    nome_deletado = pessoa["nome"]
                    print(f"\n{nome_deletado} deletado com sucesso")

                    achado = True
                    continue
                pessoas_arquivo.write(linha)
        
        return achado


    #------------------------------------------------------------------------------
    # apenas testando se o arquivo existe, se nao ja cria, isso aqui so executa 1 vez por execucao do codigo
    try:
        pessoas_arquivo = open('pessoas.txt', 'a', encoding='utf-8')
    except:
        pessoas_arquivo = open('pessoas.txt', 'w', encoding='utf-8')
        pessoas_arquivo.close()


    while True:
        op = int(input("\n\n1-inserir Pessoa" \
        "\n2-Listar Pessoas cadastradas" \
        "\n3-Buscar Pessoas por CPF" \
        "\n4-Buscar Pessoa por Telefone" \
        "\n5-Remover pessoa por cpf" \
        "\n6-SAIR\n"))

        match op:

            case 1:
                print("\n========CADASTRAR PESSOA====================================================================")
                cadastrar_pessoas()

            case 2:
                print("\n========LISTAR PESSOAS====================================================================")
                listar_pessoas()

            case 3:
                print("\n========BUSCAR PESSOAS POR CPF====================================================================")

                cpf = str(input("\nCpf: ")).strip()     # o strip() é para remover os espaços em branco
                pessoa = buscar_pessoa_p_cpf(cpf)
                print(f"{pessoa}" or "cpf não encontrado")

            case 4:
                print("\n========BUSCAR PESSOAS PELO TELEFONE====================================================================")

                telefone = str(input("\nTelefone: "))
                pessoa = buscar_pessoa_p_telefone(telefone)
                print(f"{pessoa}" or "telefone não encontrado")
                
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