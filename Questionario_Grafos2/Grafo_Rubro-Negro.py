class vertice:
    def __init__(self, ch, c = None):
        self.chave = ch
        self.conectado = []
        self.cor = c
    def coloca(self,nch,peso = 0):
        self.conectado.append(nch)
        

def rb(g, visitados = []):
    val = False
    visitados.append(g)
    if g.cor == None:
        g.cor = 'r'
    for i in g.conectado:
        if i.cor == None:
            if g.cor == 'r':
                i.cor = 'n'
            else:
                i.cor = 'r'
        if i.cor == g.cor:
            return True
        if i not in visitados:
            val = rb(i,visitados)
        if val:
            break
    return val


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
rubro_negro = False
for j in lista_g:

    rubro_negro = rb(lista_g[j])
    if rubro_negro:
        print('Mais cor, por favor!')
        break
if not rubro_negro:
    print('Lerei "O Vermelho e o Negro".')