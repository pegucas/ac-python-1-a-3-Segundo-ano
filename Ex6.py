veiculo = {}
valorFinal = 0

veiculo["marca"] = input("Nome do veículo: ")
veiculo["modelo"] = input("Modelo: ")
veiculo["Ano"] = int(input("Ano: "))
veiculo["cor"] = input("Cor: ")
veiculo["valor"] = float(input("Valor: "))

print("\nInformações do veículo:")
print(veiculo)

if veiculo["Ano"] < 2000:
    print("O veículo é antigo.")
else:
    print("O veículo é moderno.")

if veiculo["valor"] > 100000:
    desconto = veiculo["valor"] * 0.1
    valorFinal = veiculo["valor"] - desconto
    print("Desconto de 10% aplicado ao veículo")
else:
    valorFinal = veiculo["valor"]
    print("Nenhum desconto aplicado ao veículo")

print(f"Valor final do veículo: R${valorFinal:.2f}")
