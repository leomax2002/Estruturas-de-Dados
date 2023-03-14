for i in range(5):
    n = int(input())
    lista = []
    fifo = True
    lifo = True
    aipo = True
    for j in range(n):
        p,x = input().split()
        x = int(x)
        if p == 'in':
            lista.append(x)
        elif(p == 'out' and(fifo or lifo or aipo)):
            if(x != lista[len(lista)-1]):
                lifo = False
            if(x != lista[0]):
                fifo = False
            if(x != max(lista)):
                aipo = False
            if x in lista:
                lista.remove(x)
        else:
            pass
    if fifo and not lifo and not aipo:
        print('FIFO')
    elif lifo and not fifo and not aipo:
        print('LIFO')
    elif aipo and not lifo and not fifo:
        print('AIPO')
    elif not fifo and not lifo and not aipo:
        print('no hay!')
    else:
        print('uai?')
        

