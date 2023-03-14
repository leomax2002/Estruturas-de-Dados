n = int(input())
casas = [int(x) for x in input().split()]
aux = []
for i in casas:
    cont = 0
    for j in casas:
        cont+=(abs(i-j))
    aux.append(cont)
menor_dist = min(aux)
pizzopato = casas[aux.index(menor_dist)]
distancia_minima = 0
for i in casas:
    distancia_minima+=abs(i - pizzopato)
print(int(distancia_minima))