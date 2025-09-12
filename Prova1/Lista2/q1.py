def main():
    alunos = []
    
    while True:
        print("\n1-Inserir novo aluno\n2-Buscar aluno\n3-Exibir em ordem alfabetica\n4-Remover aluno da lista\n5-Sair")
        op = int(input())
    

        match op:
            case 1:
                print("\nADICIONAR ALUNO====\n")
                aluno = str(input("Nome do aluno:\n"))
                
                if aluno in alunos:
                    print("\nJa tem um aluno com esse nome!")
                    
                    return
                
                
                alunos.append(aluno)
                print(f"{aluno} Adicionado com sucesso.")
                
            case 2:
                print("\nBUSCAR ALUNO====\n")
                aluno = str(input("Nome do aluno:\n"))
                
                if aluno in alunos:
                    print("\Busca com sucesso:")
                    print(f"\n{aluno}")
                else:
                    print("\n\nBusca sem sucesso")
                    print("\nDigitaste o nome errado ou ele nao esta na lista!")

            case 3:
                print("\nEXIBIR ORDEM ALFABETICA====\n")
                
                if len(alunos) < 1:
                    print("Lista vazia por enquanto!")
                
                alunos_ordem_alfabeti = sorted(alunos)
                
                print(f"{alunos_ordem_alfabeti}")
            case 4:
                print("\REMOVER ALUNO====\n")
                aluno = str(input("Nome do aluno:\n"))
                
                if aluno in alunos:
                    alunos.remove(aluno)
                    
                    print(f"{aluno} Removido com sucesso.")

                else:
                    print("\nBusca sem sucesso")
                    print("\nDigitaste o nome errado ou ele nao esta na lista!")
                    
                    
            case 5:
                print("\nSaiu.")
                break
                
            case _:
                print("\nDigitaste algo errado!")
        
        
        
    
    
if __name__ == "__main__":
    main()