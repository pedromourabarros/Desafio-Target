def calcular_soma(indice):
  soma = 0
  for i in range(1, indice + 1):
    soma += i
  return soma

indice = 13
soma = calcular_soma(indice)

print(f"O valor da variável SOMA é {soma}")
