def procura(raiz, val, n = 0, flag = - 1):
    if raiz == None:
        return n
    print(n*'__'+str(raiz.dado))
    if val == raiz.dado:
        flag = n
    n+=1
    procura(raiz.dir,val,n, flag)
    procura(raiz.esq,val,n, flag)
    return flag

def mostra_arvore_e_nivel(raiz, n):
    h = procura(raiz, n)
    print(f'\nnivel(raiz, {n}): {h}')