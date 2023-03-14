class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
    def insere_v(self,id,dado = 0):
        if id not in self.vertices:
            self.vertices[id] = dado
        else:
            self.remove_v(id)
            self.vertices[id] = dado

    def insere_a(self,id_o,id_d):
        if id_o in self.vertices and id_d in self.vertices: 
            self.arestas.append((id_o,id_d))
            self.arestas.append((id_d,id_o))

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
                if i[0] == id_d and i[0] == id_o:
                    self.arestas.remove(i)


    def d_grau(self):
        d = None
        for i in self.arestas:
            self.vertices[i[0]]+=1
        for i in self.vertices.keys():
            if d == None or d > self.vertices[i]:
                d = self.vertices[i]
        if d == None:
            d = 0
        return d
        

    
grafo = Grafo()
n = int(input())
for i in range(n):
    ent = input().split()
    if ent[0] == 'IV':
        grafo.insere_v(ent[1],0)
    if ent[0] == 'IA':
        grafo.insere_a(ent[1],ent[2])
    if ent[0] == 'RV':
        grafo.remove_v(ent[1])
    if ent[0] == 'RA':
        grafo.remove_a(ent[1],ent[2])
print(grafo.arestas)
print(grafo.d_grau())