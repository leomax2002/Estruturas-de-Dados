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
s = input()
res = deque()
for i in s:
    if(i in '0123456789'):
        res.add_front(i)
    elif(i == '*'):
        print(res.remove_rear(),end = '')
    elif(i == '+'):
        print(res.remove_front(), end = '')
    else:
        res.add_rear(i)