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
def percorre(raiz):
    resp = ''
    if raiz != None:
        resp = '(' + str(raiz.dado) + ' '
        resp = resp + percorre(raiz.esq) + ' '
        resp = resp + percorre(raiz.dir) + ')'
    else:
        return '()'
    return resp
def mostra(raiz):
    print(percorre(raiz))

mostra(raiz)
       