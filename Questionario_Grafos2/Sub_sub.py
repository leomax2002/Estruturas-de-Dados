class vertice:
    def __init__(self, ch):
        self.chave = ch
        self.conectado = {}
    def coloca(self,nch,peso = 0):
        v = nch.chave
        self.conectado[v] = nch
        

def sub(g1,g2, visitados = []):
    visitados.append(g2)
    for i in g2.conectado:
        if i not in g1.conectado:
            return True
        if g2.conectado[i] not in visitados:
            sub(g1.conectado[i],g2.conectado[i],visitados)
    return False


lista_g1 = {}
n = int(input())
for i in range(n):
    ent = input().split()
    if int(ent[0]) not in lista_g1.keys():
        idg = vertice(int(ent[0]))
        lista_g1[int(ent[0])] = idg
    else:
        idg = lista_g1[int(ent[0])]
    if len(ent) > 2:
        for i in ent[2::]:
            i = int(i)
            if i not in lista_g1.keys():
                id2 = vertice(i)
                lista_g1[i] = id2
                idg.coloca(id2)
            else:
                idg.coloca(lista_g1[i])

esp = input()
lista_g2 = {}
n2 = int(input())
for i in range(n2):
    ent = input().split()
    if int(ent[0]) not in lista_g2.keys():
        idg = vertice(int(ent[0]))
        lista_g2[int(ent[0])] = idg
    else:
        idg = lista_g2[int(ent[0])]
    if len(ent) > 2:
        for i in ent[2::]:
            i = int(i)
            if i not in lista_g2.keys():
                id2 = vertice(i)
                lista_g2[i] = id2
                idg.coloca(id2)
            else:
                idg.coloca(lista_g2[i])
gf = False
for j in lista_g2:
    if j in lista_g1:
        gf = sub(lista_g1[j],lista_g2[j])
    else:
        gf = True
        print('Ue? Ue? Ue?')
        break
    if gf:
        print('Ue? Ue? Ue?')
        break
if not gf:
    print('Sub-sub!')