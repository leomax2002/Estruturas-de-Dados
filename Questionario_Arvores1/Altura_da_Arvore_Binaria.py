def procura(raiz, n = 0):
    if raiz == None:
        return n
    print(n*'__'+str(raiz.dado))
    n+=1
    n_dir = procura(raiz.dir,n)
    n_esq = procura(raiz.esq,n)
    return max(n_dir,n_esq)

def mostra_arvore_e_altura(raiz):
    h = procura(raiz)
    if h == 0:
        print(f'\naltura: {h}')
    else:
        print(f'\naltura: {h-1}')
        