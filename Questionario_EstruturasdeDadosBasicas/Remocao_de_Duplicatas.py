n = int(input())
for i in range(n):
    p = input()
    pilha = []
    pilha_cont = []
    sem_duplicada = True
    comecar = False
    for j in p:
        if (comecar == True and ((pilha[len(pilha)-1] == '(' and j not in '()') or (pilha[len(pilha)-1] == '[' and j not in '[]') or (pilha[len(pilha)-1] == '{' and j not in '{}') )):
                pilha_cont[len(pilha_cont)-1]+=1
        if j in '([{':
            pilha.append(j)
            pilha_cont.append(0)
            comecar = True
        if j in ')]}':
            pilha.pop()
            if(pilha_cont.pop() == 0):
                sem_duplicada = False
                print('A expressão possui duplicata.')
                break
            if(pilha_cont == []):
                comecar = False
    if(sem_duplicada):
        print('A expressão não possui duplicata.')