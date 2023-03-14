def Del(comando):
    global pos_mus
    global playlist
    comando_index = playlist.index(comando[1])
            
    playlists_anteriores.append([playlist.copy(),pos_mus])
    if pos_mus > comando_index:
        pos_mus -=1

    elif pos_mus == 0:
        pos_mus = len(playlist)-1

    elif pos_mus == len(playlist)-1:
        pos_mus = 0

    playlist.pop(comando_index)

def next(comando):
    global pos_mus
    global playlist
    global tocando
    comando_index = playlist.index(comando[1])
    playlists_anteriores.append([playlist.copy(),pos_mus])
    tmp = playlist.pop(comando_index)
    if not tocando:
        playlist.insert(pos_mus,tmp)
    else:
        if comando_index < pos_mus:
            playlist.insert(pos_mus,tmp)
            pos_mus-=1
        else:
            playlist.insert(pos_mus+1,tmp)

def undo():
    global playlists_anteriores
    global playlist
    global pos_mus
    global tocando
    tmp = playlists_anteriores.pop()
    if tmp != False:
        playlist = tmp[0]
        pos_mus = tmp[1]
    else:
        tocando = False

def undo_total():
    global playlists_anteriores
    global playlist
    global pos_mus
    global tocando
    while playlists_anteriores != []:
        tmp = playlists_anteriores.pop()
        if tmp != False:
            playlist = tmp[0]
            pos_mus = tmp[1]
        else:
            tocando = False


res = []


playlist = []
playlists_anteriores = []
tocando = False
pos_mus = None

nome_arquivo_entrada = '0000.in'
nome_arquivo_saida = '0000.out'

with open(nome_arquivo_entrada, 'r') as arquivo:
    print('Entrada:')
    print(arquivo.read()+'\n')


with open(nome_arquivo_entrada, 'r') as arquivo:
    entrada = arquivo.read().split('\n')
    for ent in entrada:
        comando = ent.split()

        if playlist == []:
            pos_mus = None
            tocando = False

        if comando[0] == 'play' and not tocando and playlist != []:
            playlists_anteriores.append(False)
            tocando = True
            

        elif comando[0] == 'stop' and tocando:
            tocando = False

        elif comando[0] == 'add':
            playlists_anteriores.append([playlist.copy(),pos_mus])
            playlist.append(comando[1])
            if pos_mus == None:
                pos_mus = 0
                
        elif comando[0] == 'del':
            if comando[1] in playlist:
                if not tocando:
                    Del(comando)
                else:
                    if playlist.index(comando[1]) != pos_mus:
                        Del(comando)

        elif comando[0] == 'next':

            if comando[1] in playlist and playlist.index(comando[1]) != pos_mus:
    
                    next(comando)

        elif comando[0] == 'list':
            if playlist == []:
                print('[vazia]')
                res.append('[vazia]')
            else:

                playlist_str = ''.join(playlist[i]+',' if i != len(playlist)-1 else playlist[i] for i in range(len(playlist)))
                print(playlist_str)
                res.append(playlist_str)                

        elif comando[0] == 'current':
            if playlist != []:
                print(playlist[pos_mus])
                res.append(playlist[pos_mus])
            else:
                print('Toque! Toque, Dijê!')
                res.append('Toque! Toque, Dijê!')

        elif comando[0] == 'undo' and playlists_anteriores != []:
            if len(comando) > 1 and comando[1] == '*':
                undo_total()
            else:
                undo()

            
        elif comando[0] == 'ended' and tocando:
            playlists_anteriores = []
            if playlist != []:
                pos_mus+=1
            
        elif comando[0] == 'fight':
            print('Jedi Wagner, assuma o comando!')
            res.append('Jedi Wagner, assuma o comando!')
            break
        if pos_mus == len(playlist):
            pos_mus = 0
 
resp = [] 
with open(nome_arquivo_saida, 'r') as arquivo:
    print('\nsaida:')
    aux = arquivo.read()
    print(aux)
    resp.append(aux.split('\n'))
    
with open(nome_arquivo_saida, 'r') as arquivo:
    print('\nComparacao:')
    i = 0
    for comp in arquivo.readlines():
        if comp.strip('\n') == res[i]:
            print('Igual')
        else:
            print('Diferente')
        i+=1