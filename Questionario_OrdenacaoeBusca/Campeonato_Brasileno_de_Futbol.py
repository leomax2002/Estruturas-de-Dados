pontos = 20*[0]
vitorias = 20*[0]
saldo_de_gols = 20*[0]
gols_marcados = 20*[0]
gols_sofridos = 20*[0]
nome = 20*[0]

for i in range(20):
    time = input().split()
    nome[i] = time[0]
    cont_pontos = 0
    cont_gols_marcados = 0
    cont_gols_sofridos = 0
    cont_vitorias = 0
    for j in range(1,len(time)-1):
        cont_gols_marcados+=time[i][0]
        cont_gols_sofridos+=time[i][1]
        if time[i][0] > time[i][1]:
            cont_pontos+=3
            cont_vitorias+=1
        elif time[i][0] == time[i][1]:
            cont_pontos+=1
    pontos[i] = cont_pontos
    vitorias[i] = cont_vitorias
    saldo_de_gols[i] = cont_gols_marcados - cont_gols_sofridos
    gols_marcados[i] = cont_gols_marcados
    gols_sofridos[i] = cont_gols_sofridos
print(pontos)
print(vitorias)
print(saldo_de_gols)
print(gols_marcados)
print(gols_sofridos)
print(nome)

