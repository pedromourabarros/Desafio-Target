def inverter_string(string):

  string_invertida = ""
  for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]
  return string_invertida

string = "Olá mundo!"
string_invertida = inverter_string(string)

print(f"A string invertida é: {string_invertida}")
