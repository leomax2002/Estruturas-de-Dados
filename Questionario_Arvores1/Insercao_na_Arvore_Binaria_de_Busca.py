class ABB:
    def __init__(self):
        self.raiz = None
    def coloca(self,dado):
        if self.raiz:
            self.posiciona(dado,self.raiz)
        else:
            self.raiz = nodo(dado)
    def posiciona(self,dado,nod):
        if dado <= nod.dado:
            if nod.esq != None:
                self.posiciona(dado,nod.esq)
            else:
                nod.esq = nodo(dado)
        else:
            if nod.dir != None:
                self.posiciona(dado,nod.dir)
            else:
                nod.dir = nodo(dado)
        
class nodo:
    def __init__(self,val,e = None, d = None):
        self.dado = val
        self.esq = e
        self.dir = d
        
              
        
def percorre(raiz):
    resp = ''
    if raiz != None:
        resp = '(' + str(raiz.dado) + ' '
        resp = resp + percorre(raiz.esq) + ' '
        resp = resp + percorre(raiz.dir) + ')'
    else:
        return '()'
    return resp
vals = []
n = int(input())
arv = ABB() 
if n > 0:
    valores = [int(x) for x in input().split()]
    for i in valores:
        arv.coloca(i)
print(percorre(arv.raiz))