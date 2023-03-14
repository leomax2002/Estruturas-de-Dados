chamadas = 0
def fibonacci(n):
    global chamadas
    if n == 0:
        chamadas+=1
        return 0
    elif n == 1:
        chamadas+=1
        return 1
    else:
        chamadas+=1
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input())
num = fibonacci(n)
print(f'Fib({n}) = {num} ({chamadas} chamadas)')