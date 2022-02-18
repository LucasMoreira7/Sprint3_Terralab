def jogar():
    import random
    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")


    numeroSecreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("qual o nível de dificuldade desejado?")
    print("(1)-Fácil, (2)-Médio, (3)-Difícil")

    nivel = int(input("Defina o nível:"))

    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 3


    for rodada in range(1,tentativas + 1):
        print("Tentativa {} de {}:".format(rodada, tentativas), end="\n")
        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)
        print("Você digitou o número",chute,".",end = "\n")

        if(chute < 1 or chute >100 ):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = chute == numeroSecreto
        maior   = chute > numeroSecreto
        menor   = chute < numeroSecreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou!, seu chute foi maior que o número secreto!", end="\n")
            elif (menor):
                print("Você errou!, seu chute foi menor que o número secreto!", end="\n")
            pontosPerdidos = abs(numeroSecreto-chute)
            pontos = pontos - (pontosPerdidos)
            print("")
        print("\n")


    print(".................................")
    print("          Fim do jogo.           ")
    print(".................................")

if(__name__ =="__main__"):
    jogar()