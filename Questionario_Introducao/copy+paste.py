import math
tam = int(input())
aux = tam
tempo = 0
cont = 0
transm = 0
print(f'Transmitindo {tam} bytes...')
while True:
    transf = int(input())
    transm += transf
    aux-=transf
    tempo+=1
    cont+=1
    if(aux == 0):
        break
    if(cont == 5):
        if(transm/cont > 0):
            restante = math.ceil((aux*cont)/transm)
            print(f'Tempo restante: {restante} segundos.')
        else:
            print('Tempo restante: pendente...')
        transm = 0
        cont = 0
print(f'Tempo total: {tempo} segundos.')
    