from random import *

#imprima as 3 portas e as instruçoes do jogo
print('''
porta da fortuna!
=========

existe um super premio atras de uma das 3 portas!
adivinhe qual e a porta certa para ganhar o premio


 _____   _____   _____
|     | |     | |     |
| (1) | | (2) | | (3) |
|    o| |    o| |    o|
|_____| |_____| |_____|


''')

#deixe o jogador fazer 3 tentativas
for attemt in range(3):

    print("\nEscolha uma porta (1, 2, 3): ")

    #pegue a porta escolhida e a armazene como um numero inteiro (int)
    portaescolhida = input()
    portaescolhida = int(portaescolhida)

    
#escolha aleatoriamente a porta que esconde o premio (entre 1 e 3)
portacerta = randint(1,3)

#mostre ao jogador qual porta ele escolheu e qual era a porta certa
print("A porta escolhida foi a", portaescolhida)
print("A porta certa é a", portacerta)

#o jogador ganha se o numero da porta escolhida e o da porta certa forem o mesmo
if portaescolhida == portacerta:
    print("parabens!")
else:
    print("Que pena!")
