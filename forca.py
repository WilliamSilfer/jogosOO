import random as rm

def jogar():
      imprime_mensagem_abertura()
      palavra_secreta = carregar_palavra_secreta()
      palavras_acertadas = inicializa_letras_acertadas(palavra_secreta)

      enforcou = False
      acertou = False
      erro = 0

# Começo do jogo
      while (not acertou and not enforcou):
            print(palavras_acertadas)
            print(f'Letras faltando: {palavras_acertadas.count("_")}')
            chute = pede_chute()

# Verificando o chute
            if (chute in palavra_secreta):
                  marca_chute_correto(chute, palavras_acertadas, palavra_secreta)
            else:
                  erro += 1
                  desenha_forca(erro)
                  print("Erros: ", erro)

# Verificando o andamento/encerramento do jogo
            enforcou = erro == 7
            acertou = "_" not in palavras_acertadas
            if acertou:
                  imprime_mensagem_ganhador(palavras_acertadas)
            elif enforcou:
                  imprime_mensagem_perdedor(palavra_secreta)


# Função de mensagem de abertura
def imprime_mensagem_abertura():
      print("__Alura__")
      print("*******************************************"
            "\nBem-Vindo no jogo da Forca!\n*******************************************")

# Função para inicializar letras acertadas
def inicializa_letras_acertadas(palavra):
      return ["_" for i in palavra]

# Função para carregar palavras secretas
def carregar_palavra_secreta():
      with open("arquivo.txt") as arquivo:
            lista_palavras = []
            for i in arquivo:
                  lista_palavras.append(i.strip())
            arquivo.close()
      numero = rm.randrange(0, len(lista_palavras))
      palavra_secreta = lista_palavras[numero].upper()
      return  palavra_secreta

# Função para chutes
def pede_chute():
      chute = input("Digite a letra: ").strip().upper()
      return chute

# Função para validar o chute
def marca_chute_correto(chute, palavras_acertadas, palavra_secreta):
      index = 0
      for i in palavra_secreta:
            if i == chute:
                  palavras_acertadas[index] = i
            index += 1
# Função para Imprimir mensagem de derrtoa
def imprime_mensagem_perdedor(palavra_secreta):
            print("Fim de game, você perdeu!! A palavra era", palavra_secreta)
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

# Função para Imprimir mensagem de vitória
def imprime_mensagem_ganhador(palavras_acertadas):
      print("Fim de jogo, você venceu!! A Palavra é ", palavras_acertadas)
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

# Função para imprimir o desenho forca
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Fim da execução
if (__name__ == "__main__"):
      jogar()
