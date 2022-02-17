import forca
import adivinhacao

print("__Alura__")
print("*******************************************"
      "\nBem-Vindo Escolha seu Jogo!\n*******************************************")

print("(1) - Forca // (2) - Adivinhação")
jogo = int(input("Qual Jogo deseja?: "))

if jogo == 1:
      print("Jogando Forca")
      forca.jogar()
elif jogo == 2:
      print("Jogando Adivinhação")
      adivinhacao.jogar()
else:
      print("Error!")
