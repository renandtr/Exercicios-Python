import random
print('=========DESAFIO19=========')
aluno1 = input(print('Digite o nome do primeiro aluno: '))
aluno2 = input(print('Digite o nome do segundo aluno:'))
aluno3 = input(print('Digite o nome do terceiro aluno'))
aluno4 = input(print('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
quadro = random.choice(lista)
print('O aluno escolhido para apagar o quadro foi? {} '.format(quadro))
