from UNO import *
system('cls')


while True:
    Vez()
    if chave == ' ':
        VerCartasCompetidores()
    MostrarJogadores()
    MostrarCartas(Jog[3])
    AcaoCarta()
    system('cls')
    if Finalizar()==False:
        break