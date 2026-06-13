from Leia import produto
 
def cadastrar_produto():
 
    produto["nome"] = input("Nome do produto: ")
    produto["preco"] = float(input("Preço: "))
    produto["quantidade"] = int(input("Quantidade: "))
 
    print("Produto cadastrado com sucesso.")
 
 
def exibir_produto():
 
    if len(produto) == 0:
        print("Nenhum produto cadastrado.")
 
    else:
        print("\nPRODUTO")
        print("Nome:", produto["nome"])
        print("Preço:", produto["preco"])
        print("Quantidade:", produto["quantidade"])
 
 
def alterar_preco():
 
    if len(produto) == 0:
        print("Nenhum produto cadastrado.")
 
    else:
        produto["preco"] = float(input("Novo preço: "))
        print("Preço alterado com sucesso.")
 
 
def alterar_quantidade():
 
    if len(produto) == 0:
        print("Nenhum produto cadastrado.")
 
    else:
        produto["quantidade"] = int(input("Nova quantidade: "))
        print("Quantidade alterada com sucesso.")
 
 
def valor_total():
 
    if len(produto) == 0:
        print("Nenhum produto cadastrado.")
 
    else:
        total = produto["preco"] * produto["quantidade"]
 
        print("Valor total em estoque:")
        print(total)
