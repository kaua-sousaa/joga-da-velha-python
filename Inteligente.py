import random
#14 lugares 
#0 numero da jogada. Cada partida reseta esse numero
#1 a 9 = posicoes para jogada
#10 Vencedor
#11 nº partida
#12, 13, 14 = X, V, O
# #vetor[0] % 2 == 0 >> X

#-1 = X /// 1 = O
vetorAtual = [0,
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,-1,
        0,0,
        0,0,0,]

ranks = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

rank = [0,0,0,0,0,0,0,0,0]
#guardar cada jogada aqui
todosJogos = []

def jogo_da_velha(vetorAtual):
    quantidade_jogos = int(input("Quantos jogos deseja ? "))
    opcao = int(input("1. Inteligente x Inteligente\n2. Inteligente x Random\n3. Random x Inteligente\n4. Invencivel x Random\n5. Inteligente x Invencivel\n6. Invencivel x Inteligente\nOpcao: "))
    dados_para_escrever = []
    
    for _ in range(quantidade_jogos):
        jogar = True
        vetorAtual[0] = 0
        vetorAtual[1:10] = [-1]*9
        vetorJogadas = []
        while (jogar == True):
            #começar os vetorJogos
            if (opcao == 1):
                if (vetorAtual[0] % 2 == 0):   
                    posicao = jogador_inteligente(vetorAtual, ranks)    
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 2
                    jogador = 2
            if (opcao == 2):         
                if (vetorAtual[0] % 2 == 0):      
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[posicao] = 2
                    jogador = 2
            if (opcao == 3):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[posicao] = 2
                    jogador = 2
                else:
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1
                    
            if (opcao == 4):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_invencivel(vetorAtual, 2)
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[posicao] = 2
                    jogador = 2
            if (opcao == 5):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogador_invencivel(vetorAtual, 2)
                    vetorAtual[posicao] = 2
                    jogador = 2
            if (opcao == 6):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_invencivel(vetorAtual, 2)
                    vetorAtual[posicao] = 2
                    jogador = 2
                else:
                    posicao= jogador_inteligente(vetorAtual, ranks)
                    vetorAtual[posicao] = 1
                    jogador = 1
            
            jogar = vencedor(vetorAtual, jogador)    
            vetorJogadas.append([vetorAtual.copy(), posicao]) #JOGADA E POSICAO
            
            vetorAtual[0]+=1

        todosJogos.append(vetorJogadas)

        atualizar_rank(vetorAtual, vetorJogadas, opcao)            
                      
        vetorAtual[11]+=1 #+1 partida
        dados_para_escrever.append(";".join(map(str, vetorAtual)))
    
    with open("teste.csv", 'w') as f:
        for linha in dados_para_escrever:
            f.write(linha + "\n")


def atualizar_rank(vetorAtual, vetorJogadas, opcao):
    for i, jogadas in enumerate(vetorJogadas):
            if opcao ==2:
                if (i%2 ==0):
                    posicao_jogada = jogadas[1]-1
                    if vetorAtual[10] == 1:
                        ranks[i][posicao_jogada] += 2
                    elif vetorAtual[10] == 2:
                        ranks[i][posicao_jogada] -= 1
                    else:
                        ranks[i][posicao_jogada] +=1
                        break   

def jogador_inteligente(vetorAtual, ranks):

    if vetorAtual[11] == 0:
        melhor_jogada = jogada_aleatoria(vetorAtual)
        return melhor_jogada

    jogada = vetorAtual[0]
    rankJogada = ranks[jogada]
    maiorRank = -999
    encontrou = False

    for i, rank in enumerate(rankJogada):
        if rank > maiorRank and vetorAtual[i+1] == -1:
            maiorRank = rank
            melhor_jogada = i+1 #Pq aqui, ele varre o rank que tem 9 posições, o tabuleiro tem 9 mas começa na 1
            encontrou = True

    if encontrou == False:
        melhor_jogada = jogada_aleatoria(vetorAtual)
        return melhor_jogada
    
    return melhor_jogada
    

def vencedor(vetor, jogador, simulacao=False):
    #print("print vetor[0]: ", vetor[0])
    if (   (vetor[1] ==  vetor[2] == vetor[3] ==jogador) #linha1
        or (vetor[4] ==  vetor[5] == vetor[6] ==jogador) #linha2
        or (vetor[7] ==  vetor[8] == vetor[9] ==jogador) #linha3
        or (vetor[1] ==  vetor[4] == vetor[7] ==jogador) #coluna1
        or (vetor[2] ==  vetor[5] == vetor[8] ==jogador) #coluna2
        or (vetor[3] ==  vetor[6] == vetor[9] ==jogador) #coluna3
        or (vetor[1] ==  vetor[5] == vetor[9] ==jogador) #diagonal 1
        or (vetor[3] ==  vetor[5] == vetor[7] ==jogador)): #diagonal 2
        if not simulacao:
            #print(f"O jogador {jogador} ganhou")
            #vetor[12] = jogador
            if jogador == 1:
                vetor[10] = 1                   
                vetor[12]+=1 #Mais uma vitoria para jogador X
            elif jogador == 2:
                vetor[10] = 2
                vetor[14]+=1 #Mais uma vitoria para jogador O
            return False #Partida acaba
        return False

    #9 jogadas, então acaba e dá velha
    if (vetor[0] == 8):
        if not simulacao:
            #print("Deu velha")
            vetor[10] = -2
            vetor[13]+= 1 #deu velha    
        return False 
    return True  

def jogada_aleatoria(vetorAtual):  
    while True:
        posicao = random.randint(1, 9)
        if vetorAtual[posicao] == -1:
            return posicao

def jogador_invencivel(vetor, jogador):
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



""" for index, jogo in enumerate(todosJogos):
    print(f"### Jogo {index + 1}:")
    print(f"- Rank: {jogo[1]}")
    
    for jogada_num, jogada in enumerate(jogo[2]):
        jogada_formatada = ', '.join(map(str, jogada))
        print(f"   {jogada_num + 1}. [{jogada_formatada}]")
    print("-"*50) """
 
print(vetorAtual)
print("-----------")
print(ranks)
print("------------")
print("------------")


""" for jogos in todosJogos:
    for jogo in jogos:
        print(jogo)
    print("*--------------*--------------") """

            
 
