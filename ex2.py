def fibonacci(n):
  if n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    fib = [0, 1]
    for i in range(2, n + 1):
      fib.append(fib[i - 1] + fib[i - 2])
    return fib

def main():
  numero = int(input("Informe um número: "))
  sequencia = fibonacci(numero)

  if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()
