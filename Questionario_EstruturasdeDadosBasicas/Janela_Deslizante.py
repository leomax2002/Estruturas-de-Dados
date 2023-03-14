class deque:
    def __init__(self):
        self.items = []
    def vazio(self):
        return self.items == []
    def colocar_frente(self, item):
        self.items.append(item)
    def colocar_atras(self, item):
        self.items.insert(0,item)
    def retirar_frente(self):
        return self.items.pop()
    def retirar_atras(self):
        return self.items.pop(0)
    def tamanho(self):
        return len(self.items)
deque = deque()
n = int(input())
lista = [int(x) for x in input().split()]
k = int(input())
for i in range(n):
    deque.colocar_frente(i)
    if deque.tamanho() >= k:
        ind = deque.retirar_frente()
        print(max(lista[ind - (k-1):ind+1]), end = ' ')
        ind = deque.colocar_frente(ind)