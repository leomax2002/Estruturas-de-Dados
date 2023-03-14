class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def procura_catarvore(raiz,v1,pai_v1 = []):
    if v1 in pai_v1:
        return pai_v1
    if raiz == None:
        return
    if raiz.dado == v1:
        pai_v1.append(raiz.dado)
        return
    pai_v1.append(raiz.dado)
    procura_catarvore(raiz.dir,v1,pai_v1)
    procura_catarvore(raiz.esq,v1,pai_v1)
    if v1 not in pai_v1:
        pai_v1.pop()
    return pai_v1
    
    



def verificaPontuacao(raiz,v1,v2):
    pai_1 = procura_catarvore(raiz,v1, pai_v1= [])
    pai_2 = procura_catarvore(raiz,v2, pai_v1 = [])
    i = 0
    val = None
    if pai_1 == None or pai_2 == None:
        return raiz.dado
    menor = min(len(pai_1),len(pai_2))
    for i in range(menor):
        if pai_1[i] == pai_2[i]:
            val = pai_2[i]
            i+=1
        else:
            break
    return val

raiz = ArvoreBinaria(1, ArvoreBinaria(4, ArvoreBinaria(5), ArvoreBinaria(0)), ArvoreBinaria(6, ArvoreBinaria(3), ArvoreBinaria(2)))
print(verificaPontuacao(raiz, 5, 6))