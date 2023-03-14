class vertice:
    def __init__(self, ch):
        self.chave = ch
        self.conectado = []
    def coloca(self,nch,peso = 0):
        self.conectado.append(nch)
        

def percorre(g,contato, visitados = [],vals = set([100000])):
    visitados.append(g)
    for i in g.conectado:
        if i.chave == contato:
            visitados.pop()
            return len(visitados)
        if i not in visitados:
            vals.add(percorre(i,contato, visitados,vals))
    visitados.pop()
    return min(vals)


lista_g = {}
n = int(input())
for i in range(n):
    ent = input().split()
    if int(ent[0]) not in lista_g.keys():
        idg = vertice(int(ent[0]))
        lista_g[int(ent[0])] = idg
    else:
        idg = lista_g[int(ent[0])]
    if len(ent) > 2:
        for i in ent[2::]:
            i = int(i)
            if i not in lista_g.keys():
                id2 = vertice(i)
                lista_g[i] = id2
                idg.coloca(id2)
            else:
                idg.coloca(lista_g[i])
eu, mussum = input().split()
eu = int(eu)
mussum = int(mussum)
amigos = percorre(lista_g[eu],mussum)
if amigos == 100000:
    print('Forevis alonis...')
else:
    print(amigos)
