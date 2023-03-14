class nodo:
    def __init__(self, ch = None, com = None, p = None):
        self.chave = ch
        self.comando = com
        self.proximo = p
    
#procurar mínimo valor -> BFS até achar o mais curto
def BFS(origem, objetivo):
    nod_or = nodo(origem)
    fila = [nod_or]
    while fila != []:
        elemento = fila.pop(0)
        aux = str(elemento.chave)
        if elemento.chave != int(aux[::-1]):
            elem_inv = nodo(int(aux[::-1]),'inverte',elemento)
            fila.append(elem_inv)
        elem_dob = nodo(2*elemento.chave,'dobra',elemento)
        fila.append(elem_dob)
        elem_add = nodo(elemento.chave+1,'adiciona',elemento)
        fila.append(elem_add)
        if elem_inv.chave == objetivo or elem_dob.chave == objetivo or elem_add.chave == objetivo:
            break
    return origem
def ler(raiz, coms = []):
    if raiz == None:
        return coms
    coms.append(raiz.comando)


def destravarPainel(painel, origem, objetivo):
    abrir = BFS(origem, objetivo)
    comandos = ler(abrir)
    if abrir != None:
        for i in abrir:
            if i == 'inverte':
                painel.inverterValor()
            if i == 'dobra':
                painel.dobrarValor()
            if i == 'adiciona':
                painel.incrementarValor()
    return painel.abrirArtefato()