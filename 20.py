galera=list()
dados=list()
totalma=totalme=0
for c in range(0,3):
  dados.append(str(input('Nome:')))
  dados.append(int(input("Idade:")))
  galera.append(dados[:])
  dados.clear()
for p in galera:
  if p[1]>=18:
    print(f"{p[0]} é maior de idade")
    totalma+=1
  else:
    print(f"{p[0]} é menor de idade")
    
print(f"temos {totalma} maiores e {totalme} menores de idade")
