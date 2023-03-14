class deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
def exibe_candidatos(deque, pos, ordem):
    cont_inicio = 0
    cont_fim = deque.size()-1
    if (ordem == 'direta' and pos >= 0 and pos <= deque.size()-1):
        while not deque.is_empty():
            nome = deque.remove_front()
            if(cont_inicio < pos):
                pass
            else:
                print(nome)
            cont_inicio+=1
    elif(ordem == 'inversa' and pos >= 0 and pos <= deque.size()-1):
        while not deque.is_empty():
            nome = deque.remove_rear()
            if(cont_fim > pos):
                pass
            else:
                print(nome)
            cont_fim-=1
    else:
        return None
deque = deque()
deque.add_rear('Obi-Wan Kenobi')
deque.add_rear('Leia Skywalker')
deque.add_rear('Chewbacca')
deque.add_rear('Boba Fett')
deque.add_rear('Yoda')
deque.add_rear('Anakin Skywalker')
deque.add_rear('Darth Vader')
deque.add_rear('Ben Solo')
deque.add_rear('Kylo Ren')
deque.add_rear('Luke Skywalker')
deque.add_rear('Leia Organa')
deque.add_rear('R2-D2')
deque.add_rear('C-3PO')
deque.add_rear('BB-8')
deque.add_rear('Han Solo')
deque.add_rear('Padmé Amidala')
deque.add_rear('Mace Windu')
deque.add_rear('Qui-Gon Jinn')
deque.add_rear('Vice Almirante Holdo')
deque.add_rear('Rose Tico')
deque.add_rear('Poe Dameron')
deque.add_rear('Lando Calrissian')
deque.add_rear('Darth Maul')
deque.add_rear('Red Boba Fett')
deque.add_rear('Jabba, the Hutt')
deque.add_rear('Jango Fett')
deque.add_rear('Conde Dooku')
deque.add_rear('Darth Tyranus')
deque.add_rear('General Grievous')
deque.add_rear('Sheev Palpatine')
deque.add_rear('Darth Sidious')
deque.add_rear('Finn')
deque.add_rear('Maz Kanata')
deque.add_rear('Rey Palpatine')
deque.add_rear('Rey Skywalker')
deque.add_rear('Ben Solo')
deque.add_rear('Kylo Ren')
deque.add_rear('Líder Supremo Snoke')
exibe_candidatos( deque, 0, 'inversa' )
