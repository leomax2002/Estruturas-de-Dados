def procura(raiz, val, n = 0, flag = -1):
    if raiz == None:
        return -1
    if raiz.dado == val:
        return n
    n+=1
    return max(procura(raiz.dir,val,n,flag), procura(raiz.esq,val,n,flag))

def nivel(raiz, n):
    return procura(raiz,n)