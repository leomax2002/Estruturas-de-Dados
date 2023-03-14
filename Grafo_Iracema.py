class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
    def insere_v(self,id,dado):
        self.vertices[id] = dado
        self.arestas[id] = []

    def insere_a(self,id_o,id_d):
        if id_o in self.vertices and id_d in self.vertices: 
            self.arestas[id_o] = self.arestas[id_o] + [id_d]

    def remove_v(self,id):
        if id in self.vertices:
            del self.arestas[id]
            for i in self.arestas.keys():
                if id in self.arestas[i]:
                    self.arestas[i].remove(id)
            del self.vertices[id]

    def remove_a(self,id_o,id_d):
        if id_o in self.arestas:
           for i in self.arestas[id_o]:
               if i == id_d:
                   self.arestas[id_o].remove(id_d)


    def grau_saida(self,id):
        if id in self.vertices:
            return len(self.arestas[id])
        else:
            return 0

    def grau_entrada(self,id):
        dent = 0
        if id in self.vertices:
            for i in self.arestas.keys():
                if id in self.arestas[i]:
                    dent+=self.arestas[i].count(id)
        return dent
    
    def alcancavel2(self,u,v,visitados = []):
        caminho = False
        visitados.append(u)
        for i in self.arestas[u]:
            if i == v:
                return True
            if i not in visitados:
                caminho = self.alcancavel2(i,v,visitados)
            if caminho:
                break
        return caminho
    def alcancavel(self,u,v):
        return self.alcancavel2(u,v,[])