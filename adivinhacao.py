import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!!")
    print("**Adivinhe um número de 01 a 100**")
    print("* Boa Sorte!!! *")
    print("****************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100
    perca_pontos = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
        perca_pontos = 5
    elif(nivel == 2):
        total_de_tentativas = 10
        perca_pontos = 10
    else:
        total_de_tentativas = 5
        perca_pontos = 20

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos :-)!!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou!! O seu chute foi maior que o número secreto.")

            elif (menor):
                print("Você errou!! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("Que pena!!! O número secreto era {}. Você fez 0 pontos".format(numero_secreto))

            pontos = pontos - perca_pontos


    print("*****************")
    print("***Fim de Jogo***")
    print("*****************")

if(__name__ == "__main__"):
    jogar()
