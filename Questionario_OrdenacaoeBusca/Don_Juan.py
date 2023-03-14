n = int(input())
esposa = ''
tam_nome = []
nome = []
for i in range(n):
    pretendente = input()
    tam_nome.append(len(pretendente))
    nome.append(pretendente)
while True:
    temp = tam_nome.count(max(tam_nome))
    if tam_nome.count(max(tam_nome)) == 1:
        print(nome[tam_nome.index(max(tam_nome))])
        break
    else:
        while temp != 0:
            aux = tam_nome.index(max(tam_nome))
            tam_nome.pop(tam_nome.index(max(tam_nome)))
            nome.pop(aux)
            temp-=1
    if len(tam_nome) == 0:
        print('Que mala suerte!')
        break