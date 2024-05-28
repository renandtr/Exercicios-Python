print('=========DESAFIO28=========')
import random
from time import sleep
numero = int(input('Descubra o nümero entre 0 e 5 que estou pensando: '))
print('Processando........')
sleep(3)
if numero <=5:
    num = random.randint(0,5)
    if numero == num:
        print('O numero que estou pensando é {}, parabéns voce acertou!'.format(num))
    else:
        print('O numero que estou pensando é {}, infelizmente voce errou'.format(num))
else:
    print('Erro')
