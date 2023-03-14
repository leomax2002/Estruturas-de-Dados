n = int(input())
for i in range(n):
    s = input()
    letras = []
    nums = []
    digi = ''
    for j in s:
        
        if j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letras.append(j)
            if(digi != ''):
                nums.append(int(digi))
            digi = ''
        else:
            digi+=j
    nums.append(int(digi))
    for i in range(len(letras)):
        print(nums[i]*letras[i], end = '')
    print()
            
            
            