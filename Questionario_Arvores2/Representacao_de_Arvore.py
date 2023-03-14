def procura(raiz,pref, n = 0):
    if raiz == None:
        return n
    print(n*pref+str(raiz.dado))
    n+=1
    for filho in raiz.filhos:
        procura(filho,pref,n)
    return

def mostra(raiz, pref):
    procura(raiz,pref)