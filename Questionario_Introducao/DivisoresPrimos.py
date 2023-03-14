def primos_gemeos (n):
    cont = 0
    pares = n*[0]
    primo = 2
    lista_primos = []
    while cont != n:
        for i in range(2,primo):
            if(primo%i == 0):
                break
            elif(i == primo-1):
                lista_primos.append(primo)
        primo+=1
        if(len(lista_primos) >= 2):
            for i in range(len(lista_primos)-1):
                if lista_primos[i+1] == lista_primos[i]+2:
                    pares[cont] = (lista_primos[i], lista_primos[i+1])
                    lista_primos = [lista_primos[i+1]]
                    cont+=1
    return pares
x = int(input())
print(primos_gemeos(x))
                    

        