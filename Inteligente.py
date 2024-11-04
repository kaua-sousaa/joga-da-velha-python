import random
#14 lugares 
#0 numero da jogada. Cada partida reseta esse numero
#1 -> [0,8] = posicoes para jogada
#2 Vencedor
#3 nº partida
#4, 5, 6 = X, V, O
#7 rank
#8 posicao jogada
# #vetor[0] % 2 == 0 >> X

#-1 = X /// 1 = O
vetorAtual = [0,
        [-1,-1,-1,
        -1,-1,-1,
        -1,-1,-1],
        0,0,
        0,0,0,
        0,0]

ranks = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]


#guardar cada jogada aqui

teste = []
vetorJogadas = []

def jogo_da_velha(vetorAtual):
    quantidade_jogos = int(input("Quantos jogos deseja ? "))
    opcao = int(input("1. Inteligente x Inteligente\n2. Inteligente x Random\n3. Random x Inteligente\n4. Inteligente x Invencivel\n5. Invencivel x Inteligente \nOpcao: "))
    dados_para_escrever = []
    
    for _ in range(quantidade_jogos):
        jogadas_utilizadas = []

        jogar = True
        vetorAtual[0] = 0
        vetorAtual[1] = [-1]*9
        vetorJogadas.append([vetorAtual[1].copy(), vetorAtual[3],vetorAtual[7], vetorAtual[8], len(vetorJogadas)+1])
        vetorAtual[0]+=1
        while (jogar == True):
            if (opcao == 1):
                """ if (vetorAtual[0] % 2 == 0):   
                    posicao = jogador_inteligente(vetorAtual, ranks)    
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 2
                    jogador = 2 """
            if (opcao == 2):         
                if (vetorAtual[0] % 2 != 0):      
                    posicao = jogador_inteligente(vetorAtual, jogadas_utilizadas)
                    vetorAtual[1][posicao] = 1
                    jogador = 1
                else:
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[1][posicao] = 2
                    jogador = 2
            if (opcao == 3):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_inteligente(vetorAtual, jogadas_utilizadas)
                    vetorAtual[1][posicao] = 1
                    jogador = 1  
                else:                   
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[1][posicao] = 2
                    jogador = 2
                    """                 
            if (opcao == 4):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogador_invencivel(vetorAtual, 2)
                    vetorAtual[posicao] = 2
                    jogador = 2
            if (opcao == 5):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_invencivel(vetorAtual, 2)
                    vetorAtual[posicao] = 2
                    jogador = 2
                else:
                    posicao= jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1 """
            
            jogar = vencedor(vetorAtual, jogador)
            vetorJogadas.append([vetorAtual[1].copy(), vetorAtual[3],vetorAtual[7], posicao, len(vetorJogadas)+1]) #tabuleiro, nº partida, rank e posicao jogada
            vetorAtual[0]+=1

        atualizar_rank(vetorAtual, vetorJogadas, jogadas_utilizadas, opcao)                             
        vetorAtual[3]+=1 #+1 partida
        dados_para_escrever.append(";".join(map(str, vetorAtual)))
        teste.append(jogadas_utilizadas)
    if opcao == 1:
        nomeCsv = 'inteligente_inteligente.csv'
    elif opcao ==2:
        nomeCsv = 'inteligente_aleatorio.csv'
    elif opcao ==3:
        nomeCsv = 'aleatorio_inteligente.csv'
    elif opcao ==4:
        nomeCsv = 'inteligente_invencivel.csv'
    elif opcao ==5:
        nomeCsv = 'invencivel_inteligente.csv'

    with open(nomeCsv, 'w') as f:
        for linha in dados_para_escrever:
            f.write(linha + "\n")

    

def atualizar_rank(vetorAtual, vetorJogadas, jogadas_utilizadas, opcao):
    # print(jogadas_utilizadas)
    for jogadas in vetorJogadas:
        if jogadas[4] in jogadas_utilizadas:
            if vetorAtual[2] == 1:
                jogadas[2]+=1
            elif vetorAtual[2] == 2:
                jogadas[2]-=1
            else:
                jogadas[2]+=0

        if vetorAtual[3] == jogadas[1]: ##Se for a mesma partida
            if vetorAtual[2] == 1: #Se foi vencedor
                jogadas[2]+=1 #atualizando rank
            elif vetorAtual[2] == 2:
                jogadas[2]-=1
            else:
                jogadas[2]+=0

            
def jogador_inteligente(vetorAtual, jogadas_utilizadas):
    if vetorAtual[3] == 0:
        melhor_jogada = jogada_aleatoria(vetorAtual)
        return melhor_jogada
    
    jogada_utilizada = None
    rank = 0
    achou = False
    for i, jogos in enumerate(vetorJogadas):
        tabuleiro = jogos[0]

        if vetorAtual[1] == tabuleiro and jogos[2] > rank and vetorAtual[1][vetorJogadas[i+1][3] == -1]:
            #Se tabuleiro é igual E Rank for o Maior E Posicao estiver disponivel no vetorAtual
            rank = jogos[2]
            melhor_jogada = vetorJogadas[i + 1][3]
            jogada_utilizada = vetorJogadas[i][4] #id do vetor utilizado
            achou = True
  
    if achou == False:
        melhor_jogada = jogada_aleatoria(vetorAtual)   

    jogadas_utilizadas.append(jogada_utilizada)
    return melhor_jogada
    

def vencedor(vetor, jogador, simulacao=False):
    #print("print vetor[0]: ", vetor[0])
    tabuleiro = vetorAtual[1]
    if (   (tabuleiro[0] ==  tabuleiro[1] == tabuleiro[2] ==jogador) #linha1
        or (tabuleiro[3] ==  tabuleiro[4] == tabuleiro[5] ==jogador) #linha2
        or (tabuleiro[6] ==  tabuleiro[7] == tabuleiro[8] ==jogador) #linha3
        or (tabuleiro[0] ==  tabuleiro[3] == tabuleiro[6] ==jogador) #coluna1
        or (tabuleiro[1] ==  tabuleiro[4] == tabuleiro[7] ==jogador) #coluna2
        or (tabuleiro[2] ==  tabuleiro[5] == tabuleiro[8] ==jogador) #coluna3
        or (tabuleiro[0] ==  tabuleiro[4] == tabuleiro[8] ==jogador) #diagonal 1
        or (tabuleiro[2] ==  tabuleiro[4] == tabuleiro[6] ==jogador)): #diagonal 2
        if not simulacao:
            #print(f"O jogador {jogador} ganhou")
            #vetor[12] = jogador
            if jogador == 1:
                vetor[2] = 1                   
                vetor[4]+=1 #Mais uma vitoria para jogador X
            elif jogador == 2:
                vetor[2] = 2
                vetor[5]+=1 #Mais uma vitoria para jogador O
            return False #Partida acaba
        return False

    #9 jogadas, então acaba e dá velha
    if (vetor[0] == 9):
        if not simulacao:
            #print("Deu velha")
            vetor[2] = -2
            vetor[6]+= 1 #deu velha    
        return False 
    return True  

def jogada_aleatoria(vetorAtual):
    vetor = vetorAtual[1]
    while True:
        posicao = random.randint(0, 8)
        if vetor[posicao] == -1:
            return posicao

def jogador_invencivel(vetorAtual, jogador):
    vetor = vetorAtual[1]
    adversario = 2 if jogador == 1 else 1

    if vetor[0] == 0 and jogador == 1:
        return 1
        
    if vetor[0] == 2 and jogador == 1:
        for i in [3, 7, 9]:
            if vetor[i] == -1:
                return i #retornando posicao    
            
    # verifica se O poDe GANHAR
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = jogador
            if not vencedor(vetor, jogador, simulacao=True):
                return i  # '1' ganha
            vetor[i] = -1 

    # Verifica se X pode ganhar
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = adversario  # Simula jogadas
            if not vencedor(vetor, adversario, simulacao=True):  # Se x vencer    
                return i# bloqueia o 2
            vetor[i] = -1  #restaura por conta da simulacao

    if vetor[0] == 4 and vetor[5] == -1:
        return 5
    
    cantos = [1, 3, 7, 9] #priorizar cantos
    for i in cantos:
        if vetor[i] == -1:
            return i
            
    #n tem jogada pra ganhar/bloq
    return jogada_aleatoria(vetor)

jogo_da_velha(vetorAtual)
print(vetorAtual)
print("-----------")
""" for jogos in vetorJogadas:
    print(jogos) """

print("------------")
""" for i in teste:
    print(i) """