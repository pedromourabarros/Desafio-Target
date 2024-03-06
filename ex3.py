def completar_sequencia(sequencia):

  # Lógica para cada sequência
  if len(sequencia) <= 2:
    return sequencia[-1] + 1
  elif sequencia[1] == sequencia[0] * 2:
    return sequencia[-1] * 2
  elif sequencia[1] == sequencia[0] ** 2:
    return (sequencia[-1] + 1) ** 2
  elif sequencia[0] == 0 and sequencia[1] == 1:
    return sequencia[-2] + sequencia[-1]
  elif sequencia[1] - sequencia[0] == 2:
    return sequencia[-1] + 2
  else:
    # Diferença constante
    diferenca = sequencia[1] - sequencia[0]
    return sequencia[-1] + diferenca

def main():
  # Sequências
  sequencias = [
    [1, 3, 5, 7],
    [2, 4, 8, 16, 32, 64],
    [0, 1, 4, 9, 16, 25, 36],
    [4, 16, 36, 64],
    [1, 1, 2, 3, 5, 8],
    [2, 10, 12, 16, 17, 18, 19],
  ]

  # Encontra o próximo elemento de cada sequência
  for i, sequencia in enumerate(sequencias):
    proximo_elemento = completar_sequencia(sequencia)
    print(f"Sequência {i + 1}: {sequencia}, {proximo_elemento}")

if __name__ == "__main__":
  main()