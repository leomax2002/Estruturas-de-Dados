def organiza(mencao):
    for i in range(len(mencao)-1):
        if mencao[len(mencao)-1] < mencao[i]:
            mencao[len(mencao)-1], mencao[i] = mencao[i], mencao[len(mencao)-1]
            
           
SS = []
MS = []
MM = []
MI = []
II = []
SR = []
n = int(input())
for i in range(n):
    aluno = input()
    aux = aluno.split(sep = ' ', maxsplit = 1)
    if aux[0] == 'SS':
        SS.append(aluno)
        organiza(SS)
    
    elif aux[0] == 'MS':
        MS.append(aluno)
        organiza(MS)
        
    elif aux[0] == 'MM':
        MM.append(aluno)
        organiza(MM)
        
    elif aux[0] == 'MI':
        MI.append(aluno)
        organiza(MI)
        
    elif aux[0] == 'II':
        II.append(aluno)
        organiza(II)
        
    elif aux[0] == 'SR':
        SR.append(aluno)
        organiza(SR)
mansoes = SS+MS+MM+MI+II+SR
for j in mansoes:
    print(j)

