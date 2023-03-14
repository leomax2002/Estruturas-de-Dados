fatoriais = [0]*5000
n = int(input())
for i in range(n):
    f = int(input())
    for i in range(f):
        if fatoriais[i] != 0:
            print(fatoriais[i%2357], end = ' ')
        else:
            fatoriais[i] = i*fatoriais[i-1]
            print(fatoriais[i]%2357, end = ' ')
