
placar = [] #Variavel que guarda o historico de partidas, pode ser zerado durante a partida
tema = []  # variavel que guarda a aparencia do jogo, puramente estetica

def exibe_menu_inicial():
    """Esta função exibe o menu quando o jogo e iniciado"""
    global placar
    print("\nSaudações,\neste e o jogo da velha NUCLEAR!!!\nBora jogar?\n")
    pede_aparencia()
    while True:
        print("\n======================")
        x = input("Escolha um modo de jogo:\n1 = jogador x jogador\n2 = jogador x computador \n3 = sair\n(para selecionar digite o número desejado no console)\n")
        if x in "123": #Confere se o input esta de acordo com o esperado
            if x == "2": # <- input de jogador x computador
                print("\n======================")
                y = input("1 = modo facil\n2 = modo dificil\n(para selecionar digite o número desejado no console)\n") #input para escolher a dificuldade
                placar = [["Jogador",0],["Computador", 0],["Empates",0]] 
                return (int(y)+1)
            if x == "1":# <- input de jogador x jogador
                placar = [["Jogador 1",0],["Jogador 2", 0],["Empates",0]]
                return int(x)
            if x == "3": # <- input para sair
                return print("Obrigado por jogar")
        else: # <- input inesperado 
            print("Talvez você tenha errado o input")

def exibe_menu_pos_jogo():
    """Essa função exibe o menu quando um jogo e terminado(vitoria, ou empate)"""
    while True:
        print("======================")
        x = input("\n1 = jogar novamente \n2 = voltar ao menu \n3 = sair\n(para selecionar digite o número desejado no console)\n")
        if x in "123":
            if x == "1": # <- Diz para o programa continuar neste modo de jogo
                return "jogar novamente" 
            if x == "2": # <- Diz para o programa continuar para o menu principal
                return "menu geral"
            if x == "3": # <- input para sair do jogo
                return print("Obrigado por jogar...")

def exibe_menu_geral():
    """Essa função representa o menu principal do jogo, todas principais alteraçoes são feitas aqui"""
    global placar
    while True:
        print("======================")
        y = input("\n1 = jogador x jogador \n2 = jogador x computador\n3 = alterar a aparencia\n4 = sair\n(para selecionar digite o número desejado no console)\n")
        if y in "1234": # <- Conferindo se o input esta de acordo com o esperado
            if y == "1": # <- input de jogador x jogador
                placar = [["Jogador 1",0],["Jogador 2", 0],["Empates",0]]
                return "jogador x jogador" # <- Diz para o programa jogar com 2 jogadores
            elif y == "2": # <- input de jogador x computador
                placar = [["Jogador",0],["Computador", 0],["Empates",0]]
                z = input("1 = modo facil\n2 = modo dificil\n(para selecionar digite o número desejado no console)\n") #input para escolhera  dificuldade
                if z in "12": # <- Conferindo se o input esta de acordo com o esperado
                    if z == "1":  # <- Diz para o programa jogar com um bot facil
                        return "bot facil" 
                    if z == "2": # <- Diz para o programa jogar com um bot dificil
                        return "bot dificil" 
                else: # <- Input inesperado
                    "Talvez você tenha errado o input"
            elif y == "3": # <- input para alterar a aparencia do jogo
                pede_aparencia()
            elif y == "4": # <- input para sair do jogo
                return print("Obrigado por jogar...")
           


def pede_aparencia():
    """Esta função define a aparencia do jogo a partir do input do usuario, função puramente estetica"""
    global tema
    while True:
        print("======================")
        x = input("\nEscolha uma aparencia para o jogo  \n1 = Padrão \n2 = Nuclear\n3 = Personalizado \n(para selecionar digite o número desejado no console)\n")
        x = list(x)
        if x[0] == str(1): # <- Aparencia padrão do jogo
            tema = ["✕","◯"]
            break
        if x[0] == str(2): # <- Aparencia NUCLEAR 
            tema = ["☢","☠"]
            break
        if x[0] == str(3): # <- Aparencia personalizada
            tema1 = input("Qual a aparencia do jogador 1\n(Digite o simbolo do jogador 1 no console\n")
            tema2 = input("Qual a aparencia do jogador 2\n(Digite o simbolo do jogador 2 no console\n")
            tema = [tema1,tema2]
            break
        if x[0] not in "123": # <- input inesperado
            print("Talvez você tenha errado o tema")


def pede_jogada(jogador):
    """Esta e á função que interage com o usuario na hora de realizar uma jogada, reiniciar ou voltar ao menu
    int -> (alteração no campo)"""
    (print("\nJogador {}\n(Para jogar escreva as coordenadas no console exemplo:(a1, 1a, A1, 1A, a 1, 1 a, A 1, 1 A)\n(Para reiniciar digite 'r' no console, para voltar ao menu digite 'm' no console)".format(jogador)))
    x = input()
    x = str.upper(x) # <- coloca o input em maiusculo, evitando erros do usuario
    x = x.replace(" ","") # <- remove espaços do input, evitando erros do usuario
    if x in "RM": # <- Input R = reiniciar , input M = menu
        return x
    elif len(x) > 1: # <- conferindo se o input esta dentro do esperado
        if x[1] in "ABC": # formatando o input, para que não faça diferença a ordem lina x coluna ou coluna x linha
            x = x[::-1]
            return x
        else:
            return x

def exibe_campo(campo):
    """Esta função e responsavel por mostrar o jogo ao usuario
    ela converte os numeros (-1 0 1) do campo em figuras e as exibe no console
    list -> print"""
    print("\n======================")
    print("\n1 2 3") # <- colunas
    campo1 = [[],[],[]] # <- campo com os valores trocados por figuras 
          ###   Esta parte da função preenche o campo que sera exibido ####
    for i in range(3):
        for j in range(3):
            if campo[i][j] == 0:
                campo1[i].append("☐") # <- um quadrado para representar o espaço vazio
            if campo[i][j] == 1:
                campo1[i].append(tema[0]) # <- a primeira figura da lista(tema) para representar o primeiro jogador
            if campo[i][j] == -1:
                campo1[i].append(tema[1]) # <- a segunda figura da lista(tema) para representar o segundo jogador
          ### Esta parte da função imprime o campo criado acima no console ###
    for i in range(3):
        print(campo1[0][i], end=" ")
    print("A")
    for i in range(3):
        print(campo1[1][i], end=" ")
    print("B")
    for i in range(3):
        print(campo1[2][i], end=" ")
    print("C")

def exibe_ganhador(ganhador):
    """Esta função e acionada quando alguem vence ou o jogo empata, ela analisa se alguem venceu, imprime o resultado e o placar
    str -> print"""
    if ganhador == "Velha": # <- Deu Velha
        print("deu velha\n")
        placar[2][1] += 1
    else:
        print("\nO {} ganhou!!!!\n".format(placar[ganhador][0])) # <- Alguem ganhou
        placar[ganhador][1] += 1
    print("======================\n{} = {}\n{} = {}\n{} = {}".format(placar[0][0],placar[0][1],placar[1][0],placar[1][1],placar[2][0],placar[2][1]))
