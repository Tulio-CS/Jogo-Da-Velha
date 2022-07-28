import interface_grafica as ig
from random import randint


def main():
    """Esta e a funcão que inicia o jogo, o primeiro menu que aparecera, é acionada somente uma vez"""
    comando = ig.exibe_menu_inicial() # <- chama a função que exibe o menu inicial no console
    if comando == 1: # <- input para jogador x jogador
        jogo_2_jogadores() 
    if comando == 2: # <- input para jogador x bot facil
        jogo_bot_facil()
    if comando == 3: # <- input para jogador x bot dificil
        jogo_bot_dificil()

def gerador_de_campo():
    """Esta e a função que gera o campo para o jogo da velha"""
    campo = []
    for i in range(3):
        campo.append(3*[0])
    return campo

    
def jogo_2_jogadores():
    """Esta e a função que gerencia o modo jogador x jogador, analisa se e possivel jogar, 
    em caso positivo analisa quem deve jogar(jogador 1 ou jogador 2)"""
    campo = gerador_de_campo() # <- cria uma variavel(matriz com o campo do jogo)
    acao = 0 # acao e uma variavel utilizada para registrar o numero de jogadas e a vez de cada jogador
    while condicao_vitoria(campo) == 0 : # <- analisa se alguem ganhou
        ig.exibe_campo(campo) # <- imprime o campo no console 
        campo = altera_campo(campo,(acao%2),jogo_2_jogadores) # <- pede o input ao usuario e altera o campo
        if campo == "R": # <- input para reiniciar
            return reinicia(jogo_2_jogadores)
        elif campo == "M": # <- input para voltar ao menu
            return menu_geral()
        acao += 1 # <- passa a vez quando um jogador realiza uma jogada
    acao -=1 # retorna a jogada em um, para que o placar fique correto, pois o jogador fez a jogada que ganhou e passou sua vez
    ultimo_jogador = (acao%2) # <- diz quem foi o ultimo jogador a jogar
    checa_ganhador(ultimo_jogador,campo) # <- analisa quem foi o ganhador
    menu_pos_jogo(jogo_2_jogadores) # <- chama o menu pos jogo

def jogo_bot_facil():
    """Esta e a função que gerencia o modo jogador x bot facil, gerencia a vez do jogador e do computador, 
    e analisa se alguem ganhou"""
    campo = gerador_de_campo() # <- cria uma variavel(matriz com o campo do jogo)
    while condicao_vitoria(campo) == 0: # Analisa se alguem ganhou
        ultimo_jogador = 0 # <- mantem salvo que foi o ultimo a jogar
        ig.exibe_campo(campo) # <- exibe o campo no console
        campo = altera_campo(campo,0,jogo_bot_facil) # <- altera o campo de acordo com o input do usuario
        if campo == "R": # <- input para reiniciar
            return reinicia(jogo_bot_facil)
        elif campo == "M": # <- input para voltar ao menu
            return menu_geral()
        if condicao_vitoria(campo) == 0: # <- checa se o jogador ganhou na linha acima
            campo = jogada_bot_facil(campo) # <- realiza uma jogada para o bot facil(aleatoriamente)
    checa_ganhador(ultimo_jogador,campo) # <- checa quem ganhou a partida
    menu_pos_jogo(jogo_bot_facil) # <- chama o menu do pos jogo

def jogada_bot_facil(campo):
    """Esta fução realiza a jogada do bot facil, sua decisão e escolhida aleatoriamente, por isso sua dificuldade
    e considerada facil
    list(matriz com o campo) -> list(matriz com o campo alterado)"""
    while True: # <- Realizar a jogada aleatoriamente ate que seja escolhida uma jogada possivel
        jogada_linha = randint(0,2) # <- jogada na linha(aleatoriamente)
        jogada_coluna = randint(0,2) # <- jogada na coluna(aleatoriamente)
        if campo[jogada_linha][jogada_coluna] == 0: # <- checa se a jogada do bot e possivel
            campo[jogada_linha][jogada_coluna] = -1 # <- altera o campo com a jogada do bot
            return campo


def jogo_bot_dificil():
    """Esta e a função que gerencia o modo jogador x bot dificil, gerencia a vez de jogar do jogador e do computador
    e analisa se alguem ganhou"""
    campo = gerador_de_campo() # <- cria uma matriz(campo de jogo) como variavel
    while condicao_vitoria(campo) == 0: # <- checa se alguem ganhou
        ig.exibe_campo(campo) # <- imprime o campo no console 
        campo = altera_campo(campo,0,jogo_bot_dificil)# <- altera o campo de acordo com o input do usuario
        if campo == "R": # <- input para reiniciar
            return reinicia(jogo_bot_dificil)
        elif campo == "M": # <- input para voltar ao menu
            return menu_geral()
        ultimo_jogador = 0 # <- mantem salvo que foi o ultimo a jogar 
        if condicao_vitoria(campo) == 0: # <- checa se o jogador ganhou na linha acima
            campo = jogada_bot_dificil(campo) # <- pede a jogada ao bot dificil
            ultimo_jogador = 1 # <- mantem salvo que foi o ultimo jogador 
    checa_ganhador(ultimo_jogador,campo) # <-analisa quem foi o vencedor 
    menu_pos_jogo(jogo_bot_dificil) # <- chama o menu pos jogo

def jogada_bot_dificil(campo):
            ########################################################################################
            # O bot na dificuldade dificil e uma maquina especialista, isto é, segue um padrão de  #
            # jogadas para que se torne impossivel ganhar dela, na wikipedia do jogo da velha é    #
            # possivel encontrar um diagrama com todos os passos para a criação da jogada perfeita #
            # os passos são os seguintes :                                                         #
            # 1 - Se você pode ganhar, faça a jogada que vai te garantir a vitoria imediata        #
            # 2 - se o oponente pode ganhar imediatamente, jogue de forma a bloqueá-lo             #
            # 3 - Triangulaçoes, crie mais de uma forma de ganhar (preferencialmente pelo meio)    #
            #     ☢ ▢ ☢              ▢ ☢ ▢          ☢ ▢ ☢                                     # 
            #     ▢ ▢ ▢              ▢ ☢ ☢          ▢ ☢ ▢                                     #
            #     ☢ ▢ ▢              ▢ ▢ ▢          ▢ ▢ ▢                                     #
            #   3.1 - Jogue de forma a criar triangulaçoes a favor                                 #
            #   3.2 - Jogue de forma a bloquear as triangulaçoes do oponente                       #
            # 4 - Jogue no centro                                                                  #
            # 5 - Jogue num canto                                                                  #
            ########################################################################################              
            
            ########################################################################################
            #                                   PASSO 1                                            #
            ########################################################################################
                # Checando linhas para ganhar
            for i in range(3):  
                if sum(campo[i]) == -2:
                    campo[i][campo[i].index(0)] = -1
                    return campo 
                #Checando colunas para ganhar
            for i in range(3):
                soma = 0
                for j in range(3):
                    soma += campo[j][i]
                    if soma == -2:
                        for j in range(3):
                            if campo[j][i] == 0:
                                campo[j][i] = -1
                                return campo
                #Checando diagonais para ganhar
            if campo[0][0] + campo[1][1] + campo[2][2] == -2:
                for i in range(3):
                    if campo[i][i] == 0:
                        campo[i][i] = -1
                        return campo
            if campo[0][2] + campo[1][1] + campo[2][0] == -2:
                for i in ([0,2],[1,1],[2,0]):
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo
            ########################################################################################
            #                                   PASSO 2                                            #
            ########################################################################################
                # Checando linhas para impedir o oponente de ganhar
            for i in range(3):
                if sum(campo[i]) == 2:
                    campo[i][campo[i].index(0)] = -1
                    return campo
                #Checando colunas para impedir o oponente de ganhar
            for i in range(3):
                soma = 0
                for j in range(3):
                    soma += campo[j][i]
                    if soma == 2:
                        for j in range(3):
                            if campo[j][i] == 0:
                                campo[j][i] = -1
                                return campo
                #Checando Diagonais para impedir o oponente de ganhar
            if campo[0][0] + campo[1][1] + campo[2][2] == 2:
                for i in range(3):
                    if campo[i][i] == 0:
                        campo[i][i] = -1
                        return campo
            if campo[0][2] + campo[1][1] + campo[2][0] == 2:
                for i in ([0,2],[1,1],[2,0]):
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo
            ########################################################################################
            #                                   PASSO 3                                            #
            ########################################################################################            
             ######################### Triangulaçoes a favor #######################################
            if campo[1][1] == 0: # <- checando se o meio esta ocupado
                campo[1][1] = -1  # <- jogando no meio (campo mais importante, pois possui o dobro de triangulaçoes)
                return campo
                        #Estrategia de triangulação pelo meio  
            if campo[1][1] == -1: #<- checando se o meio foi ocupado pelo computador ou pelo jogador
                for i in ([2,1],[1,2],[0,1],[1,0]): # <- jogando nas bordas(Estrategia 1 de triangulação)
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo
                for i in ([2,2],[0,2],[0,0],[2,0]): # <- jogando nos cantos(Estrategia 2 de triangulação)
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo 
                        #Triangulação pelos cantos 
            else: # <- meio foi ocupado pelo jogador, existe apenas uma estrategia de triangulação
                for i in ([2,2],[0,2],[0,0],[2,0]): # <- (Estrategia de tiangulação pelos cantos)
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo 
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo
                for i in ([2,1],[1,2],[0,1],[1,0]): # <- Em ultimo caso, jogar nos espaços vazios das bordas (casos especificos)
                    if campo[i[0]][i[1]] == 0:
                        campo[i[0]][i[1]] = -1
                        return campo

def altera_campo(campo,valor,modo_de_jogo):
    """Esta e a função que é chamada para realizar uma jogada(alterar o campo)
    list(matriz com o campo do jogo),int,str -> list(matriz com o campo do jogo ja alterado)"""
    linha = {"A":0,"B":1,"C":2} # <- Dicionario com as linhas, usado para alterar o campo
    coluna = {"1":0,"2":1,"3":2} # <- Dicionario com as colunas, usado para alterar o campo
    while True:
        comando = ig.pede_jogada(valor) # <- pede um input para o jogador 
        if comando == "R": # <- input para reiniciar  o jogo
            return comando
        elif comando == "M": # <- input para voltar para o menu principal
            return comando
        elif comando[0] in "ABC" and comando[1] in "123": # <- conferindo se o input esta dentro do esperado
            if campo[linha[comando[0]]][coluna[comando[1]]] == 0: # <- conferindo se o espaço escolhido esta vazio
                valor += 1 
                if valor == 2: # alterando o numero do jogador(2) para sua representação no campo do jogo (-1)
                    valor = -1 
                campo[linha[comando[0]]][coluna[comando[1]]] = valor # <- altera o campo de jogo de acordo com o input do usuario
                break
            else:
                ig.exibe_campo(campo)
                print("Esse campo ja foi escolhido") # <- campo escolhido pelo usuario ja foi preenchido
        else:
            ig.exibe_campo(campo)
            print("Talvez você tenha errado o input") # <- input inesperado
    return campo


def checa_ganhador(ultima_jogada,campo):
    """Esta função checa quem se houve um ganhador, em caso positivo ela retorna quem foi o ganhador
    int, list(matriz com o campo) -> function"""
    ig.exibe_campo(campo)
    if condicao_vitoria(campo) == 2:
        ig.exibe_ganhador("Velha")
    else:
        ig.exibe_ganhador(ultima_jogada)


def condicao_vitoria(campo):
    """Essa função checa se alguem venceu o jogo, realizando a soma das jogadas(1 para o jogador 1 e -1 para o bot ou jogador 2)
    se a soma nas linhas, colunas ou diagonais foi igual a -3 ou 3 quer dizer que alguem ganhou o jogo
    retorno 0 = ninguem ganhou o jogo e ainda não aconteceu um empate
    retorno 1 = alguem ganhou o jogo
    retorno 2 = empate ou "velha" """
    #linas
    if campo[0][0]+campo[0][1]+campo[0][2] == 3 or campo[1][0]+campo[1][1]+campo[1][2] == 3 or campo[2][0]+campo[2][1]+campo[2][2] == 3:
        return 1
    if campo[0][0]+campo[0][1]+campo[0][2] == -3 or campo[1][0]+campo[1][1]+campo[1][2] == -3 or campo[2][0]+campo[2][1]+campo[2][2] == -3:
        return 1
    #colunas
    if campo[0][0]+campo[1][0]+campo[2][0] == 3 or campo[0][1]+campo[1][1]+campo[2][1] == 3 or campo[0][2]+campo[1][2]+campo[2][2] == 3:
        return 1
    if campo[0][0]+campo[1][0]+campo[2][0] == -3 or campo[0][1]+campo[1][1]+campo[2][1] == -3 or campo[0][2]+campo[1][2]+campo[2][2] == -3:  
        return 1
    #diagonais
    if campo[0][0]+campo[1][1]+campo[2][2] == 3 or campo[0][2]+campo[1][1]+campo[2][0] == 3:        
        return 1
    if campo[0][0]+campo[1][1]+campo[2][2] == -3 or campo[0][2]+campo[1][1]+campo[2][0] == -3:      
        return 1
    #Velha 
    if 0 not in campo[0] and 0 not in campo[1] and 0 not in campo[2]:
        return 2
    return 0

def menu_geral():
    """Esta funçao é o menu principal, aqui é possivel alterar qualquer detalhe no jogo
    é chamado exclusivamente pelo input do usuario"""
    comando = ig.exibe_menu_geral() # <- imprime o menu principal na tela    
    if comando == "sair": # <- input inesperado ou usuario saindo do jogo
        return exit()
    else: # <- analisando se o input e valido
        return comando()

def menu_pos_jogo(modo_de_jogo):
    """Esta função é responsavel por administrar o jogo em caso de empate ou vitoria
    pode recomeçar o jogo, ir para o menu principal ou sair do jogo
    str -> function"""
    comando = ig.exibe_menu_pos_jogo() # <- imprime o menu na tela
    if comando == "jogar novamente": # <- input para jogar novamente, utiliza o dicionario acima para chamar a função dos jogos
        return modo_de_jogo()
    if comando == "menu geral": # <- input para ir para o menu principal
        return menu_geral()
    elif comando == "sair": # erro de input ou usuario saindo do jogo
        return exit()

def reinicia(modo_de_jogo):
    """Esta função reinicia o jogo, precisa do modo de jogo para continuar no mesmo modo
    str -> function"""
    return modo_de_jogo() # <- reinicia o jogo de acordo com o modo de jogo

        
if __name__ == "__main__":
    main()