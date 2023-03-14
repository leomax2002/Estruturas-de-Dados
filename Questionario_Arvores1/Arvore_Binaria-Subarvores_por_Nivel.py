class BinaryTree:
    def __init__(self,rootObj):
        self.dado = rootObj
        self.esq = None
        self.dir = None

    def insertLeft(self,newNode):
        if self.esq == None:
            self.esq = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.esq = self.esq
            self.esq = t

    def insertRight(self,newNode):
        if self.dir == None:
            self.dir = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.dir = self.dir
            self.dir = t


    def getRightChild(self):
        return self.dir

    def getLeftChild(self):
        return self.esq

    def setRootVal(self,obj):
        self.dado = obj

    def getRootVal(self):
        return self.dado

raiz = BinaryTree(1)
raiz.insertLeft(2)
raiz.insertRight(4)
raiz.insertRight(3)
def percorre(raiz, n, nivel_atual = 0):
    resp = ''
    if raiz != None:
        if nivel_atual >= n:
            resp = '(' + str(raiz.dado) + ' '
            resp = resp + percorre(raiz.esq, n, nivel_atual+1) + ' '
            resp = resp + percorre(raiz.dir, n, nivel_atual+1) + ')'
        else:
            resp = percorre(raiz.esq, n, nivel_atual+1)
            if resp == '()':
                resp = ''
                resp = percorre(raiz.dir, n, nivel_atual+1)
            else:
                aux = percorre(raiz.dir, n, nivel_atual+1)
                if aux == '()':
                    pass
                else:
                    resp =resp + '\n' + aux
    else:
        return '()'
    return resp

def mostra_nivel(raiz, n):
    print(percorre(raiz, n))

mostra_nivel(raiz,1)