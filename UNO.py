from random import randint, choice
from os import system
from xmlrpc.client import boolean
from collections import Counter
from introducao import Explicando
from time import sleep


def datar(x):
    with open('Historico.txt', 'a') as arquivo:
        arquivo.write(f"{x}\n")


class Carta:
    def __init__(self, cor, valor, validar=0):
        valores = ['verm', 41, 'verd', 42, 'amar', 43, 'azul', 44, 'bran', 47]
        self.cor = cor
        self.numcor = valores[valores.index(cor)+1]
        self.valor = valor

        if type(validar) == boolean:
            self.validacao = validar
        else:
            self.validacao = True if '+' in self.valor else False


def CriarTodasCartas():
    """
        Cria todas as cartas do jogo em formato de objeto e adiciona todas elas em uma lista
    Retorna: Uma lista com todas as cartas em objeto
    """

    x = list()
    for cor in ['verm', 'verd', 'amar', 'azul']:
        [x.append(Carta(c, v))
         for v, c in [['#', 'bran'], ['+4', 'bran'], ['0', cor]]]
        [x.append(Carta(cor, valores)) for i in range(1, 3) for valores in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '<>', '+2']]
    return x


def MostrarCartas(CartasProprias, CartasPorColuna=12):
    """
        Mostra as cartas da lista na tela
    EspacoCartas --> O numero de cartas que cada fileira ira suportar
    CartasProprias --> Refere-se as proprias cartas na mao do jogador
    """

    sep = [CartasProprias[i:i+CartasPorColuna]
           for i in range(0, len(CartasProprias), CartasPorColuna)]
    numero = 0
    for i1 in sep:
        for pos in ['', '>', '^', '<']:
            for i2 in i1:
                numero += 1 if pos == '' else 0
                print(f"\033[1;30;{i2.numcor}m {f'{i2.valor}' if pos != '^' else 'UNO':{pos}3} \033[m" if pos !=
                      '' else f"{f' [{numero}] ':.5}", end=" ")
            print()
        print()


def SepararCartas(Quantidades=7):
    """
        Separa todas as cartas para os jogadores tirando do <pacoteCartas>
    quantidades --> será a quantidade de cartas que o jogador ira receber para iniciar o jogo
    Retorna: Uma um dicionario com a lista de cartas de todos os jogadores e a chave deles são: 0, 1, 2, 3
    """

    x = dict()
    for i in range(4):
        jogoCartas = list()
        for i1 in range(0, Quantidades):
            escolhido = choice(pacote_cartas)
            jogoCartas.append(escolhido)
            pacote_cartas.remove(escolhido)
        x[i] = jogoCartas
    return x


def MostrarJogadores():  #Ajustar para PyCharm
    """
        Mostra os jogadores com suas quantidades de cartas e a carta na mesa
    """

    x = [46, 46, 46, 46]
    x[vez] = 45

    espL = ' '*15
    espA = '\n'*3
    Jog2_espL = ' '*21
    setas = ' '*21

    for i1 in ['>', '^', '<']:
        print(f"{Jog2_espL}\033[1;30;{x[1]}m {f'{len(Jog[1])}':{i1}3} \033[m" if i1 !=
              '^' else f"{Jog2_espL}\033[1;30;47m Jo2 \033[m")
    print()

    print(
        f"{espA}{Jog2_espL}\033[1;30;47m +{f'{empilhar}':>2} \033[m" if empilhar > 0 else espA)

    print(setas, "-->" if lado == True else "<--")
    for i1 in ['>', '^', '<']:
        for cor, valor, nome in zip([x[0], carta_mesa.numcor, x[2]], [len(Jog[0]), carta_mesa.valor, len(Jog[2])], ['Jo1', 'UNO', 'Jo3']):
            print(f"\033[1;30;{cor}m {f'{valor}':{i1}3} \033[m{espL}" if i1 !=
                  '^' else f"\033[1;30;{47 if nome != 'UNO' else carta_mesa.numcor}m {f'{nome}':{i1}3} \033[m{espL}", end=" ")
        print()
    print(setas, "<--" if lado == True else "-->")
    print('\n\n')


def Vez():
    """
        Mostra uma lista com os valores que decidem a vez do jogador
        Se <lado> for True, será sentido horario, se False antido anti horario
    """
    global vez, lado
    vez = randint(0, 3) if vez == -1 else vez

    if lado == True:
        vez = vez+1 if vez < 3 else 0
    else:
        vez = vez-1 if vez > 0 else 3


def VerCartasCompetidores():
    """
        Mostra as cartas dos outros jogadores para analizar 
    """
    global vez
    for i in range(3):
        print(f"\033[1;35mJOGADOR - [ {i+1} ] \033[m" if vez == i else f"Jogador-{i+1}")
        MostrarCartas(Jog[i])


def EscolherCarta():
    """
        Se trata de retornar a carta escolhida levando em consideração se esta fazendo a escolha correta, como;
        se a carta de descarte possui as mesmas informações da carta da mesa como cor e valor
        ou se esta os jogadores estao jogando +4 ou +2 para somar as cartas de compra, então deve ser jogar carta de soma

        A maquina tambem escolhe sua propria carta se caso ela tiver e a maquina tambem possui a inteligencia de
        jogar carta de soma se caso ela precise fazer isso

    Retorna: A propria carta da escolha em Objeto
    """

    global vez, Jog, carta_mesa
    if vez == 3:  # Se caso for a sua vez
        while True:
            escolha = str(input(">> "))
            # Filtrando o valor da escolha, para voce não colocar valor incorreto
            if escolha.isnumeric() and int(escolha) <= len(Jog[vez]) and int(escolha) > 0:
                escolha = Jog[vez][int(escolha)-1]
                if carta_mesa.validacao == True:
                    if escolha.validacao == True:
                        return escolha  # Retorno de carta para somar
                    else:
                        print(
                            "ESSA CARTA NÃO SERVE COMO SOMA\nPrecione ENTER se deseja comprar")
                # caso nao estiver acontecendo somas
                elif set([carta_mesa.cor, carta_mesa.valor, 'bran']).isdisjoint([escolha.cor, escolha.valor]) == False:
                    # Retorno de carta normal (não sendo de somas)
                    return escolha
                else:
                    print("Os valores dessa carta não correspondem")
            elif escolha == '':
                return False  # Retorna False se for para comprar uma carta os as cartas de pilhagem
            else:
                print("Valor ou respota INCORRETA\nPrecione ENTER se deseja comprar")

    else:  # Se caso for a vez da maquina
        if chave == ' ':
            input("<<<")
        else:
            sleep(randint(2,3))
        if carta_mesa.validacao == True:
            for carta in Jog[vez]:
                if '+' in carta.valor:
                    return carta  # Retorna uma carta de soma
            return False  # Retorna nada pois não possui uma carta de soma, então esse player deve comprar as cartas
        else:
            found = False
            for carta in Jog[vez]:
                if set([carta_mesa.cor, carta_mesa.valor, 'bran']).isdisjoint([carta.valor, carta.cor]) == False and carta.numcor != 47:
                    # Retorna uma carta normal (Não sendo +4 e nem Troca_De_Cor)
                    return carta
                if set([carta.numcor]).isdisjoint([47]) == False:
                    found = carta
            return found  # Retorna o +4 e o Troca_De_Cor, ou False se cado não encontrar nenhum dos dois


def ComprarCarta(QuantCartas):
    """
        Irá fazer o jogador comprar uma certa quantidade de cartas
    QuantCartas -> O valor numerica de quantas cartas o jogador irá comprar
    """
    global pacote_cartas

    try:
        for i in range(QuantCartas):
            escolha = choice(pacote_cartas)
            Jog[vez].append(escolha)
            pacote_cartas.remove(escolha)
        datar(f"Jogador[{vez+1}] Comprou {QuantCartas}x {'Carta' if QuantCartas == 1 else 'Cartas'}\n")
    except:
        print("Não há mais cartas no pacote, os jogadores usaram tudo")
        exit()


def TrocaLado():
    """
        Ira alterar de True pra False e de False para True, ja que o lado do
        jogo varia de True -> Horario e False -> Anti horario
    """
    global lado
    if lado == True:
        lado = False
    else:
        lado = True


def Reciclando(escolha):
    """
        Se trata de descartar a carte e devolver ela pro pacote
    """
 
    Jog[vez].remove(escolha)
    pacote_cartas.append(escolha)
    datar(f"Jogador[{vez+1}] Descartou [ {escolha.valor} - {escolha.cor} ]\n")


def AcaoCarta():
    """
    - Recebe o retorno da <EscolhaCarta()> e descarta a carta caso a carta tenha sido retornada
    - Faz a tarefa de somar as cartas de compras dos player que jogam estas cartas
    - Lida com a compra de cartas caso o jogador não tenha a carta ou se alguem fez ele comprar com cartas de compra
    - Faz a cartas de troca de cores receberem uma cor escolhida levando em consideração à escolha do jogador ou da maquina
    - Se caso o jogador comprar uma carta e for compativel com a carta que esta na mesa o jogador pode escolher jogar essa carta
    """

    global carta_mesa, empilhar, umavez

    if umavez == True: #Fazer a primeira carta que for lançada na mesa valer
        escolha = EscolherCarta()
    else:
        Jog[vez].append(carta_mesa)
        escolha = carta_mesa
        umavez = True

    if escolha == False: #Verificando se o jogador NÃO retonou uma carta
        if empilhar > 0: #Se empilhar entiver acima de 0, significa que os jogadores estavam jogando cartas de soma
            ComprarCarta(empilhar) #Então esse jogador ira comprar toda a pilha de cartas que foi somada
            empilhar = 0
            carta_mesa.validacao = False
        else:
            ComprarCarta(1)
            if set([Jog[vez][-1].valor, Jog[vez][-1].cor]).isdisjoint(set([carta_mesa.cor, carta_mesa.valor, 'bran'])) == False: #Caso o jogador compre uma carta e essa carta for compativel com a carta que esta na mesa
                if vez == 3: #Verificando a sua vez
                    MostrarCartas([Jog[vez][-1]])
                    resultado = input("Precione [ENTER] para jogar ou [ESPACO+ENTER] para guardar\n>> ")
                    if resultado == '':
                        escolha = Jog[vez][-1]
                        datar(f"Jogador[{vez+1}] Carta De Compra [{escolha.valor} - {escolha.cor}] Compativel com a carta de descarte")
                else: #Fazendo a maquina jogar automaticamente se a carta comprada for compativel
                    escolha = Jog[vez][-1]
                    if chave == ' ':
                        print("[Maquina] - Carta Compativel Com o Descarte!")
                        MostrarCartas([escolha])
                        input("<<>>")
                    datar(f"Jogador[{vez+1}] Carta De Compra [{escolha.valor} - {escolha.cor}] Compativel com a carta de descarte")
            carta_mesa.validacao = False

    if escolha != False: #Se caso retornou um carta
        if '+' in escolha.valor: #Trabalando com a soma dos valores
            empilhar += int(escolha.valor[1])
        
        if escolha.numcor == 47: #Trabalhando com a alteracao da carta de troca de cor
            if vez+1 == 4: #Verificando se é a sua vez
                for i in range(3):
                    x = [1, 2, 3, 4] if i == 1 else ['', '', '', '']
                    for cor, num in zip([41, 42, 43, 44], x):
                        print(f"\033[1;30;{cor}m {f'[ {num} ]' if i == 1 else '     '} \033[m   ", end=" ")
                    print()

                while True: #Escolha do jogador(voce) de escolher a cor das cartas de troca de cor
                    valor = str(input(">> "))
                    if valor.isnumeric() and int(valor)>0 and int(valor)<5:
                        carta_mesa = Carta(['verm','verd','amar','azul'][int(valor)-1], escolha.valor)
                        Reciclando(escolha)
                        return None
                    print("Escolha INVALIDA! Tente de novo...")

            else: #Vez das maquinas de escolher qual cor da carta de troca de cor elas querem levando em consideração as cartas proprias
                cores = [x.cor for x in Jog[vez] if x.numcor != 47]
                if len(cores) > 0:
                    carta_mesa = Carta(Counter(cores).most_common(1)[0][0], escolha.valor) #Verificando quais são as cores que mais se repetem para escolher essa cor
                else:
                    carta_mesa = Carta(choice(['verm','verd','amar','azul']), escolha.valor) #Se caso não tiver nenhum carta de cor, então ira escolher uma cor aleatoria
                Reciclando(escolha)
                return None
        
        if escolha.valor == '<>': #Trocando a direcao do jogo
            TrocaLado()
        
        if escolha.valor == 'X': #Passando a vez do jogador
            carta_mesa = escolha
            Reciclando(escolha)
            Vez()
            return None
        carta_mesa = escolha
        Reciclando(escolha)
    
        
def CartaDaMesa():
    """
        Funcao criada para gerar uma carta para a carta que ficara na mesa
    Retorna: Uma carta para a mesa
    """

    global carta_mesa

    escolha = choice(pacote_cartas)
    pacote_cartas.remove(escolha)
    return escolha


def Finalizar():
    if len(Jog[vez])==0:
        print(f"Jogador[{vez+1}] Venceu o Jogo!")
        return False


chave = Explicando()
pacote_cartas = CriarTodasCartas()
carta_mesa = CartaDaMesa()
Jog = SepararCartas(7)
lado = True
vez = -1
empilhar = 0
umavez = False


