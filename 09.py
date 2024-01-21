
times = ["Flamengo", "Palmeiras", "Corinthians", "Atletico Mineiro", "Cruzeiro", "Botafogo", "Fluminense", "Botafogo", "Curitiba", "Chapecoense", "Juventude", "Gremio", "Internacional", "ABC", "America", "Sao Paulo", "Monaco", "River"]


print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')

print(f"o Chapecoense está na {times[9]} posição")

print(f"O ABC está na {times.index('ABC')+1} posição")
