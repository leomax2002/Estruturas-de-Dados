lista = []
d = {}
while True:
    produto = input().split()
    if produto[0] == 'fim':
        break
    if produto[0] == '-':
        lista.remove((d[produto[1]],produto[1]))
        
    else:
         lista.append((float(produto[1]),produto[0]))
         d[produto[0]] = float(produto[1])
cont = 0
tot = 0
for i, j in sorted(lista, reverse = True):
    print(f'{j}: R$ {i:.2f}')
    cont+=1
    tot+=i
print('----------------------')
print(f'{cont} item(ns): R$ {tot:.2f}')
    
    

    
    