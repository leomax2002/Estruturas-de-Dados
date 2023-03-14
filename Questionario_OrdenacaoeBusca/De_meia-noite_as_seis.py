n = int(input())
for i in range(n):
    materias = []
    for i in range(4):
        if i == 0:
            plano = input()
        else:
            materia = input()
            materias.append(materia)
    for i in materias:
        if i in plano:
            plano-=i
    
    print(plano, ':', materias)