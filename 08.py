cont=('zero', 'um',"dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartoze","quinze","dzesseis","dezesste","dezoito","dezenov","inte")
while True:
  num=int(input("digite um número de 0 a 20:"))
  if num>0 and num<20:
    break
  print("digite novamente " , end='')
print(f"Voçe digitou o número:{cont[num]}")