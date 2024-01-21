palavras=("aprender","programar","python","futuro","estudar","trabalhar","gratis","pratica")

for p in palavras:
  print(f"\nna palavra {p} temos")
  for letra in p:
    if letra.lower() in 'aeiou':
      print(letra,end="")