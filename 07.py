from datetime import date
ano=int(input("Digite um ano ano:"))
if ano==0:
    ano= date.today().year
if ano % 4 ==0 and ano % 100 !=0 or ano %400==0:
  print(f"O ano {ano} é Bissexto")
else:
  print (f"O ano {ano} não é Bissexto")