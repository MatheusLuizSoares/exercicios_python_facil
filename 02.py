nome = str(input("Digite o seu nome: "))
mas = nome.upper()
minus = nome.lower()
prim = nome.split()[0]  
print(f"Seu nome em maiúsculas é {mas}")
print(f"Seu nome em minúsculas é {minus}")
print("Seu nome tem", len(nome), "letras")
print(f"O seu primeiro nome é {prim} e ele tem {len(prim)} letras")
