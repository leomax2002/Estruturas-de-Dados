class vertice:
    def __init__(self, ch):
        self.chave = ch
        self.conectado = []
    def coloca(self,nch,peso = 0):
        self.conectado.append(nch)
        
        
def ciclo(vertice, pais = [], visitados = []):
    pais.append(vertice)
    visitados.append(vertice)
    for i in vertice.conectado:
        if i in pais:
            return True
        if i not in visitados:
            ciclo(i,pais)
    pais.pop()
    return False
     
lista_vert = {}
n = int(input())
for i in range(n):
    ent = input().split()
    if ent[0] not in lista_vert.keys():
        id = vertice(ent[0])
        lista_vert[ent[0]] = id
    else:
        id = lista_vert[ent[0]]
    if len(ent) > 2:
        for i in ent[2::]:
            if i not in lista_vert.keys():
                id2 = vertice(i)
                lista_vert[i] = id2
                id.coloca(id2)
            else:
                id.coloca(lista_vert[i])
    
for j in lista_vert:
    c = ciclo(lista_vert[j])
    if c:
        print('Hoje tem!')
        break
if not c:
    print('... que ama ninguem.')