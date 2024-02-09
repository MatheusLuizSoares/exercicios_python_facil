lista_inteiro=list()
list_pares=list()
lis_impares=list()
while True:
  numero=(int(input("Digite um número:")))
  lista_inteiro.append(numero)
  if numero%2 ==0:
   list_pares.append(numero) 
  else:
   lis_impares.append(numero) 
  
  cont=input("Quer continuar [S/N]")
  if cont in "N/n":
    break
print(f"Lista inteiro é {lista_inteiro}")
print(f"Lista pares é {list_pares}")
print(f"Lista impares é {lis_impares}")