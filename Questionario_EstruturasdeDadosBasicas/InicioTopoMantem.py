class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)
        # Implemente este método.
      
    def pop(self):
        return self.items.pop(0)
       # Implemente este método.
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack() 
s.push(0)
s.push(2)
s.pop()
s.pop()
for i in s.items:
    print(i)
     