def editor_listas(inst,lista):
    if(inst[0] == 'I' and int(inst[1]) > 0):
        lista.insert(0,int(inst[1]))
    if(inst[0] == 'F' and int(inst[1]) > 0):
        lista.append(int(inst[1]))
    if(inst[0] == 'P'):
        print(lista.pop())
    if(inst[0] == 'D'):
        print(lista.pop(0))
    if(inst[0] == 'V' and int(inst[1]) > 0):
        ocor = lista.count(int(inst[1]))
        for i in range(ocor):
            lista.remove(int(inst[1]))
        print(ocor)
    if(inst[0] == 'E' and int(inst[1]) > 0):
        print(lista.pop( int(inst[1])-1 ))
    if(inst[0] == 'T' and int(inst[1]) > 0 and int(inst[2]) > 0):
        lista[lista.index(int(inst[1]))] = int(inst[2])
    if(inst[0] == 'C' and int(inst[1]) > 0):
        print(lista.count( int(inst[1]) ))

lista = []
while True:
    instrucao = input().split()
    if(instrucao[0] == 'X'):
        break
    editor_listas(instrucao, lista)
print()
for i in lista:
    print(i)