num=(int(input("Digite um número:")),
     int(input("Digite um número:")),
     int(input("Digite um número:")),
     int(input("Digite um número:")))
print(f'voçe digitou os valores{num} ')
print(f"O valor 9 {num.count(9)}")
if 3 in num:
 print(f"O valor 3 apareceu na {num.index(3)+1} posição")
else:
  print("na tupla não tem o número 3")
for n in num:
  if n%2==0:
   print()
     