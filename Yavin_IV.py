import random
class Fila:
    def __init__(self):
        self.itens = []
    def vazia(self):
        return self.itens == []
    def enfileirar(self, item):
        self.itens.insert(0,item)
    def desenfileirar(self):
        return self.itens.pop()
    def tamanho(self):
        return len(self.itens)

class Fighter:
    def __init__(self, id):
        self.id = id
        self.defesa = 100
        self.ataque = int(random.uniform(0,100))
        self.precisao = round(random.uniform(0, 1),2)
        self.jedi = bool(round(random.uniform(0,1)) <= 1.25e-10)
        
    def get_precisao(self):
        return self.precisao
    def get_id(self):
        return self.id
    def get_jedi(self):
        return self.jedi
    def get_defesa(self):
        return self.defesa
    def get_ataque(self):
        return self.ataque
    def __str__(self):
        return f'fighter_id = {self.id}, d: {self.defesa}, a:{self.ataque}, p: {self.precisao}, j: {self.jedi}'
    def disparar(self):
        
        if random.uniform(0, 1) <= self.precisao:
            return self.ataque
        
        return 0
    def sobreviveu_danos(self, disparos):
        
        for i in disparos:
            self.defesa -= i
            
        return self.defesa > 0
class Death_Star:
    def __init__(self):
        self.defesa = 1000
        self.ataque = int(random.uniform(0, 100))
        self.precisao = round(random.uniform(0, 1), 2)
        self.canhoes = int(random.uniform(1, 6))

    def get_precisao(self):
        return self.precisao

    def get_jedi(self):
        return self.jedi

    def get_defesa(self):
        return self.defesa

    def get_ataque(self):
        return self.ataque
    
    def __str__(self):
        return f'death_star = d: {self.defesa}, a:{self.ataque}, p: {self.precisao}, c: {self.canhoes}'
    
    def disparar(self):

        r = []

        for i in range(self.canhoes):
            
            if random.uniform(0, 1) <= self.precisao:
                r.append(self.ataque)
            else:
                r.append(0)
        return r
    
    def sobreviveu_danos(self, disparo):
        self.defesa -= disparo

        return self.defesa > 0
    
class Simulacao_Batalha:
    
    def __init__(self, turnos, confianca):
        self.f_fighters = Fila()
        self.turnos = turnos
        self.confianca = confianca
        self.id_geral = 0
        self.death_star = Death_Star()
    
    def novo_fighter(self):
        numero = round(random.uniform(0, 1), 2)
        return numero <= self.confianca
    
    def get_novo_id(self):
        self.id_geral +=1
        return self.id_geral
    
    def executar_simulacao(self):
        
        for t in range(self.turnos):
            print('---------------------------')
            print(f'Turno {t}')
            print('---------------------------')
            
            if self.novo_fighter():
                fighter = Fighter(self.get_novo_id())
                
                self.f_fighters.enfileirar(fighter)
                print(f"- fighter_id: {fighter.get_id()} entrou em formação")
                
            print(f'- {self.f_fighters.tamanho()} fighters para atacar.')
            if self.f_fighters.tamanho() == 0:
                continue
            
            fighter = self.f_fighters.desenfileirar()
            print(f'- <LIDER> {fighter}')
            
            if fighter.get_jedi():
                print('<<<<<< TEMOS UM JEDI >>>>>>')
            #turno Death Star
            print('\nTurno - Death Star')
            print(f'- {self.death_star}')
            
            disparos = self.death_star.disparar()
            print(f'- disparos: {disparos}')
            
            if fighter.sobreviveu_danos(disparos):
                print(f"= {fighter} sobreviveu!")
            else:
                print(f'- MAN DOWN! - fighter_id: {fighter.get_id()}')
                
            #turno fighter
                print('\nTurno - Fighter')
                disparo = fighter.disparar()
                print(f'- disparo: {disparo}')
                
                if fighter.get_jedi():
                    print('-Bonus JEDI +10.000')
                    disparo+= 10000
                if self.death_star.sobreviveu_danos(disparo):
                    print(f'- {self.death_star} sobreviveu!')
                else:
                    print("\n\n DEATH STAR DESTROYED!! ")
                    print(f'{self.death_star}')
                    exit()
                self.f_fighters.enfileirar(fighter)
                
simulacao = Simulacao_Batalha(1000, 0.7)
simulacao.executar_simulacao()