class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
    def insere_v(self,id,dado):
        self.vertices[id] = dado

    def insere_a(self,id_o,id_d):
        if id_o in self.vertices and id_d in self.vertices: 
            self.arestas.append((id_o,id_d))

    def remove_v(self,id):
        if id in self.vertices:
            for i in self.arestas.copy():
                if id == i[0] or id == i[1]:
                    self.arestas.remove(i)
            del self.vertices[id]

    def remove_a(self,id_o,id_d):
        if id_o in self.vertices:
           for i in self.arestas.copy():
               if i[0] == id_o and i[1] == id_d:
                   self.arestas.remove(i)


    def grau_saida(self,id):
        out = 0
        if id in self.vertices:
            for i in self.arestas:
                if id == i[0]:
                    out+=1
        return out

    def grau_entrada(self,id):
        dent = 0
        if id in self.vertices:
            for i in self.arestas:
                if id == i[1]:
                    dent+=1
        return dent
    
    def alcancavel2(self,u,v,visitados = []):
        caminho = False
        visitados.append(u)
        for i in self.arestas:
            if i[0] == u:
                if i[1] == v:
                    return True
                if i[1] not in visitados:
                    caminho = self.alcancavel2(i[1],v,visitados)
                if caminho:
                    break
        return caminho
    def alcancavel(self,u,v):
        if u in self.vertices and v in self.vertices:
            return self.alcancavel2(u,v,[])
        else:
            return False
grafo = Grafo()
n = int(input())
for i in range(n):
    ent = input().split()
    if ent[0] == 'IV':
        grafo.insere_v(ent[1],ent[2])
    if ent[0] == 'IA':
        grafo.insere_a(ent[1],ent[2])
    if ent[0] == 'RV':
        grafo.remove_v(ent[1])
    if ent[0] == 'RA':
        grafo.remove_a(ent[1],ent[2])
print(grafo.arestas)
print(grafo.alcancavel('A', 'E'))

