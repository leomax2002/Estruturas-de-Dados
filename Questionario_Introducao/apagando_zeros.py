n = int(input())
for i in range(n):
    s = input()
    aux = []
    flag = 0
    cont_1 = 0   
    cont = 0
    for j in s:
        if j == '1':
            flag = 1
            cont_1+=1
        else:
            if(flag!= 0 and cont_1 < s.count('1')):
                cont+=1
    print(cont)
        