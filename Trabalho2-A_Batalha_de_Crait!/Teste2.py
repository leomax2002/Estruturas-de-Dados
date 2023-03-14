class arvore_de_decisao:
    def __init__(self,l = None, m = None, e = None, d = None):
        self.letra_alfabeto = l
        self.letra_morse = m
        self.esq = e
        self.dir = d

def constroi_alfabeto(raiz,no, morse,s, nivel):
    if s == morse:
        return None
    if morse[nivel] == '.':
        s+='.'
        if raiz.esq == None:
            if s != morse:
                nodo = arvore_de_decisao(None,s)
            else:
                nodo = arvore_de_decisao(no,s)
            raiz.esq = nodo
        else:
            if s == morse and raiz.esq.letra_alfabeto == None:
                raiz.esq.letra_alfabeto = no 
        return constroi_alfabeto(raiz.esq,no, morse,s,nivel+1)
    else:
        s+='-'
        if raiz.dir == None:
            if s != morse:
                nodo = arvore_de_decisao(None,s)
            else:
                nodo = arvore_de_decisao(no,s)
            raiz.dir = nodo
        else:
            if s == morse and raiz.dir.letra_alfabeto == None:
                raiz.dir.letra_alfabeto = no 
        return constroi_alfabeto(raiz.dir,no,morse,s,nivel+1)
    
def exibe_alfabeto(raiz):
    global alfabeto
    nao_visitados = []
    nao_visitados.append(raiz)
    while nao_visitados != []:
        no_atual = nao_visitados.pop(0)
        if no_atual.letra_alfabeto != None:
            alfabeto+=' '+ no_atual.letra_alfabeto
        else:
            if alfabeto == '':
                alfabeto+='*'
            else:
                alfabeto+=' *'
        if no_atual.esq != None:
            nao_visitados.append(no_atual.esq)
        if no_atual.dir != None:
            nao_visitados.append(no_atual.dir)
            

def decodifica(codigo,chave):
    pal = ''
    decod = ''
    mensagem_original = ''
    for i in codigo:
        if i == ' ' or mensagem_original == codigo[:len(codigo)-1:]:
            if mensagem_original == codigo[:len(codigo)-1:]: #Trecho feito para os casos de teste no .zip. Retirar no código final
                pal+=i
            if pal not in chave.keys():
                decod = 'Impossível decodificar a mensagem!'
                break
            decod+= chave[pal]
            pal = ''
        elif i == '/':
            decod+=' '
        else:
            pal+=i
        mensagem_original+=i
    return decod

def codifica(codigo, chave):
    cod = ''
    anterior = None
    for i in codigo:
        if i != ' ':
            if i not in chave.keys():
                cod = 'Impossível codificar a mensagem!'
                break
            cod+= chave[i] + ' '
        else:
            if anterior != ' ':
                cod+= '/'
        anterior = i
    return cod





nome_arquivo_entrada = '10.in'
nome_arquivo_saida = '10.out'

with open(nome_arquivo_entrada, 'r') as arquivo:
    print('Entrada:')
    print(arquivo.read()+'\n')


res = []

chave_de_conversao_morse = {}
chave_de_conversao_alfabeto = {}
aux = []
alfabeto = ''
raiz = arvore_de_decisao()

with open(nome_arquivo_entrada, 'r') as arquivo:
    entrada = arquivo.read().split('\n')
    n = int(entrada[0])
    for ent in entrada[1:len(entrada)-2:]:
        comando = ent.split()
        letra,codigo = comando
        chave_de_conversao_morse[codigo] = letra
        chave_de_conversao_alfabeto[letra] = codigo
        constroi_alfabeto(raiz,letra, codigo, '',0)

    cod_decod = int(entrada[len(entrada)-2])
    codigo = entrada[len(entrada)-1]

    if cod_decod == 0:
        v = decodifica(codigo,chave_de_conversao_morse)
        print(v)
        res.append(v)
    else:
        v = codifica(codigo,chave_de_conversao_alfabeto)
        print(v)
        res.append(v[:len(v)-1:])

    if v != 'Impossível codificar a mensagem!' and v != 'Impossível decodificar a mensagem!':   
        exibe_alfabeto(raiz)
        print(alfabeto)
        res.append(alfabeto)

resp = []
with open(nome_arquivo_saida, 'r') as arquivo:
    print('\nsaida:')
    aux = arquivo.read()
    print(aux)
    resp.append(aux.split('\n'))
    
with open(nome_arquivo_saida, 'r') as arquivo:
    print('\nComparacao:')
    i = 0
    for comp in arquivo.readlines():
        if comp.strip('\n') == res[i]:
            print('Igual')
        else:
            print('Diferente')
        i+=1  