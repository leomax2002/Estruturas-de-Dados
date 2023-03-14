class ArvoreBinaria():
    def __init__(self, dado = ''):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura_esq = None
        self.altura_dir = None
        
        
def percorre(raiz):
    resp = ''
    if raiz != None:
        resp = '(' + str(raiz.altura_esq - raiz.altura_dir) + ' '
        resp = resp + percorre(raiz.esq) + ' '
        resp = resp + percorre(raiz.dir) + ')'
    else:
        return '()'
    return resp


def balanceia(raiz):
    if raiz == None:
        return 0
    raiz.altura_esq = balanceia(raiz.esq)
    raiz.altura_dir = balanceia(raiz.dir)
    return 1 + max(raiz.altura_esq,raiz.altura_dir)


def converte(s, raiz):
    ind = 0
    cont = 0
    i = 1
    while s[i] != '(':
        raiz.dado+=s[i]
        i+=1

    for j in range(i,len(s)):
        if s[j] == '(':
            cont+=1
        if s[j] == ')':
            cont-=1
        if cont == 0:
            ind = j
            break
    esq = s[i:ind+1:]
    dir = s[ind+2:len(s)-1:]
    if esq != '()':
        raiz.esq = ArvoreBinaria()
        converte(esq,raiz.esq)
    if dir != '()':
        raiz.dir = ArvoreBinaria()
        converte(dir,raiz.dir)
        
entrada = input()
raiz = ArvoreBinaria()
converte(entrada,raiz)
balanceia(raiz)
print(percorre(raiz))