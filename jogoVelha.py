import random
#14 lugares 
#1 a 9 = posicoes para jogada
#10 = nº da partida
# 11 = vencedor (1, 0 ou 2) player 1, velha ou player 2        
# 12 a 14 quantidade de vitorias player 1, velha ou player 2
#vetor[0] % 2 == 0 >> X
vetor = [0,
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,-1,
        0,0,0,0,0]

def jogo_da_velha(vetor):  
    n = int(input("quantos jogos deseja: "))
    opcao = int(input("1. Jogador x Jogador\n2.Jogador x Aleatorio\n3.Aleatorio x Aleatorio\n4.jogador x invencivel\n5.Aleatorio x invencivel\n6.invecivel x invecivel\nopcao: "))
    
    for _ in range(n):
        vetor[0] = 0
        vetor[1:10] = [-1]*9
        jogar = True

        while (jogar == True):
            if opcao == 1:
                posicao = get_posicao(vetor)
                jogador = jogador_jogador(vetor, posicao)
            
            elif opcao == 2:
                if (vetor[0] %2 ==0):
                    posicao = get_posicao(vetor)
                    jogador = 'X'
                    vetor[posicao] = jogador
                else:
                    jogada_aleatoria(vetor, 'O')
                    jogador = 'O'

            elif opcao == 3:
                if(vetor[0] % 2 ==0):
                    jogada_aleatoria(vetor, 'X')
                    jogador = 'X'
                else:
                    jogada_aleatoria(vetor, 'O')
                    jogador = 'O'

            elif opcao == 4: #Começa no O
                if (vetor[0] %2 != 0): 
                    posicao = get_posicao(vetor) 
                    vetor[posicao] = 'X'
                    jogador = 'X'
                else:
                    jogador = jogador_invencivel(vetor)
                    jogador = 'O'

            elif opcao ==5: #Começa no O
                if (vetor[0]%2 !=0):
                    jogada_aleatoria(vetor, 'X')
                    jogador = 'X'
                else:
                    jogador = jogador_invencivel(vetor)
                    jogador = 'O'
            
            elif opcao == 6:
                print("deu nao")

            vetor[0]+= 1     
            print("jogador", jogador)
            jogar = vencedor(vetor, jogador)
            tabuleiro(vetor)
        vetor[10]+=1
    print("\n fim do jogo: ",vetor)
    #grafico(vetor)


def vencedor(vetor, jogador, simulacao=False):
    if (   (vetor[1] ==  vetor[2] == vetor[3] ==jogador) #linha1
        or (vetor[4] ==  vetor[5] == vetor[6] ==jogador) #linha2
        or (vetor[7] ==  vetor[8] == vetor[9] ==jogador) #linha3
        or (vetor[1] ==  vetor[4] == vetor[7] ==jogador) #coluna1
        or (vetor[2] ==  vetor[5] == vetor[8] ==jogador) #coluna2
        or (vetor[3] ==  vetor[6] == vetor[9] ==jogador) #coluna3
        or (vetor[1] ==  vetor[5] == vetor[9] ==jogador) #diagonal 1
        or (vetor[3] ==  vetor[5] == vetor[7] ==jogador)): #diagonal 2
        if not simulacao:
            print(f"O jogador {jogador} ganhou")
            vetor[11] = jogador
            if jogador == 'X':                   
                vetor[12]+=1 #Mais uma vitoria para jogador X
            else:
                vetor[14]+=1 #Mais uma vitoria para jogador O
            return False #Partida acaba
        return False

    #9 jogadas, então acaba e dá velha
    if (vetor[0] == 9):
        if not simulacao:
            print("Deu velha")
            vetor[13]+= 1 #deu velha    
        return False 
    return True     


def jogador_invencivel(vetor):
    if vetor[0] == 0:  
        vetor[1] = 'O'
        return True

    if vetor[0] == 2:
        for i in [3, 7, 9]:
            if vetor[i] == -1:
                vetor[i] = 'O'
                return True

    # Verifica se X pode ganhar
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = 'X'  # Simula jogadas
            if not vencedor(vetor, 'X', simulacao=True):  # Se x vencer
                vetor[i] = 'O'  # bloqueia o X
                return True
            vetor[i] = -1  #restaura por conta da simulacao

    # verifica se O poDe GANHAR
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = 'O'
            if not vencedor(vetor, 'O', simulacao=True):
                return True  # 'O' ganha
            vetor[i] = -1 

    cantos = [1, 3, 7, 9] #priorizar cantos
    for i in cantos:
        if vetor[i] == -1:
            vetor[i] = 'O'
            return True
    
    #n tem jogada pra ganhar/bloq
    jogada_aleatoria(vetor, 'O')

def jogada_aleatoria(vetor, jogador):
    posicao_livre = []
    for i in range(1,10):
        if (vetor[i] == -1):
            posicao_livre.append(i) 
    posicao = random.choice(posicao_livre)
    vetor[posicao] = jogador

def jogador_jogador(vetor, posicao):
    if (vetor[0] % 2 == 0):
        vetor[posicao] = 'X' # Jogador X
        jogador = 'X'
    else:
        vetor[posicao] = 'O' # jogador O
        jogador = 'O'
    return jogador

def tabuleiro(vetor):
    for i in range(1, 10):
        print(f"{vetor[i]:^3}", end=' | ' if i % 3 != 0 else '\n')
        if i % 3 == 0 and i < 9:
            print("-------------")

def get_posicao(vetor):
    while (True):
        posicao = int(input("\nNumero do tabuleiro (1 a 9): "))
        if ( 1 <= posicao <=9 and vetor[posicao] == -1):
            return posicao
        print("Posicao já preenchida ou incorreta")


jogo_da_velha(vetor)