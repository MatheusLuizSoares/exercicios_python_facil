valores=list()
while True:
  numero=int(input("digite um valor:"))
  if numero not in valores:
    valores.append(numero)
    print("Valor adicionado com sucesso")
  else:
    print("Valor duplicado!não será adicioionado") 
  conti=(input("Quer continuar? [S/N]"))
  if conti in "Nn":
    break
valores.sort()
print(f"Você digitou os valores:{valores}")
    
  
  
  
  