n = int(input())
fibonacci = [0,1]
fib_nao_acci = []
termos = 1
i = 2
while True:
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    i+=1
    if i not in fibonacci:
        fib_nao_acci.append(i)
        termos+=1
print(fib_nao_acci)