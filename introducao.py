from os import system
arquivo = open('Historico.txt', 'w+')
arquivo.close()

def Explicando():

    input("""
É importante que para iniciar, utilize o Visual Studio Code para rodar o programa ---
pois vai entregar uma experiência melhor na visualização das cartas                ꓥ
e expanda seu terminal ao nivel á seguir...                                        |
                                                                                   |
                                                                                   |
Qualquer alterção que ocorra no tamanho do terminal do VsCode deforma as           |
cartas, mas basta passar pra proxima jogada que volta ao normal                    |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                           Nivel do tamanho  --->  |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                                                                   |
                                  ꓥ                                                |
                                  |                                                |
                                  |                                                |
                          Olha la pra cima                                         |
                                                                                   |
                                                                                   V
Expanda seu terminal até pegar todo o nivel do tamanho            -->             ---
Precione [ENTER]
>>""")

    system('cls')

    input(f"""O jogo foi criado seguindo as regras que eu jogava com meus amigos
Isso significa que, a carta de +4 não possui o modo Desafiar Jogador
ela pode ser somada com cartas de +2 e vice-versa independente da cor

\033[1;30;41m  +2 \033[m     \033[1;30;42m  +4 \033[m     \033[1;30;44m  +2 \033[m     \033[1;30;43m  +4 \033[m
\033[1;30;41m UNO \033[m  +  \033[1;30;42m UNO \033[m  +  \033[1;30;44m UNO \033[m  +  \033[1;30;43m UNO \033[m  =  +12
\033[1;30;41m +2  \033[m     \033[1;30;42m +4  \033[m     \033[1;30;44m +2  \033[m     \033[1;30;43m +4  \033[m
    
Precione [ENTER]
>>""")

    system('cls')

    input(f"""
 Numero de cartas --->  \033[1;30;46m   7 \033[m
      que o             \033[1;30;47m Jo4 \033[m  <--- Nome do Jogador (Isso não importa nada kk)
  jogador possui  --->  \033[1;30;46m 7   \033[m

     Quando o    --->   \033[1;30;45m   7 \033[m
   Jogador esta         \033[1;30;47m Jo4 \033[m
      na vez     --->   \033[1;30;45m 7   \033[m



\033[1;30;44m  <> \033[m
\033[1;30;44m UNO \033[m =-> Carta De Inversão
\033[1;30;44m <>  \033[m

\033[1;30;47m   # \033[m
\033[1;30;47m UNO \033[m =-> Carta De Troca De Cor
\033[1;30;47m #   \033[m

\033[1;30;41m   X \033[m
\033[1;30;41m UNO \033[m =-> Carta De Bloqueio
\033[1;30;41m X   \033[m

Precione [ENTER]
>>""")

    system('cls')

    escolha = input("""
Há um arquivo de historico de jogadas
onde você pode analizar todos os
movimentos das cartas. Mas se quiser
uma analizada melhor Precione [ESPACO+ENTER]
------------------- OU ---------------------

Precione [ENTER] Para Jogar Normalmente
>>""")

    system('cls')
    
    if escolha == ' ':
        input("""
                                                                                    ---
                                                                                     ꓥ
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                            Nivel do tamanho  --->   |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
                                                                                     |
É importante que você expanda quase 100% do seu terminal para                        |
utilizar essa função na melhor experiência                                           |
                                                                                     V
Precione [ENTER]                                                                    ---
>>""")                                                                        
    return escolha
