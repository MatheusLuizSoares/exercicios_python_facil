valores=list()
while True:
  n=int(input("Digite um valor"))
  valores.append(n)
  print("O valor adicionado com sucesso")
  cont=input("deseja continuar[S/N]")
  
  if cont in "N/n":
    break
  valores.sort(reverse=True)
if 5 in valores:
  print("O valor 5 está na lista")
else:
  print(") valor 5 não está na lista")
print(f"O valores digitados foram{valores} ")
  