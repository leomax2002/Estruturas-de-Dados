n = int(input())
cx,cy = [float(i) for i in input().split()]
rx,ry = [float(j) for j in input().split()]
flag = 0
for k in range(n):
    x, y = [float(l) for l in input().split()]
    dist_c = ((x-cx)**2+(y-cy)**2)**(0.5)
    dist_r = ((x-rx)**2+(y-ry)**2)**(0.5)
    if(flag == 0 and dist_r > 2*dist_c):
        print(f'O coelho pode escapar pelo buraco ({x:.3f}, {y:.3f}).')
        flag = 1
if(flag == 0):
    print('O coelho nao pode escapar.')
