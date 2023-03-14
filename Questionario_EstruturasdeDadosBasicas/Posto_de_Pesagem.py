tempo = 0
n,f,p = [int(i) for i in input().split()]
caminhao = [int(j) for j in input().split()]
caminhao = caminhao[::-1]
while len(caminhao) != 0:
    pesagem = caminhao.pop()
    if pesagem > p:
        tempo+=10
        caminhao.insert(0,(pesagem-2))
    if pesagem <= p:
        tempo+=5
    if f-1 != 0:
        for j in range(f-1):
            if len(caminhao) != 0:
                caminhao.pop()
                tempo+=1
            
print(tempo)