def quadrado_perfeito(lista):
    if len(lista) == 1:
        print(f'{lista[0]}')
        return lista[0]
    else:
        print(f'{lista[0]} + soma({lista[1::]})')
        return lista[0] + quadrado_perfeito(lista[1::])
n = int(input())
lista = []
for i in range(1, n+1):
    lista.append(2*i-1)
v = quadrado_perfeito(lista)
print('---------------')
print(f'{n} ** 2 == {v}')