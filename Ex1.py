meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

Pagamentos = [39, 716, 610, 354, 84, 924, 261, 349, 150, 14, 400, 200]

maiorPagamento = max(Pagamentos)
menorPagamento = min(Pagamentos)

posMaior = Pagamentos.index(maiorPagamento)
mesDoMaior = meses[posMaior]
posMenor = Pagamentos.index(menorPagamento)
mesDoMenor = meses[posMenor]

print(f"Maior valor de venda: {maiorPagamento} em reais")
print(f"Que ocorreu no mes {posMaior} ou seja em {mesDoMaior}")

print(f"Menor valor de venda: {menorPagamento} em reais")
print(f"Que ocorreu no mes {posMenor} ou seja em {mesDoMenor}")

media = sum(Pagamentos) / len(Pagamentos)
print(f"A média foi de {media} reais")
