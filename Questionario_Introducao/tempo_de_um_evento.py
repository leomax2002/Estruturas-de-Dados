comeco = input().split(' ')
final = input().split(' ')

dia_comeco = int(comeco[0])
dia_final = int(final[0])

horario_comeco = [int(i) for i in comeco[1].split(':')]
horario_final = [int(j) for j in final[1].split(':')]

comeco_seg = dia_comeco*(86400) + horario_comeco[0]*(3600) + horario_comeco[1]*(60) + horario_comeco[2]
final_seg = dia_final*(86400) + horario_final[0]*(3600) + horario_final[1]*(60) + horario_final[2]


if(final_seg <= comeco_seg):
    print('Data inválida!')
else:
    tempo = final_seg - comeco_seg
    dia = tempo//(86400)
    tempo = tempo%86400
    hora = tempo//3600
    tempo = tempo%3600
    minuto = tempo//60
    segundo = tempo%60
    print(f'{dia} dia(s)')
    print(f'{hora} hora(s)')
    print(f'{minuto} minuto(s)')
    print(f'{segundo} segundo(s)')