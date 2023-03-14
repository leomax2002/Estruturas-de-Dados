class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def procura(raiz, val, n = 0, flag = -1):
    if raiz == None:
        return -1
    if raiz.dado == val:
        return n
    n+=1
    n_esq = procura(raiz.dir,val,n,flag)

    n_dir = procura(raiz.esq,val,n,flag)
    return max(n_esq,n_dir)

def nivel(raiz, n):
    return procura(raiz,n)

def procura_catarvore(raiz,v1,pai_v1 = []):
    if raiz == None:
        return []
    if raiz.dado == v1:
        return pai_v1
    pai_v1.append(raiz)
    p_dir = procura_catarvore(raiz.dir,v1,pai_v1)
    p_esq = procura_catarvore(raiz.esq,v1,pai_v1)
    return (p_dir,p_esq)


def verificaPontuacao(raiz,v1,v2):
    nivel_v1 = nivel(raiz,v1)
    nivel_v2 = nivel(raiz,v2)
    if nivel_v1 > nivel_v2:
        filho = v2
    else:
        filho = v1
    #print(nivel_v1)
    #print(nivel_v2)
    pai_1 = procura_catarvore(raiz,v1)
    pai_2 = procura_catarvore(raiz,v2)
    print(pai_1)
    #print(pai_2)
    return procura_catarvore(raiz,v1,v2)

raiz = ArvoreBinaria(1, ArvoreBinaria(4, ArvoreBinaria(5), ArvoreBinaria(0)), ArvoreBinaria(6, ArvoreBinaria(3), ArvoreBinaria(2)))
print(verificaPontuacao(raiz, 3, 2))  
