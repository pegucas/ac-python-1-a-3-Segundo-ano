from Luke import *
 
opcao = 0
 
while opcao != 6:
 
    print("\nMENU")
    print("1 - Cadastrar produto")
    print("2 - Exibir produto")
    print("3 - Alterar preço")
    print("4 - Alterar quantidade")
    print("5 - Calcular valor total em estoque")
    print("6 - Encerrar sistema")
 
    opcao = int(input("Escolha uma opção: "))
 
    if opcao == 1:
        cadastrar_produto()
 
    elif opcao == 2:
        exibir_produto()
 
    elif opcao == 3:
        alterar_preco()
 
    elif opcao == 4:
        alterar_quantidade()
 
    elif opcao == 5:
        valor_total()
 
    elif opcao == 6:
        print("Programa encerrado.")
 
    else:
        print("Opção inválida.")
