def dist_alt(x):
    return x[2]
import time
t = time.time()
def pes(x):
    if x[3] == 0:
        return -1000
    if x[3] < 0:
        return abs(x[3])
    if x[3] > 0:
        return x[3]+1000
    return abs(x[3])

def sobrenome(x):
        return x[1]
    
def nome(x):
    return x[0]

n = int(input())
cavalheiros = []
alt_sep = []
pes_sep = []
sob_sep = []
for i in range(n):
    pretendente = input().split()
    pretendente[2], pretendente[3] = abs(int(pretendente[2])-180), (int(pretendente[3])-75)
    pretendente = tuple(pretendente)
    alt_sep.append(pretendente[2])
    pes_sep.append(pretendente[3])
    sob_sep.append(pretendente[1])
    cavalheiros.append(pretendente)

cavalheiros.sort(key = dist_alt)
for i in set(alt_sep):
    aux = [j for j, x in enumerate(cavalheiros) if x[2] == i]
    if len(aux) > 1:
        cavalheiros[aux[0]:aux[len(aux)-1]+1:] = sorted(cavalheiros[aux[0]:aux[len(aux)-1]+1:],key = pes)
    for k in set(pes_sep):
        aux_2 = [j for j, x in enumerate(cavalheiros) if x[3] == k and x[2] == i]
        if len(aux_2) > 1:
            cavalheiros[aux_2[0]:aux[len(aux_2)-1]+1:] = sorted(cavalheiros[aux_2[0]:aux_2[len(aux_2)-1]+1:],key = sobrenome)
        for l in set(sob_sep):
            aux_3 = [j for j, x in enumerate(cavalheiros) if x[1] == l and x[2] == i and x[3] == j]
            if len(aux_3) > 1:
                cavalheiros[aux_3[0]:aux[len(aux_3)-1]+1:] = sorted(cavalheiros[aux_3[0]:aux_3[len(aux_3)-1]+1:],key = nome)

[print(k[1] + ', ' + k[0]) for k in cavalheiros]
f = time.time()
print(f-t,'s')
