from heapq import heappush, heappop

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
        
            
    def insere_v(self,id,dado = float('inf'), pai = None):
        self.vertices[id] = (dado,pai)
        self.arestas[id] = []

    def insere_a(self,id_o,id_d,p):
        self.arestas[id_o].append((id_d,p))
    
    def ligado(self,id):
        conect = []
        if id in self.vertices:
            for i in self.arestas:
                if id == i[0]:
                    conect.append((i[1],i[2]))
        return conect 

def menor_caminho(g,ch):
    tamanho_encanamento = 0                  
    visitados = set()            
    inicio = ch   
    nao_visitados = [(0, inicio)]   
    while nao_visitados:
        peso, atual = heappop(nao_visitados)
        if atual not in visitados:
            visitados.add(atual)
            tamanho_encanamento += peso
            for proximo, peso in g.arestas[atual]:
                if proximo not in visitados:
                    heappush(nao_visitados, (peso, proximo))
    return tamanho_encanamento
        
g = Grafo()
n = int(input())
for i in range(n):
    ent = input().split()
    tmp = int(ent[0])
    if tmp not in g.vertices.keys():
        g.insere_v(tmp)
    if len(ent) > 2:
        aux = ent[2::]
        for i in range(0,len(aux),2):
            tmp = int(aux[i+1])
            tmp2 = int(aux[i])
            if tmp not in g.vertices.keys():
                g.insere_v(tmp)
                g.insere_a(int(ent[0]),tmp,tmp2)
            else:
                g.insere_a(int(ent[0]),tmp,tmp2)

aux = next(iter(g.vertices))
menor = menor_caminho(g,aux)*3.14
print(f'R$ {menor:.2f}')
