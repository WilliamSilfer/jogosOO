import random as rd

def jogar():
    imprimir_mensagem_abertura()
    numero = gerar_numero_secreto()
    pontos_vida = 1000
    print("\n\nVocê Iniciariá com 1000 pontos de vida", numero)

    tentativas = selecionar_dificuldade()

    print(f'Você terá {tentativas} tentativas\n\n\n\n')
    for i in range(0, tentativas):
        chute = chute_feito()
        print(f'Tentativa de número {i + 1}')
        if (verificar_acerto(chute) == False):
            break

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        if (acertou):
            print(f'Você Acertou, sua pontuação é de {pontos_vida} pontos')
            break
        else:
            if (maior):
                print("Você errou, seu número é maior!!")
                pontos_perdidos = abs(numero - chute)
                pontos_vida = pontos_vida - pontos_perdidos
                print(f'Pontos de vida {pontos_vida}')
            elif (menor):
                print("Você errou, seu número é menor!!")
                pontos_perdidos = abs(numero - chute)
                pontos_vida = pontos_vida - pontos_perdidos
                print(f'Pontos de vida {pontos_vida}')
        if (pontos_vida) <= 0:
            print("Fim de jogo, seus pontos de vida foram zerados!!")
            break
    print("O número é: ", numero)

def selecionar_dificuldade():
    numero = round(rd.random() * 100)
    nivel = int(input("\n\n\n\nQual o nível desejado 1 - Fácil 15 tentativas"
                      "/ 2 - Médio 10 tentativas/ 3 - Aleatorio: "))
    if (nivel == 1):
        tentativas = 15
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = numero
    return tentativas

def chute_feito():
    chute = int(input("Digite um número entre 1 e 100: "))
    print("\n\n\nNúmero digitado: ", chute)
    return chute

def verificar_acerto(erro):
    if (erro < 1 or erro > 100):
        print("O número digitado é menor que 0 ou maior que 100!!")
        return False
    else:
        return True

def imprimir_mensagem_abertura():
    print("__Alura__")
    print("*******************************************"
          "\nBem-Vindo no jogo de adivinhação!\n*******************************************")

def gerar_numero_secreto():
    numero = round(rd.random() * 100)
    return numero

if (__name__ == "__main__"):
    jogar()
