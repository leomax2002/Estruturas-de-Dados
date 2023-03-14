n = int(input())
roupas = input().split()
duplicatas = []
cont_duplicatas = 0
for i in roupas:
    if i not in duplicatas:
        duplicatas.append(i)
    else:
        cont_duplicatas+=1

print(cont_duplicatas)
