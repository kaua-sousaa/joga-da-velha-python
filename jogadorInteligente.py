import random
#14 lugares 
#0 numero da jogada. Cada partida reseta esse numero
#1 a 9 = posicoes para jogada
#10 = nº da partida
#11 = RANK
# 12  vencedor (1, 0 ou 2) player 1, velha ou player 2        
# 13 a 15 quantidade de vitorias player 1, velha ou player 2
# 16 posicao jogada
# 17 jogador
#vetor[0] % 2 == 0 >> X

#-1 = X /// 1 = O
TUDOTESTE = []
vetorAtual = [0,
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,-1,
        0,0,0,0,0,0,0,0]

#guardar cada jogada aqui
todosJogos = []

def jogo_da_velha(vetorAtual):
    quantidade_jogos = int(input("Quantos jogos deseja ? "))
    opcao = int(input("1. Random x Random\n2. Inteligente x Random\n3. Random x Inteligente\n4. Invencivel x Random\n5. Invencivel x Inteligente\nOpcao: "))
    dados_para_escrever = []
    
    for _ in range(quantidade_jogos):
        jogar = True
        vetorAtual[0] = 0
        vetorAtual[1:10] = [-1]*9
        vetorJogadas = []
        jogoNOVO = False
        while (jogar == True):
            #começar os vetorJogos
            """ if (opcao == 1):
                posicao = jogada_aleatoria(vetor)

                if (vetor[0] % 2 == 0):              
                    vetor[posicao] = 1
                    jogador = 1
                else:
                    vetor[posicao] = -3
                    jogador = -3 """
            if (opcao == 2):         
                if (vetorAtual[0] % 2 == 0):      
                    posicao, jogoNOVO, idJogo = jogador_inteligente(todosJogos, vetorAtual, jogoNOVO)
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
                    posicao, jogoNOVO, idJogo = jogador_inteligente(todosJogos, vetorAtual, jogoNOVO)
                    vetorAtual[posicao] = 1
                    jogador = 1
            if (opcao == 4):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_invencivel(vetorAtual)
                    vetorAtual[posicao] = 2
                    jogador = 2
                else:
                    posicao = jogada_aleatoria(vetorAtual)
                    vetorAtual[posicao] = 1
                    jogador = 1
            if (opcao == 5):
                if (vetorAtual[0] % 2 == 0):
                    posicao = jogador_invencivel(vetorAtual)
                    vetorAtual[posicao] = 2
                    jogador = 2
                else:
                    posicao, jogoNOVO, idJogo = jogador_inteligente(todosJogos, vetorAtual, jogoNOVO)
                    vetorAtual[posicao] = 1
                    jogador = 1

    
            vetorAtual[16] = posicao
            vetorAtual[17] = jogador
            
            jogar = vencedor(vetorAtual, jogador)          
            vetorJogadas.append([vetorAtual.copy(), vetorAtual[16]]) #JOGADA E POSICAO
            
            vetorAtual[0]+=1
              
        vetorAtual[10]+=1 #+1 jogo
        
        rank = 0
        if (vetorAtual[12] == 1):
            rank = 1
        elif(vetorAtual[12] == 2):
            rank = -1
        else:
            rank = 0

        if not jogoNOVO:
            novo_jogo = [len(todosJogos) + 1, rank ,vetorJogadas.copy()]
            inserir_ordenado(todosJogos, novo_jogo)
            """ print("Lista ordenada por rank:")
            for jogo in todosJogos:
                print(f"ID: {jogo[0]}, Rank: {jogo[1]}") """
        else:
            for i, jogo in enumerate(todosJogos):
                if (jogo[0] == idJogo):
                    jogo[1]+=rank
                    jogo_atualizado = todosJogos.pop(i)
                    inserir_ordenado(todosJogos, jogo_atualizado)
                    break
                        
        if opcao == 3:
            dados_para_escrever.append(";".join(map(str, vetorAtual)))

    
    with open("teste.csv", 'w') as f:
        for linha in dados_para_escrever:
            f.write(linha + "\n")


def inserir_ordenado(todosJogos, novo_jogo):
    # Percorre a lista para encontrar a posição correta
    for i, jogo in enumerate(todosJogos):
        if novo_jogo[1] > jogo[1]:  # Compara pelo rank (segundo elemento da lista)
            todosJogos.insert(i, novo_jogo)  # Insere na posição correta
            return
    # Se não encontrar posição, insere no final (rank mais baixo)
    todosJogos.append(novo_jogo)


def jogador_inteligente(todosJogos, vetorAtual, jogoNOVO):
    #Jogada 1: Se na jogada 1 o vetor na posicao 11 tive rank, lá que vai ser e assim por diante
    #vou percorrer o vetor e marcar 1 se o jogo tiver dado vitoria para o X
    #primeira jgoada é aleatoria
    #FALSE QUANDO VAI CRIAR JOGADAS
    #TRUE QUANDO NAO VAI CRIAR JOGADAS

    jogada = vetorAtual[0]
    maiorRank =0
    melhor_posicao =0
    encontrou_maior = False
    jogadas = []
    #print(vetorJogos)

    #PRIMEIRA JOGADA ONDE DE TODAS, POIS O VETORJOGOS TA VAZIO
    """ if not todosJogos:
        melhor_posicao = random.randint(1,9)
        return melhor_posicao """
          
    #QUANDO FOR A PRIMEIRA PARTIDA
    if (vetorAtual[10] == 0):
        melhor_posicao = jogada_aleatoria(vetorAtual)
        return melhor_posicao, False, None #primeiro jogo entao nao há jogos para comparar
    
    
    #Varrendo os vetores para achar o melhor rank
    for ranks in todosJogos:
        if (ranks[1] >= maiorRank): #Achando o jogo com melhor RANK
            idJogo = ranks[0]
            maiorRank = ranks[1]
            jogadas = ranks[2] #Depositando em jogadas os vetores das jogadas com mais rank
        else:
            break

    if not jogadas:
        melhor_posicao = jogada_aleatoria(vetorAtual)
        return melhor_posicao, False, None
    
    for jogos in jogadas:
        jogo = jogos[0]
        if (jogo[0] == jogada and vetorAtual[jogo[16]] == -1):
            melhor_posicao = jogo[16]
            encontrou_maior = True
            break

    if encontrou_maior == False:               
        melhor_posicao = jogada_aleatoria(vetorAtual)
        return melhor_posicao, False,None #hovue alteração entao é uma nova partida

    return melhor_posicao, True, idJogo # nao houve alteracao, entao usou exatamente algum jogo anterior

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
                vetor[12] = 1                   
                vetor[13]+=1 #Mais uma vitoria para jogador X
            elif jogador == 2:
                vetor[12] = 2
                vetor[15]+=1 #Mais uma vitoria para jogador O
            return False #Partida acaba
        return False

    #9 jogadas, então acaba e dá velha
    if (vetor[0] == 8):
        if not simulacao:
            #print("Deu velha")
            vetor[12] = -2
            vetor[14]+= 1 #deu velha    
        return False 
    return True  

def jogada_aleatoria(vetorAtual):  
    while True:
        posicao = random.randint(1, 9)
        if vetorAtual[posicao] == -1:
            return posicao

def jogador_invencivel(vetor):
    if vetor[0] == 0:
        return 1

    if vetor[0] == 2:
        for i in [3, 7, 9]:
            if vetor[i] == -1:
                return i #retornando posicao    
            
    # verifica se O poDe GANHAR
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = 2
            if not vencedor(vetor, 2, simulacao=True):
                return i  # 'O' ganha
            vetor[i] = -1 

    # Verifica se X pode ganhar
    for i in range(1, 10):
        if vetor[i] == -1:
            vetor[i] = 1  # Simula jogadas
            if not vencedor(vetor, 1, simulacao=True):  # Se x vencer    
                return i# bloqueia o X
            vetor[i] = -1  #restaura por conta da simulacao

    if vetor[0] == 4:
        if(vetor[5] == -1):
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

jogo = todosJogos[0]
vetor = jogo[2]
print("rank: " ,jogo[1])
for i in vetor:
    print(i)

""" for index, jogo in enumerate(TUDOTESTE):
    print(f"### Jogo {index + 1}:")
    print(f"- Rank: {jogo[1]}")
    
    for jogada_num, jogada in enumerate(jogo[2]):
        jogada_formatada = ', '.join(map(str, jogada))
        print(f"   {jogada_num + 1}. [{jogada_formatada}]")
    print("-"*50) """
 
