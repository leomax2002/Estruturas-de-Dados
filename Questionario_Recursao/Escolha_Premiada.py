def escolha(s,v):
    for i in range(2**len(v)):
        soma = 0
        binario = list(bin(i))
        binario.reverse()
        ind = 0
        if sum(v) < s:
            break
        for j in range(len(binario)):
            if binario[j] == 'b':
                break
            if v[j] > s:
                continue
            if v[j] == s:
                return True
            soma+=v[j]*int(binario[j])
            if soma == s:
                return True
    else:
        return False



v = [int(x) for x in input().split()]
s = int(input())
if(escolha(s,v)):
    print('E possivel ganhar.')
else:
    print('Impossivel ganhar.')