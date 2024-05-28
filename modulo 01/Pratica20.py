from random import shuffle
print('=========DESAFIO20=========')
aluno1 = input(print('Digite o nome Do primeiro aluno '))
aluno2 = input(print('Digite o nome do segundo aluno: '))
aluno3 = input(print('Digite o nome o terceiro aluno: '))
aluno4 = input(print('Digite o nome do quarto aluno'))
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print(lista)
