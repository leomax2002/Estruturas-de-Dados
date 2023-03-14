import timeit
import random
import string
def verificaPalindromo(lista):
    resposta = True
    while lista:
        c1 = lista.pop(0)
        c2 = lista.pop()
        if c1 != c2:
            resposta = False
    return resposta
lista = list(range(200))
t1 = timeit.Timer("verificaPalindromo(lista)", "from __main__ import verificaPalindromo,lista")
print(t1.timeit(number=1000))
