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
vetor = [0,
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,-1,
        0,0,0,0,0,0,0,0]

vetorJogos = [] #guardar cada jogada aqui

def jogo_da_velha(vetor):
    quantidade_jogos = int(input("Quantos jogos deseja ? "))
    opcao = int(input("1. Random x Random\n2. Inteligente x Random\nOpcao: "))
    for _ in range(quantidade_jogos):
        jogar = True
        vetor[0] = 0
        vetor[1:10] = [-1]*9
        while (jogar == True):
            if (opcao == 1):
                posicao = jogada_aleatoria(vetor)

                if (vetor[0] % 2 == 0):              
                    vetor[posicao] = 1
                    jogador = 1
                else:
                    vetor[posicao] = 0
                    jogador = 0
            if (opcao == 2):         
                if (vetor[0] % 2 == 0):      
                    if jogador_inteligente(vetorJogos, vetor[0]):
                        posicao = jogador_inteligente(vetorJogos, vetor[0])
                    vetor[posicao] = 1
                    jogador = 1
                else:
                    posicao = jogada_aleatoria(vetor)
                    vetor[posicao] = -3
                    jogador = -3
                
            vetor[16] = posicao
            vetor[17] = jogador
            
            jogar = vencedor(vetor, jogador) 
            vetorJogos.append(vetor.copy())

            vetor[0]+=1

        if (jogar == False and vetor[12] == 1): # JOGADOR X
            for jogo in vetorJogos:
                jogo[11]+=3
        if (jogar == False and vetor[12] == -3): # jogador O
            for jogo in vetorJogos:
                jogo[11]-=2 
        if (jogar == False and vetor[12] == -2): #VELHA
            for jogo in vetorJogos:
                jogo[11]-=1   
        
                     
        vetor[10]+=1 #+1 jogo
        #print("+1 jogo")
        if (opcao == 2):
            with open("inteligente_aleatorio11.csv", 'a') as f:
                for item in vetor:
                    f.write(f"{item};")
                f.write("\n")

def jogador_inteligente(vetorJogos, jogada):
    #Jogada 1: Se na jogada 1 o vetor na posicao 11 tive rank, lá que vai ser e assim por diante
    #vou percorrer o vetor e marcar 1 se o jogo tiver dado vitoria para o X
    #primeira jgoada é aleatoria
    maiorRank =0
    melhor_posicao =0
    encontrou_maior = False
    #print(vetorJogos)

    if not vetorJogos:
        melhor_posicao = random.randint(1,9)
        
    for jogo in vetorJogos:
        if (jogo[10] == 0):
            melhor_posicao = jogada_aleatoria(jogo)
    #PRIMEIRA JOGADA, NÃO ENTR AQUI, POIS VETORJOGOS ESTÁ VAZIO
    
    for jogo in vetorJogos:  
        if (jogo[0] == jogada):
            #print("a")
            if (jogo[11] > maiorRank):
                maiorRank = jogo[11]
                melhor_posicao = jogo[16]
                encontrou_maior = True

            if encontrou_maior == False:
                melhor_posicao = jogada_aleatoria(jogo)


    return melhor_posicao

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
            elif jogador == -3:
                vetor[12] = -3
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

def jogada_aleatoria(vetor):  
    posicoes_livres = []
    for i in range(1,10):
        if (vetor[i] == -1):
            posicoes_livres.append(i)

    if posicoes_livres:
        posicao = random.choice(posicoes_livres)
        return posicao


jogo_da_velha(vetor)



""" for jogo in vetorJogos:
    print(jogo)
 """
print("-----")
print(vetor)

