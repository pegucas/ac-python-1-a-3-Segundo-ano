Nomes = {"USUARIO"}

resposta = "nao"
Falhas = 0

while resposta != "FIM":
    resposta = input("Coloque o nome ou digite 'fim': ").upper()
    if resposta in Nomes:
        Falhas = Falhas + 1
    elif resposta != "FIM":
        Nomes.add(resposta)

print(sorted(Nomes))
print(f"Ouve {Falhas} tentativas de repetir")
