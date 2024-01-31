valores=list()
maior=0
menor=0
for i in range(0,5):
  valores.append(input(f"Digite um  valor para a posição {i}: "))
  if i==0:
    maior=menor=valores[i]
  else:
     if valores[i]>maior:
       maior=valores[i]
     if valores[i]<menor:
       menor=valores[i]
     

print(f"você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} ")
print(f'O menor valor digitado foi {menor}')