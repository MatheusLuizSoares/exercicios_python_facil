from random import randint
from time import sleep
computador=randint(0,5)

print('-=-'*20)
print("Vou pensar em um número entre de 0 até 5. Tente adivinhar...")
print('-=-'*20)

jogador=int(input("Adivinhe um número que eu pensei: "))

print("Processando...")
sleep(3)
if jogador==computador:
  print("Parabens, você acertou meu número")
else:
  print(f"Errou, meu numero não era {jogador}, era {computador}.Tente novamente")