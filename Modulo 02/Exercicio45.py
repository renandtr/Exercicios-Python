import random
import time
print('=========DESAFIO45=========')
print('Escolha Suas Opções: ')
print('0- Pedra')
print('1- Papel')
print('2- Tesoura')
lista = ('pedra', 'papel', 'tesoura')
jogador = int(input('Qual sua jogada? '))
print('Pedra,Papel,Tesoura........')
print('Pedra,Papel,Tesoura........')
print('Pedra,Papel,Tesoura........')
time.sleep(3)
cpu = random.randint(0, 2)
if jogador == 0:
    if cpu == 0:
        print('=-' * 11)
        print('Jogador jogou pedra')
        print('Computador jogou pedra')
        print('Deu empate')
        print('=-' * 11)
    elif cpu == 1:
        print('=-' * 11)
        print('Jogador jogou pedra')
        print('Computador jogou papel')
        print('Computador venceu!!')
        print('=-' * 11)
    elif cpu == 2:
        print('=-' * 11)
        print('Jogador jogou pedra')
        print('Computador jogou tesoura')
        print('Computador perdeu!!')
        print('=-' * 11)
elif jogador == 1:
    if cpu == 0:
        print('=-' * 11)
        print('Jogador jogou papel')
        print('Computador jogou pedra')
        print('Computador perdeu!!')
        print('=-' * 11)
    elif cpu == 1:
        print('=-' * 11)
        print('Jogador jogou papel')
        print('Computador jogou papel')
        print('Deu empate!!')
        print('=-' * 11)
    elif cpu == 2:
        print('=-' * 11)
        print('Jogador jogou papel')
        print('Computador jogou tesoura')
        print('Computador venceu!!')
        print('=-' * 11)
elif jogador == 2:
    if cpu == 0:
        print('=-' * 11)
        print('Jogador jogou tesoura')
        print('Computador jogou pedra')
        print('Computador venceu!!')
        print('=-' * 11)
    elif cpu == 1:
        print('=-' * 11)
        print('Jogador jogou tesoura')
        print('Computador jogou papel')
        print('Computador perdeu!!')
        print('=-' * 11)
    elif cpu == 2:
        print('=-' * 11)
        print('Jogador jogou tesoura')
        print('Computador jogou tesoura')
        print('Deu empate!!')
        print('=-' * 11)
else:
    print('Opçâo invàlida!!')
