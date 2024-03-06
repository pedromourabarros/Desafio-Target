import time

def ligar_interruptor(numero_interruptor):

  print(f"Ligando o interruptor {numero_interruptor}")

def desligar_interruptor(numero_interruptor):

  print(f"Desligando o interruptor {numero_interruptor}")

def ir_sala_lampadas():

  print("Indo para a sala das lâmpadas...")

def tocar_lampadas():

  print("Tocando nas lâmpadas...")

  return [1, 3] 

def descobrir_interruptores():


  # Ligue o interruptor 1 por 1 minuto
  ligar_interruptor(1)
  time.sleep(60)

  # Desligue o interruptor 1 e ligue o interruptor 2
  desligar_interruptor(1)
  ligar_interruptor(2)

  # Vá para a sala das lâmpadas e toque nas lâmpadas
  ir_sala_lampadas()
  lampadas_quentes = tocar_lampadas()

  # Imprima o resultado
  for i in range(1, 4):
    if i in lampadas_quentes:
      print(f"O interruptor {i} controla a lâmpada {i}")
    else:
      print(f"O interruptor {i} controla a lâmpada {3 - i}")

def main():

  descobrir_interruptores()

if __name__ == "__main__":
  main()
