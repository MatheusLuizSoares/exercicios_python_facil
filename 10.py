from random import randint

numeros=randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),
print("os valores sorteados foram:", end='')
for n in numeros:
  print(f"{n} ", end='')
  
print(f"\n O maior valor sorteado foi:{max(numeros)}")
print(f"\nO menor valor sorteado foi:{min(numeros)}")