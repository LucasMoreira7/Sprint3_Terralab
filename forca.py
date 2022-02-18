import random
import forca



def jogar():
    forca.abertura()

    palavra_secreta = forca.sorteio_palavra()

    palavra_tratada = forca.letrasTratadas(palavra_secreta)

    print(palavra_tratada)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = recebe_chute()

        if(chute in palavra_secreta):
            marca_letras_corretas(chute,palavra_tratada,palavra_secreta)##--##
        else:
            
            tentativas += 1
            desenha_forca(tentativas)
        enforcou = tentativas == 7
        acertou = "_" not in palavra_tratada
        

        print(palavra_tratada)

    if(acertou):
        imprime_venceu()
    else:
        imprime_perdeu(palavra_secreta)

    print(".................................")
    print("          Fim do jogo.           ")
    print(".................................")


def abertura():
    print("---------------------------------")
    print("Bem vindo ao jogo de Forca!")
    print("---------------------------------")

def sorteio_palavra():
    file = open("palavras.txt", "r")
    palavras = []

    for linha in file:
        linha = linha.strip()
        palavras.append(linha)

    file.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()
    return palavra_secreta

def letrasTratadas(palavra_secreta):
    letras = ["_" for letra in palavra_secreta]
    return letras

def recebe_chute():
    chute = input("Digite uma letra:")
    chute = chute.strip().upper()
    return chute

def marca_letras_corretas(chute,palavra_tratada,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):  # sempre analiza letras maiúculas
            palavra_tratada[index] = letra
        index += 1

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(tentativas == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (tentativas == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_perdeu(palavra_secreta):
    print("você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ =="__main__"):
    jogar()
