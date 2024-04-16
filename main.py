import fucoes

def menu():
    print("\n1. Cadastrar Veiculo")
    print("2. Listar Veiculos")
    print("3. Consultar Veiculo")
    print("4. Atualizar Veiculo")
    print("5. Deletar Veiculo")
    print("6. Cadastrar Motorista")
    print("7. Listar Motoristas")
    print("8. Consultar Motorista")
    print("9. Atualizar Motorista")
    print("10. Deletar Motorista")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opcao: ")

        if opcao == '1':
            placa = input("Digite a placa do veiculo: ")
            modelo = input("Digite o modelo do veiculo: ")
            ano = input("Digite o ano do veiculo: ")
            veiculo = {'placa': placa, 'modelo': modelo, 'ano': ano}
            fucoes.cadastrar_veiculo(veiculo)
            print("Veiculo cadastrado com sucesso!")
        
        elif opcao == '2':
            veiculos = fucoes.listar_veiculos()
            print("Lista de Veiculos:")
            for veiculo in veiculos:
                print(veiculo)

        elif opcao == '3':
            placa = input("Digite a placa do veiculo: ")
            veiculo = fucoes.consultar_veiculo(placa)
            if veiculo:
                print("Veiculo encontrado:", veiculo)
            else:
                print("Veiculo nao encontrado.")

        elif opcao == '4':
            placa = input("Digite a placa do veiculo a ser atualizado: ")
            novo_placa = input("Digite a nova placa do veiculo: ")
            novo_modelo = input("Digite o novo modelo do veiculo: ")
            novo_ano = input("Digite o novo ano do veiculo: ")
            novo_veiculo = {'placa': novo_placa, 'modelo': novo_modelo, 'ano': novo_ano}
            fucoes.atualizar_veiculo(placa, novo_veiculo)
            print("Veiculo atualizado com sucesso!")
        
        elif opcao == '5':
            placa = input("Digite a placa do veiculo a ser deletado: ")
            fucoes.deletar_veiculo(placa)
            print("Veiculo deletado com sucesso!")

        elif opcao == '6':
            nome = input("Digite o nome do motorista: ")
            idade = input("Digite a idade do motorista: ")
            motorista = {'nome': nome, 'idade': idade}
            fucoes.cadastrar_motorista(motorista)
            print("Motorista cadastrado com sucesso!")

        elif opcao == '7':
            motoristas = fucoes.listar_motoristas()
            print("Lista de Motoristas:")
            for motorista in motoristas:
                print(motorista)

        elif opcao == '8':
            nome = input("Digite o nome do motorista: ")
            motorista = fucoes.consultar_motorista(nome)
            if motorista:
                print("Motorista encontrado:", motorista)
            else:
                print("Motorista nao encontrado.")

        elif opcao == '9':
            nome = input("Digite o nome do motorista a ser atualizado: ")
            novo_nome = input("Digite o novo nome do motorista: ")
            nova_idade = input("Digite a nova idade do motorista: ")
            novo_motorista = {'nome': novo_nome, 'idade': nova_idade}
            fucoes.atualizar_motorista(nome, novo_motorista)
            print("Motorista atualizado com sucesso!")

        elif opcao == '10':
            nome = input("Digite o nome do motorista a ser deletado: ")
            fucoes.deletar_motorista(nome)
            print("Motorista deletado com sucesso!")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opcao invalida!")

if __name__ == "__main__":
    main()
