n = int(input())
notas = []
for i in range(n):
    nota = float(input())
    notas.append(nota)

for j in range(1, len(notas)):
    nota_atual = notas[j]
    aux = j
    while aux > 0 and notas[aux-1] > nota_atual:
        notas[aux] = notas[aux-1]
        aux-=1
    notas[aux] = nota_atual

mediana = ((len(notas)+1)//2) - 1

print(f'{notas[0]:.2f}')
print(f'{notas[mediana]:.2f}')
print(f'{notas[len(notas)-1]:.2f}')
