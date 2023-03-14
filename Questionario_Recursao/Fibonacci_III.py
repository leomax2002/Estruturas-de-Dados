def fibonacci(n):
    if n == 0:
        chamadas[n]+=1
        return 0
    elif n == 1:
        chamadas[n]+=1
        return 1
    else:
        chamadas[n]+=1
        return fibonacci(n-2) + fibonacci(n-1)

n = int(input())
chamadas = [0]*(n+1)
res = fibonacci(n)
print(f'fibonacci({n}) = {res}.')
for i in range(n+1):
    print(f'{chamadas[i]} chamada(s) a fibonacci({i}).')