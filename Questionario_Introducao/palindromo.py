s = input()
cont = 0
for i in range(len(s)//2):
    if(s[i] != s[(len(s)-1)-i]):
        cont+=1

if (len(s)%2 == 0 and cont == 1) or (len(s)%2 != 0 and cont <= 1):
    print('POSSÍVEL') 
else:
    print('IMPOSSÍVEL')
    