n = input().split()
num_v = int(n[0])
num_e = int(n[1])
c = n[2]
matriz_adj = []
for m in range(num_v):
    matriz_adj.append(num_v*[0])
        
for i in range(num_e):
    ent = [int(x) for x in input().split()]
    if c == 'D':
        matriz_adj[ent[0]-1][ent[1]-1] = ent[2]
    else:
        matriz_adj[ent[0]-1][ent[1]-1] = ent[2]
        matriz_adj[ent[1]-1][ent[0]-1] = ent[2]
for k in matriz_adj:
    for l in k:
        print(f'{l:4}', end = '')
    print()