def modulo_2(x):
    if x >= 0:
        val = x%2
    else:
        val = -1*(abs(x)%2)
    return val
def modulo(x):
    if x >= 0:
        val = x%k
    else:
        val = -1*(abs(x)%k)
    lista_mod.append(val)
    return val
n, k = [int(x) for x in input().split()]
lista = []
for i in range(n):
    num = int(input())
    lista.append(num)
lista_mod = []
lista_ord = sorted(lista, key = modulo, reverse = True)
lista_mod.sort(reverse = True)
for i in sorted(set(lista_mod), reverse = True):
    if lista_mod.count(i) > 1:
        aux = [j for j, x in enumerate(lista_mod) if x == i]
        for k in aux[1::]:
            for l in aux[1::]:
                if modulo_2(lista_ord[l-1]) != 0 and modulo_2(lista_ord[l]) == 0:
                    lista_ord[l-1],lista_ord[l] = lista_ord[l], lista_ord[l-1]
                elif modulo_2(lista_ord[l-1]) == 0 and modulo_2(lista_ord[l]) == 0 and lista_ord[l-1] < lista_ord[l]:
                    lista_ord[l-1],lista_ord[l] = lista_ord[l], lista_ord[l-1]
                elif modulo_2(lista_ord[l-1]) != 0 and modulo_2(lista_ord[l]) != 0 and lista_ord[l-1] > lista_ord[l]:
                    lista_ord[l-1],lista_ord[l] = lista_ord[l], lista_ord[l-1]
        
[print(x,end = ' ') for x in lista_ord]