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
                
def pre(raiz):
    if raiz != None:
        print(raiz.dado, end = ' ')
        pre(raiz.esq) 
        pre(raiz.dir)

def inf(raiz):
    if raiz != None:
        inf(raiz.esq) 
        print(raiz.dado, end = ' ')
        inf(raiz.dir)

def pos(raiz):
    if raiz != None:
        pos(raiz.esq) 
        pos(raiz.dir)
        print(raiz.dado, end = ' ')

arv = ABB()
while True:
    n = input()
    if n == 'quack':
        break
    elif n == 'in':
        inf(arv.raiz)
        print()
    elif n == 'pre':
        pre(arv.raiz)
        print()
    elif n == 'pos':
        pos(arv.raiz)
        print()
    else:
        arv.coloca(int(n))
