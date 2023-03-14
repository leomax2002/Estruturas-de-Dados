def hanoi(n,a,b,c):
    if n >= 1:
        hanoi(n-1,a,c,b)
        print(f'Mover de {a} para {b}.')
        hanoi(n-1,c,b,a)


entrada = input().split()
n = int(entrada[0])
a = entrada[1] #fromPole
b = entrada[2] #toPole
c = entrada[3] #withPole
hanoi(n,a,b,c)