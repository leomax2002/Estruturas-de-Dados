def maior_norma(a,b):
    conta  = 0
    contb = 0
    for i in a:
        conta+= abs(i)
    for j in b:
        contb+= abs(j)
    if(conta > contb) :
        print('PRIMEIRO')
    else:
        print('SEGUNDO')
    return None
        

        