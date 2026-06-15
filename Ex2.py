Assentos = (
    "1A", "1B", "1C",
    "2A", "2B", "2C",
    "3A", "3B", "3C",
    "4A", "4B", "4C",
    "5A", "5B", "5C",
    "6A", "6B", "6C",
    "7A", "7B"
)

Livre = 0
Ocupado = 1

Ocupacao = (
    Livre, Ocupado, Livre,
    Ocupado, Livre, Ocupado,
    Ocupado, Ocupado, Livre,
    Livre, Livre, Ocupado,
    Ocupado, Livre, Livre,
    Ocupado, Ocupado, Ocupado,
    Ocupado, Livre
)

print("Estes são todos os nossos assentos")
print(Assentos)
print("-" * 45)

Livres = 0
print("Estes são os livres: ")
for i in range(len(Ocupacao)):
    if Ocupacao[i] == Livre:
        Livres = Livres + 1
        AssentoLivre = Assentos[i]
        print(f"O assento {AssentoLivre} está livre para ser usado")
        print("-" * 39)

print("-" * 45)

Ocupados = 0
print("Estes são os ocupados: ")
for i in range(len(Ocupacao)):
    if Ocupacao[i] == Ocupado:
        Ocupados = Ocupados + 1
        AssentoOcupado = Assentos[i]
        print(f"O assento {AssentoOcupado} está ocupado")
        print("-" * 39)

print(f"De todos os assentos {Livres} estão livres e {Ocupados} estão ocupados")

pergunta = input("Voce quer pesquisar os Status de um assento? (S/N): ").upper()
if pergunta == "S":

    Pesquisa = input("Qual o assento que voce gostaria (Numero + Letra): ")

    if Pesquisa in Assentos:
        print("O assento existe e está: ")
        Ocup = Assentos.index(Pesquisa)
        LivreOuNao = Ocupacao[Ocup]
        
        if LivreOuNao == 0:
            print("LIVRE")
        else:
            print("OCUPADO")

    else:
        print("O assento requerido não existe")

else:
    print("Saindo...")
