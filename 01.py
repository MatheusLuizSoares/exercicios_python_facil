n1=int(input("informe um valor  até 9999:"))
u=n1//1 %10
d=n1//10 %10
c=n1//100 %10
m=n1//1000 %10
print("Analisando o número {}". format(n1))
print("unidade:{}".format(u))
print("Dezena: {}".format(d))
print("centena: {}".format(c))
print("Milhar: {}".format(m))

